# Data Dictionary
## Financial Analytics and Risk Reporting System

This document describes the datasets used in the project.

## 1. Financial Ledger (`financial_ledger.csv`)

| Column | Description | Data Type |
|---|---|---|
| journal_id | Unique journal entry identifier | Integer |
| transaction_date | Date of financial transaction | Date |
| account_code | Unique account code | Text |
| account_name | Name of the financial account | Text |
| account_type | Revenue, Expense, Asset, Liability or Equity | Text |
| description | Transaction description | Text |
| debit | Debit transaction amount | Decimal |
| credit | Credit transaction amount | Decimal |

## 2. Chart of Accounts (`chart_of_accounts.csv`)

| Column | Description | Data Type |
|---|---|---|
| account_code | Unique account identifier | Text |
| account_name | Account name | Text |
| account_type | Financial account classification | Text |

## 3. Monthly Budget (`monthly_budget_2025.csv`)

| Column | Description | Data Type |
|---|---|---|
| budget_month | Budget reporting month | Date |
| account_code | Related account code | Text |
| account_name | Account name | Text |
| account_type | Financial account classification | Text |
| budget_amount | Planned monthly financial amount | Decimal |

## 4. Credit Risk Dataset (`german_credit_clean.csv`)

The cleaned German Credit dataset contains 1,000 records and 20 original input features, along with derived and target columns.

Important fields include:

| Field | Description |
|---|---|
| checking_account | Checking account status |
| duration | Credit duration in months |
| credit_history | Previous credit history |
| purpose | Purpose of the loan |
| credit_amount | Requested credit amount |
| savings_account | Savings account status |
| employment | Employment duration category |
| installment_rate | Installment rate |
| personal_status_sex | Personal status and sex category |
| other_debtors | Other debtors or guarantors |
| present_residence | Duration at current residence |
| property | Property category |
| age | Applicant age |
| other_installment_plans | Other installment plans |
| housing | Housing category |
| existing_credits | Number of existing credits |
| job | Employment category |
| dependents | Number of dependents |
| telephone | Telephone availability |
| foreign_worker | Foreign worker indicator |
| credit_risk | Original credit classification |
| default_flag | Derived binary target: 0 = Good, 1 = Bad |

## 5. Data Quality and Preparation

- Checked missing values and duplicate records.
- Standardized date and numeric fields.
- Validated debit and credit balancing.
- Prepared the credit dataset for exploratory analysis and model development.
- Excluded sensitive features from the final WoE credit risk model.

## 6. Data Sources

- Financial ledger and budget: Synthetic project-generated data.
- Credit risk: UCI Statlog German Credit dataset.

**Note:** Data types describe the intended analytical representation. Actual storage types may differ between CSV, PostgreSQL, Power BI and Qlik Sense.