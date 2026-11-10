# Nexvia Capstone Projects

This repository contains two data analytics capstone projects: **DA-03 – Retail Supply Chain Control Tower** and **DA-04 – Financial Analytics and Risk Reporting System**. Together, they demonstrate practical work in data engineering, SQL, Python analytics, predictive modeling, business intelligence, dashboard development, and workflow automation.

## Project Overview

| Project | Focus | Main Technologies |
|---|---|---|
| [DA-03 – Retail Supply Chain Control Tower](DA-03/README.md) | Inventory, shipments, supplier performance, demand forecasting, anomaly detection, and operational alerts | Python, Pandas, PostgreSQL, Apache Airflow, Apache Superset, Prophet, Docker |
| [DA-04 – Financial Analytics and Risk Reporting System](DA-04/Documentation/README.md) | Financial statements, budget-versus-actual analysis, credit risk modeling, scorecards, and board reporting | Python, Pandas, Scikit-learn, PostgreSQL, Power BI, Qlik Sense, DAX |

---

## DA-03 – Retail Supply Chain Control Tower

**Objective:** Build an analytics solution to monitor retail supply-chain operations, identify operational risks, forecast demand, and present actionable insights through dashboards and automated notifications.

### Key Components

- **Data processing:** Cleaned and prepared supplier, product, inventory, shipment, and demand-history data using Python.
- **Database and SQL:** Stored and analyzed supply-chain data in PostgreSQL and created KPI views.
- **Operational KPIs:** Analyzed stock-out rate, delivery performance, supplier lead time, and inventory coverage.
- **Anomaly detection:** Identified unusual shipment lead times and demand spikes.
- **Demand forecasting:** Used Prophet to forecast demand for 20 selected products and assess potential stockout risk.
- **Dashboard:** Built an interactive Apache Superset dashboard for inventory, shipment, supplier, forecast, and anomaly insights.
- **Workflow monitoring:** Configured Apache Airflow checks and Gmail SMTP notifications, using Docker for local services.

### Dataset and Results

The project uses five datasets containing **426,100 records** in total:

| Dataset | Records |
|---|---:|
| Suppliers | 100 |
| Products | 1,000 |
| Inventory | 10,000 |
| Shipments | 50,000 |
| Demand history | 365,000 |
| **Total** | **426,100** |

Selected analytical results:

- Stock-out rate: **0.21%**
- On-time delivery rate: **43.25%**
- Average supplier lead time: **18.32 days**
- Average days of inventory: **81.59 days**
- Unusual shipment lead-time records detected: **33**
- Demand spikes detected: **768**
- Forecast coverage: **20 products** (17 classified as high stockout risk and 3 as moderate)

**Workflow note:** The hourly Airflow workflow checks existing database tables, records refresh status, evaluates available risk summaries, and supports email alerts. It does not regenerate source data or rerun the forecasting and anomaly-detection models every hour.

**Project links:** [Project folder](DA-03/) · [Detailed README](DA-03/README.md) · [Dashboard PDF](DA-03/Superset/retail-supply-chain-control-tower-inventory-operations-dashboard-2026-11-07T10-31-04.295Z.pdf) · [Dashboard export](DA-03/Superset/Retail_Supply_Chain_Dashboard_Export.zip) · [Project showcase website](https://retail-supply-chain-control-tower-v.vercel.app/)

---

## DA-04 – Financial Analytics and Risk Reporting System

**Objective:** Analyze financial performance, summarize financial statements, identify budget variances, and develop an educational credit-risk scorecard.

### Key Components

- **Financial reporting:** Used SQL and PostgreSQL to prepare Profit and Loss, Balance Sheet, and monthly financial performance summaries.
- **Budget analysis:** Compared budgeted and actual revenue, expenses, and profit to identify variance drivers.
- **Credit risk analysis:** Used the German Credit dataset for exploratory analysis and credit-risk classification.
- **Predictive modeling:** Built Logistic Regression and Weight of Evidence (WoE) Logistic Regression models.
- **Risk scorecard:** Converted model probabilities into score bands and evaluated their performance.
- **Business intelligence:** Developed financial dashboards in Power BI and Qlik Sense.
- **Board reporting:** Generated a monthly financial board report in PDF format.

### Financial and Model Results

The synthetic financial data produced the following illustrative summary:

| Metric | Result |
|---|---:|
| Total revenue | ₹795,000 |
| Total expenses | ₹661,200 |
| Net profit | ₹133,800 |
| Profit margin | 16.83% |

Credit-risk model results on the held-out test data:

| Model | ROC-AUC |
|---|---:|
| Logistic Regression | 0.8040 |
| WoE Logistic Regression | 0.8027 |

**Implementation note:** Excel Power Pivot was part of the original requirement. Since Excel with Power Pivot was not available during development, Power BI Desktop was used for data modeling, DAX calculations, KPI reporting, and dashboard development. A separate Excel Power Pivot workbook was not created.

**Data and model disclaimer:** The financial ledger and budget data are synthetic and intended for educational demonstration. The credit-risk analysis uses the German Credit dataset and is not validated or approved for real-world lending decisions.

**Project links:** [Project folder](DA-04/) · [Detailed documentation](DA-04/Documentation/README.md)

---

## Skills Demonstrated

- Python programming and data analysis
- Data cleaning, transformation, and exploratory data analysis
- SQL and PostgreSQL
- KPI development and financial / operational reporting
- Predictive modeling, anomaly detection, and demand forecasting
- Credit-risk analysis and scorecard validation
- Power BI, Qlik Sense, and Apache Superset dashboards
- Workflow orchestration with Apache Airflow
- Docker-based local development and Gmail SMTP alerting
- Technical documentation and project reporting

## Getting Started

1. Open the relevant project folder.
2. Read its project README and documentation for setup instructions.
3. Review the source code, datasets, SQL scripts, reports, dashboards, and screenshots.
4. Follow the project-specific instructions before running scripts or connecting dashboards to local data sources.

Each project has its own dependencies and setup process; refer to its documentation before execution.
