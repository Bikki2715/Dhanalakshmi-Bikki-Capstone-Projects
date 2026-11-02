# Financial Analytics and Risk Reporting System — Architecture

```mermaid
flowchart TD
    A[Data Sources]

    A --> B[Financial Ledger CSV]
    A --> C[Chart of Accounts CSV]
    A --> D[Monthly Budget CSV]
    A --> E[German Credit Dataset]

    B --> F[PostgreSQL Database]
    C --> F
    D --> F

    B --> G[Python Data Processing]
    E --> G

    G --> H[EDA and Data Cleaning]
    H --> I[Logistic Regression and WoE]
    I --> J[Credit Risk Scorecard]

    F --> K[SQL Financial Reporting]
    K --> L[Profit and Loss]
    K --> M[Balance Sheet]
    K --> N[Budget vs Actual]

    L --> O[Power BI Dashboard]
    M --> O
    N --> O

    L --> P[Qlik Sense Dashboard]
    M --> P
    N --> P

    J --> Q[Credit Risk Reports]
    O --> R[Financial Reporting]
    P --> R
    Q --> R
```

## Architecture Explanation

1. **Data Sources:** Financial ledger, chart of accounts, monthly budget and German Credit dataset.
2. **PostgreSQL:** Stores financial data and supports SQL reporting.
3. **Python:** Performs data cleaning, exploratory analysis and credit risk modeling.
4. **Credit Risk Model:** Uses Logistic Regression and WoE to generate a risk scorecard.
5. **Power BI and Qlik Sense:** Provide interactive financial dashboards.
6. **Reports:** Present financial performance and credit risk findings.