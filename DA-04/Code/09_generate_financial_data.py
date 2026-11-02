
import pandas as pd
from pathlib import Path

# Project paths
project_path = Path(__file__).resolve().parent.parent
raw_path = project_path / "data" / "raw"
raw_path.mkdir(parents=True, exist_ok=True)

# Chart of accounts
accounts = [
    (1000, "Cash", "Asset"),
    (1100, "Accounts Receivable", "Asset"),
    (1200, "Inventory", "Asset"),
    (1500, "Equipment", "Asset"),
    (1590, "Accumulated Depreciation", "Contra Asset"),
    (2000, "Accounts Payable", "Liability"),
    (2100, "Loan Payable", "Liability"),
    (2200, "Tax Payable", "Liability"),
    (3000, "Owner Capital", "Equity"),
    (3100, "Retained Earnings", "Equity"),
    (4000, "Sales Revenue", "Revenue"),
    (5000, "Cost of Goods Sold", "Expense"),
    (5100, "Salaries Expense", "Expense"),
    (5200, "Rent Expense", "Expense"),
    (5300, "Marketing Expense", "Expense"),
    (5400, "Utilities Expense", "Expense"),
    (5500, "Depreciation Expense", "Expense"),
    (5600, "Interest Expense", "Expense"),
    (5700, "Tax Expense", "Expense")
]

account_df = pd.DataFrame(
    accounts,
    columns=["account_code", "account_name", "account_type"]
)

account_lookup = {
    code: (name, account_type)
    for code, name, account_type in accounts
}

ledger = []

def add_entry(entry_id, date, description, entries):
    """Add balanced debit and credit lines to the general ledger."""
    total_debit = sum(item[1] for item in entries)
    total_credit = sum(item[2] for item in entries)

    if round(total_debit, 2) != round(total_credit, 2):
        raise ValueError(f"Unbalanced journal entry: {entry_id}")

    for code, debit, credit in entries:
        name, account_type = account_lookup[code]

        ledger.append({
            "journal_entry_id": entry_id,
            "transaction_date": date,
            "account_code": code,
            "account_name": name,
            "account_type": account_type,
            "description": description,
            "debit": round(debit, 2),
            "credit": round(credit, 2)
        })


# Opening balances: 1 January 2025
add_entry(
    "OPEN001",
    "2025-01-01",
    "Opening balances",
    [
        (1000, 100000, 0),
        (1100, 20000, 0),
        (1200, 30000, 0),
        (1500, 80000, 0),
        (1590, 0, 10000),
        (2000, 0, 15000),
        (2100, 0, 50000),
        (3000, 0, 100000),
        (3100, 0, 55000)
    ]
)


# Generate monthly financial transactions
for month in range(1, 13):

    date = f"2025-{month:02d}-28"

    revenue = 50000 + (2500 * month)
    cogs = revenue * 0.45
    salaries = 12000 + (100 * month)
    rent = 4000
    marketing = 2500 + (100 * month)
    utilities = 1200
    depreciation = 1000
    interest = 500

    pretax_profit = (
        revenue - cogs - salaries - rent
        - marketing - utilities - depreciation - interest
    )

    tax = max(0, pretax_profit * 0.20)

    # Sales: 80% cash and 20% credit
    add_entry(
        f"SALE{month:03d}",
        date,
        "Monthly sales",
        [
            (1000, revenue * 0.80, 0),
            (1100, revenue * 0.20, 0),
            (4000, 0, revenue)
        ]
    )

    # Cost of goods sold
    add_entry(
        f"COGS{month:03d}",
        date,
        "Monthly cost of goods sold",
        [
            (5000, cogs, 0),
            (1200, 0, cogs)
        ]
    )

    # Monthly operating expenses
    expenses = [
        ("SAL", 5100, salaries, "Monthly salaries"),
        ("REN", 5200, rent, "Monthly rent"),
        ("MKT", 5300, marketing, "Monthly marketing"),
        ("UTL", 5400, utilities, "Monthly utilities"),
        ("DEP", 5500, depreciation, "Monthly depreciation"),
        ("INT", 5600, interest, "Monthly interest")
    ]

    for prefix, code, amount, description in expenses:
        if code == 5500:
            add_entry(
                f"{prefix}{month:03d}",
                date,
                description,
                [
                    (code, amount, 0),
                    (1590, 0, amount)
                ]
            )
        else:
            add_entry(
                f"{prefix}{month:03d}",
                date,
                description,
                [
                    (code, amount, 0),
                    (1000, 0, amount)
                ]
            )

    # Inventory purchases on supplier credit
    purchases = cogs + 1000

    add_entry(
        f"PUR{month:03d}",
        date,
        "Monthly inventory purchases",
        [
            (1200, purchases, 0),
            (2000, 0, purchases)
        ]
    )

    # Pay 85% of monthly purchases
    supplier_payment = purchases * 0.85

    add_entry(
        f"PAY{month:03d}",
        date,
        "Monthly supplier payment",
        [
            (2000, supplier_payment, 0),
            (1000, 0, supplier_payment)
        ]
    )

    # Monthly income tax provision
    add_entry(
        f"TAX{month:03d}",
        date,
        "Monthly income tax provision",
        [
            (5700, tax, 0),
            (2200, 0, tax)
        ]
    )


# Convert ledger to DataFrame
ledger_df = pd.DataFrame(ledger)

# Save datasets
ledger_df.to_csv(
    raw_path / "financial_ledger.csv",
    index=False
)

account_df.to_csv(
    raw_path / "chart_of_accounts.csv",
    index=False
)

# Final data-quality checks
print("FINANCIAL DATA GENERATION COMPLETED")

print("\nLedger shape:", ledger_df.shape)
print("Number of accounts:", len(account_df))
print("Number of journal entries:",
      ledger_df["journal_entry_id"].nunique())

print("\nTotal debit:",
      round(ledger_df["debit"].sum(), 2))

print("Total credit:",
      round(ledger_df["credit"].sum(), 2))

print("\nDebit and credit balanced:",
      round(ledger_df["debit"].sum(), 2)
      == round(ledger_df["credit"].sum(), 2))

print("\nFiles saved:")
print(raw_path / "financial_ledger.csv")
print(raw_path / "chart_of_accounts.csv")
