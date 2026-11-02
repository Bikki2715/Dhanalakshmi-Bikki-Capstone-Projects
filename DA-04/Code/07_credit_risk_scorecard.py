
from pathlib import Path

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

# 1. Load dataset
project_dir = Path(__file__).resolve().parent.parent

file_path = (
    project_dir / "data" / "processed" / "german_credit_clean.csv"
)

df = pd.read_csv(file_path)

# 2. Exclude target and sensitive features
target = "default_flag"

excluded = [
    "credit_risk",
    "default_flag",
    "personal_status_sex",
    "foreign_worker"
]

X = df.drop(columns=excluded)
y = df[target]

# 3. Split dataset
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

# 5. Create numerical bins using training data
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
    result = pd.DataFrame(index=data.index)

    for col in numerical_columns:
        result[col] = pd.cut(
            data[col],
            bins=bin_edges[col],
            labels=False,
            include_lowest=True
        )

    for col in categorical_columns:
        result[col] = data[col].astype(str)

    return result


train_grouped = prepare_features(X_train)
test_grouped = prepare_features(X_test)

# 6. Calculate WoE from training data
woe_mappings = {}

for col in train_grouped.columns:

    grouped = pd.DataFrame({
        "feature": train_grouped[col],
        "target": y_train
    }).groupby("feature")["target"].agg(
        ["count", "sum"]
    )

    grouped["bad"] = grouped["sum"]
    grouped["good"] = grouped["count"] - grouped["bad"]

    good_dist = (
        (grouped["good"] + 0.5) /
        (grouped["good"].sum() + 0.5 * len(grouped))
    )

    bad_dist = (
        (grouped["bad"] + 0.5) /
        (grouped["bad"].sum() + 0.5 * len(grouped))
    )

    woe_mappings[col] = np.log(
        good_dist / bad_dist
    ).to_dict()


def apply_woe(data):
    result = pd.DataFrame(index=data.index)

    for col in data.columns:
        result[col] = (
            data[col]
            .map(woe_mappings[col])
            .fillna(0)
        )

    return result


X_train_woe = apply_woe(train_grouped)
X_test_woe = apply_woe(test_grouped)

# 7. Train WoE Logistic Regression
model = LogisticRegression(max_iter=2000)

model.fit(X_train_woe, y_train)

# 8. Predict bad-credit probability
probabilities = model.predict_proba(X_test_woe)[:, 1]

print("Model ROC-AUC:", round(
    roc_auc_score(y_test, probabilities), 4
))

# 9. Convert probability into credit score
# Higher score = lower estimated bad-credit probability

base_score = 600
base_odds = 50
points_to_double_odds = 20

factor = points_to_double_odds / np.log(2)
offset = base_score - factor * np.log(base_odds)

probabilities = np.clip(
    probabilities, 1e-6, 1 - 1e-6
)

good_bad_odds = (
    (1 - probabilities) / probabilities
)

scores = offset + factor * np.log(good_bad_odds)

scores = np.round(scores).astype(int)

# 10. Assign risk bands
def assign_risk(score):
    if score >= 600:
        return "Low"
    elif score >= 550:
        return "Moderate"
    else:
        return "High"


risk_bands = [assign_risk(score) for score in scores]

# 11. Create scorecard output
scorecard = pd.DataFrame({
    "actual_bad_credit": y_test.values,
    "predicted_bad_probability": probabilities,
    "credit_score": scores,
    "risk_band": risk_bands
})

# 12. Summarize risk bands
summary = scorecard.groupby("risk_band").agg(
    applicants=("credit_score", "count"),
    average_score=("credit_score", "mean"),
    observed_bad_credit_rate=("actual_bad_credit", "mean"),
    average_bad_probability=("predicted_bad_probability", "mean")
)

summary["observed_bad_credit_rate"] *= 100
summary["average_bad_probability"] *= 100

print("\nCREDIT RISK SCORECARD SUMMARY")
print(summary.round(2))

# 13. Save results
output_dir = project_dir / "reports"
output_dir.mkdir(parents=True, exist_ok=True)

scorecard.to_csv(
    output_dir / "07_credit_risk_scorecard.csv",
    index=False
)

summary.to_csv(
    output_dir / "07_credit_risk_band_summary.csv"
)

print("\nScorecard files saved successfully.")
