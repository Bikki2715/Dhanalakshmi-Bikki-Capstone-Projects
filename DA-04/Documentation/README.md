# Financial Analytics and Risk Reporting System

## 1. Project Overview

The Financial Analytics and Risk Reporting System is a data analytics project designed to analyze financial performance, monitor budget deviations, and assess credit risk using data analytics and business intelligence tools.

## 2. Project Objectives

- Analyze Profit and Loss statements.
- Generate Balance Sheet summaries.
- Compare budgeted and actual financial performance.
- Identify key financial variance drivers.
- Develop a credit risk classification model.
- Build interactive financial dashboards.

## 3. Tools and Technologies

- **Python:** Data cleaning, exploratory data analysis, and credit risk modeling.
- **Pandas and NumPy:** Data processing.
- **Scikit-learn:** Logistic Regression.
- **PostgreSQL:** Financial database and SQL reporting.
- **Power BI:** Financial performance dashboards.
- **Qlik Sense:** Interactive financial analytics dashboards.
- **DAX:** Financial calculations and KPIs.

## Tools and Implementation Note

Microsoft Excel with Power Pivot was part of the original project requirements. However, I did not have access to Microsoft Excel with Power Pivot during development. Therefore, I used **Power BI Desktop** as an alternative for data modeling, financial analysis, KPI calculations, and dashboard development.

The financial data was loaded into Power BI, relationships were created between tables, and DAX measures were used to calculate financial KPIs and budget variances. The dashboards were also developed using Power BI and Qlik Sense.

This implementation provides the required financial reporting and visualization functionality, although a separate Excel Power Pivot workbook was not created.

## Steps to Run the Project

### 1. Python Environment
- Install Python 3.12 or later.
- Open the project folder in VS Code.
- Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn reportlab
```

### 2. Run Python Scripts
- Navigate to the `Code` folder.
- Run the Python scripts in numerical order where applicable.
- The scripts perform data inspection, cleaning, exploratory analysis, credit risk modeling, scorecard development, and report generation.

Example:

```bash
python 01_inspect_dataset.py
```

Run the scripts from the project directory and ensure the required datasets are available in the `Datasets` folder.

### 3. Run SQL Reports
- Install PostgreSQL.
- Create the project database.
- Import the financial ledger, chart of accounts, and budget data.
- Open the SQL files in pgAdmin and execute them to generate the financial reports.

### 4. Open Dashboards
- Open `Financial_Analytics_Dashboard.pbix` using Power BI Desktop.
- Open the `.qvf` file using Qlik Sense, where supported.
- If prompted, update the data source paths to match your local project folders.

### 5. Generate the Monthly Board Report
Run the Python script:

```bash
python 10_generate_monthly_board_report.py
```

The generated PDF is saved in the Reports folder.

## Data Disclaimer

The financial ledger and budget data used in this project are synthetic and were created for educational and demonstration purposes. The credit risk analysis uses the German Credit dataset. The results are intended for academic demonstration and are not validated for real-world lending decisions.


## 4. Key Modules

### Financial Reporting
- Profit and Loss statement.
- Balance Sheet.
- Monthly financial performance.

### Budget vs Actual Analysis
- Budget and actual revenue.
- Budget and actual expenses.
- Profit variance analysis.

### Credit Risk Analysis
- Data preprocessing.
- Exploratory data analysis.
- Logistic Regression.
- Weight of Evidence (WoE).
- Credit risk scorecard.

## 5. Credit Risk Model Results

| Model | ROC-AUC |
|---|---:|
| Logistic Regression | 0.8040 |
| WoE Logistic Regression | 0.8027 |

The model uses the German Credit dataset containing 1,000 records. Results are based on a held-out test set and are intended for educational analysis.

## 6. Financial Summary

The synthetic financial ledger contains 285 transaction rows across 2025.

- Total Revenue: ₹795,000
- Total Expenses: ₹661,200
- Net Profit: ₹133,800
- Profit Margin: 16.83%

These figures are illustrative project data, not actual company financial results.

## 7. Project Deliverables

- Processed datasets.
- SQL scripts and financial summaries.
- Python credit risk analysis.
- Credit risk validation report.
- Power BI dashboard.
- Qlik Sense dashboard.

## 8. Limitations

The financial ledger and budget figures are synthetic. The credit risk model uses a small historical dataset and should not be used for real lending decisions without further validation.

## 9. Conclusion

This project demonstrates how SQL, Python, statistical modeling, and business intelligence tools can be combined to support financial reporting, performance monitoring, and credit risk analysis.