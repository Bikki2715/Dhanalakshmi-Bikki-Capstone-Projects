import pandas as pd
from pathlib import Path

# Load processed dataset
file_path = (
    Path(__file__).resolve().parent.parent
    / "data" / "processed" / "german_credit_clean.csv"
)

df = pd.read_csv(file_path)

# 1. Summary statistics
print("NUMERICAL SUMMARY")
print(df[[
    "duration_months",
    "credit_amount",
    "installment_rate",
    "age",
    "existing_credits"
]].describe().round(2))

# 2. Average values by credit-risk group
print("\nAVERAGE VALUES BY CREDIT RISK")
print(
    df.groupby("default_flag")[[
        "duration_months",
        "credit_amount",
        "installment_rate",
        "age"
    ]].mean().round(2)
)

# 3. Risk rate by checking account
print("\nBAD CREDIT RATE BY CHECKING ACCOUNT")
print(
    df.groupby("checking_account")["default_flag"]
    .agg(["count", "mean"])
    .assign(bad_credit_percentage=lambda x: x["mean"] * 100)
    .round(2)
)

# 4. Risk rate by loan purpose
print("\nBAD CREDIT RATE BY LOAN PURPOSE")
print(
    df.groupby("purpose")["default_flag"]
    .agg(["count", "mean"])
    .assign(bad_credit_percentage=lambda x: x["mean"] * 100)
    .round(2)
)
