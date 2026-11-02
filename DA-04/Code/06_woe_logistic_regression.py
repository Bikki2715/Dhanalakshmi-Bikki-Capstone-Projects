
from pathlib import Path

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    roc_auc_score
)

# 1. Load dataset
project_dir = Path(__file__).resolve().parent.parent
file_path = project_dir / "data" / "processed" / "german_credit_clean.csv"

df = pd.read_csv(file_path)

# 2. Define target and exclude sensitive variables
target = "default_flag"

excluded = [
    "credit_risk",
    "default_flag",
    "personal_status_sex",
    "foreign_worker"
]

X = df.drop(columns=excluded)
y = df[target]

# 3. Split before calculating WoE
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# 4. Identify feature types
numerical_columns = X_train.select_dtypes(
    include=["number"]
).columns.tolist()

categorical_columns = X_train.select_dtypes(
    exclude=["number"]
).columns.tolist()

# 5. Create numerical bins using training data only
bin_edges = {}

for col in numerical_columns:
    _, edges = pd.qcut(
        X_train[col],
        q=5,
        retbins=True,
        duplicates="drop"
    )

    edges[0] = -np.inf
    edges[-1] = np.inf
    bin_edges[col] = edges

def prepare_features(data):
    transformed = pd.DataFrame(index=data.index)

    for col in numerical_columns:
        transformed[col] = pd.cut(
            data[col],
            bins=bin_edges[col],
            labels=False,
            include_lowest=True
        )

    for col in categorical_columns:
        transformed[col] = data[col].astype(str)

    return transformed

X_train_grouped = prepare_features(X_train)
X_test_grouped = prepare_features(X_test)

# 6. Calculate WoE mappings from training data
woe_mappings = {}
iv_results = []

for col in X_train_grouped.columns:

    grouped = pd.DataFrame({
        "feature": X_train_grouped[col],
        "target": y_train
    }).groupby("feature", dropna=False)["target"].agg(
        ["count", "sum"]
    )

    grouped["bad"] = grouped["sum"]
    grouped["good"] = grouped["count"] - grouped["bad"]

    # Smoothing avoids division by zero
    good_dist = (
        (grouped["good"] + 0.5) /
        (grouped["good"].sum() + 0.5 * len(grouped))
    )

    bad_dist = (
        (grouped["bad"] + 0.5) /
        (grouped["bad"].sum() + 0.5 * len(grouped))
    )

    woe = np.log(good_dist / bad_dist)

    iv = ((good_dist - bad_dist) * woe).sum()

    woe_mappings[col] = woe.to_dict()

    iv_results.append({
        "feature": col,
        "information_value": iv
    })

# 7. Apply training WoE mappings to both datasets
def apply_woe(data):
    result = pd.DataFrame(index=data.index)

    for col in data.columns:
        mapping = woe_mappings[col]

        result[col] = (
            data[col]
            .map(mapping)
            .fillna(0)
        )

    return result

X_train_woe = apply_woe(X_train_grouped)
X_test_woe = apply_woe(X_test_grouped)

# 8. Train WoE Logistic Regression
model = LogisticRegression(max_iter=2000)

model.fit(X_train_woe, y_train)

# 9. Predictions
y_pred = model.predict(X_test_woe)
y_probability = model.predict_proba(X_test_woe)[:, 1]

# 10. Evaluation
print("\nWOE LOGISTIC REGRESSION COMPLETED")

print("\nCONFUSION MATRIX")
print(confusion_matrix(y_test, y_pred))

print("\nCLASSIFICATION REPORT")
print(classification_report(
    y_test,
    y_pred,
    zero_division=0
))

print("\nROC-AUC SCORE")
print(round(roc_auc_score(y_test, y_probability), 4))

# 11. Save IV results
output_dir = project_dir / "reports"
output_dir.mkdir(parents=True, exist_ok=True)

iv_df = pd.DataFrame(iv_results).sort_values(
    "information_value",
    ascending=False
)

iv_df.to_csv(
    output_dir / "06_woe_information_value.csv",
    index=False
)

print("\nWOE INFORMATION VALUE RESULTS")
print(iv_df.to_string(index=False))

print("\nResults saved successfully.")
