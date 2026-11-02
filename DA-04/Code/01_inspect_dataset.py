import pandas as pd
from pathlib import Path

# Locate dataset
file_path = Path(__file__).resolve().parent.parent / "data" / "raw" / "german.data"

# Define column names
columns = [
    "checking_account",
    "duration_months",
    "credit_history",
    "purpose",
    "credit_amount",
    "savings_account",
    "employment_since",
    "installment_rate",
    "personal_status_sex",
    "other_debtors",
    "residence_since",
    "property",
    "age",
    "other_installment_plans",
    "housing",
    "existing_credits",
    "job",
    "dependents",
    "telephone",
    "foreign_worker",
    "credit_risk"
]

# Load dataset
df = pd.read_csv(file_path, sep=r"\s+", header=None, names=columns)

# Convert target into binary format
df["default_flag"] = df["credit_risk"].map({1: 0, 2: 1})

print("DATASET DIMENSIONS")
print(df.shape)

print("\nCOLUMN NAMES")
print(df.columns.tolist())

print("\nDUPLICATE RECORDS")
print(df.duplicated().sum())

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nCREDIT RISK DISTRIBUTION")
print(df["default_flag"].value_counts())

print("\nCREDIT RISK PERCENTAGES")
print((df["default_flag"].value_counts(normalize=True) * 100).round(2))

print("\nFIRST 5 RECORDS")
print(df.head())

# Save processed dataset
output_path = Path(__file__).resolve().parent.parent / "data" / "processed"

output_path.mkdir(parents=True, exist_ok=True)

df.to_csv(output_path / "german_credit_clean.csv", index=False)

print("\nPROCESSED DATASET SAVED SUCCESSFULLY")
print(output_path / "german_credit_clean.csv")