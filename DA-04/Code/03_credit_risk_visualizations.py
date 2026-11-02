from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
project_dir = Path(__file__).resolve().parent.parent
file_path = project_dir / "data" / "processed" / "german_credit_clean.csv"

df = pd.read_csv(file_path)

# Create reports folder
output_dir = project_dir / "reports"
output_dir.mkdir(parents=True, exist_ok=True)

# 1. Good vs Bad Credit Distribution
credit_counts = df["default_flag"].value_counts().sort_index()

plt.figure(figsize=(7, 5))
plt.bar(["Good Credit", "Bad Credit"], credit_counts.values)
plt.title("Credit Risk Distribution")
plt.xlabel("Credit Category")
plt.ylabel("Number of Applicants")
plt.tight_layout()
plt.savefig(output_dir / "01_credit_risk_distribution.png", dpi=300)
plt.close()

print("Chart 1 saved successfully.")

# 2. Average Credit Amount by Credit Category

average_amount = df.groupby("default_flag")["credit_amount"].mean()

plt.figure(figsize=(7, 5))
plt.bar(
    ["Good Credit", "Bad Credit"],
    average_amount.values
)
plt.title("Average Credit Amount by Risk Category")
plt.xlabel("Credit Category")
plt.ylabel("Average Credit Amount")
plt.tight_layout()
plt.savefig(output_dir / "02_average_credit_amount.png", dpi=300)
plt.close()

print("Chart 2 saved successfully.")

# 3. Average Loan Duration by Credit Category

average_duration = df.groupby("default_flag")["duration_months"].mean()

plt.figure(figsize=(7, 5))
plt.bar(
    ["Good Credit", "Bad Credit"],
    average_duration.values
)
plt.title("Average Loan Duration by Credit Category")
plt.xlabel("Credit Category")
plt.ylabel("Average Duration (Months)")
plt.tight_layout()
plt.savefig(output_dir / "03_average_loan_duration.png", dpi=300)
plt.close()

print("Chart 3 saved successfully.")

# 4. Bad Credit Rate by Checking Account

checking_risk = (
    df.groupby("checking_account")["default_flag"].mean() * 100
).sort_values(ascending=False)

plt.figure(figsize=(9, 5))
plt.bar(checking_risk.index, checking_risk.values)

plt.title("Bad Credit Rate by Checking Account")
plt.xlabel("Checking Account Category")
plt.ylabel("Bad Credit Rate (%)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig(output_dir / "04_bad_credit_by_checking_account.png", dpi=300)
plt.close()

print("Chart 4 saved successfully.")