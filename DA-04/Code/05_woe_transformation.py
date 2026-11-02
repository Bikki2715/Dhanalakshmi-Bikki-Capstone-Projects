from pathlib import Path
import pandas as pd
import numpy as np

# Load cleaned dataset
project_dir = Path(__file__).resolve().parent.parent
file_path = project_dir / "data" / "processed" / "german_credit_clean.csv"

df = pd.read_csv(file_path)

# Define target
target = "default_flag"

# Select numerical and categorical features
numerical_columns = df.select_dtypes(include=["number"]).columns.tolist()
numerical_columns = [
    col for col in numerical_columns
    if col not in ["credit_risk", "default_flag"]
]

categorical_columns = df.select_dtypes(exclude=["number"]).columns.tolist()

# Create bins for numerical features
for col in numerical_columns:
    df[col + "_bin"] = pd.qcut(
        df[col],
        q=5,
        duplicates="drop"
    )

# Calculate WoE and IV
def calculate_woe(data, feature, target):
    grouped = data.groupby(feature, observed=False)[target].agg(
        ["count", "sum"]
    )

    grouped["good"] = grouped["count"] - grouped["sum"]
    grouped["bad"] = grouped["sum"]

    grouped["good_dist"] = (
        grouped["good"] / grouped["good"].sum()
    )

    grouped["bad_dist"] = (
        grouped["bad"] / grouped["bad"].sum()
    )

    grouped["woe"] = np.log(
        grouped["good_dist"] / grouped["bad_dist"]
    )

    grouped["iv"] = (
        grouped["good_dist"] - grouped["bad_dist"]
    ) * grouped["woe"]

    return grouped

# Calculate for categorical features
results = []

for col in categorical_columns:
    table = calculate_woe(df, col, target)
    results.append({
        "feature": col,
        "information_value": table["iv"].sum()
    })

# Calculate for numerical features
for col in numerical_columns:
    bin_col = col + "_bin"
    table = calculate_woe(df, bin_col, target)
    results.append({
        "feature": col,
        "information_value": table["iv"].sum()
    })

# Display IV results
iv_results = pd.DataFrame(results)
iv_results = iv_results.sort_values(
    "information_value",
    ascending=False
)

print("\nINFORMATION VALUE RESULTS")
print(iv_results.to_string(index=False))

# Save results
output_dir = project_dir / "reports"
output_dir.mkdir(parents=True, exist_ok=True)

iv_results.to_csv(
    output_dir / "05_information_value_results.csv",
    index=False
)

print("\nWoE and IV analysis completed.")