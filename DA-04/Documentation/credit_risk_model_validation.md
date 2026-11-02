
# Credit Risk Model – Methodology and Validation

## 1. Project Overview

This module analyzes customer credit-risk characteristics and classifies applicants into risk categories using Logistic Regression and Weight of Evidence (WoE).

Dataset: UCI Statlog German Credit Data

- Total records: 1,000
- Good-credit records: 700 (70%)
- Bad-credit records: 300 (30%)
- Training records: 800
- Testing records: 200

The original target classes were mapped as:
- Class 1 = Good credit (0)
- Class 2 = Bad credit (1)

The target represents the dataset's historical good/bad credit classification. It should not be interpreted as a guaranteed future default.

## 2. Data Preparation

- Loaded the original German Credit dataset.
- Assigned meaningful column names.
- Converted the target into a binary variable.
- Checked missing values and duplicate records.
- Confirmed 1,000 records and no missing values.
- Saved the cleaned dataset as german_credit_clean.csv.

## 3. Exploratory Data Analysis

Key observations:

- Average credit amount: 3,271.26
- Average loan duration: 20.90 months
- Average applicant age: 35.55 years.
- Average credit amount was higher among bad-credit applicants.
- Average loan duration was longer among bad-credit applicants.
- Applicants in checking-account category A11 had a higher bad-credit rate than those in A14.

These are associations in the dataset, not proof of causation.

## 4. Logistic Regression Model

A baseline Logistic Regression model was developed using an 80:20 train-test split.

Test results:

- Accuracy: 78%
- ROC-AUC: 0.8040
- Bad-credit precision: 0.67
- Bad-credit recall: 0.53
- Bad-credit F1-score: 0.59

Confusion matrix:

| Actual / Predicted | Good | Bad |
|---|---:|---:|
| Good | 124 | 16 |
| Bad | 28 | 32 |

## 5. Weight of Evidence Model

WoE was applied to transform categorical and numerical variables into risk-related numerical values.

Information Value (IV) was calculated to evaluate the predictive separation of individual features.

The WoE Logistic Regression model achieved:

- Accuracy: 78%
- ROC-AUC: 0.8027
- Bad-credit precision: 0.70
- Bad-credit recall: 0.47
- Bad-credit F1-score: 0.56

Sensitive variables such as personal_status_sex and foreign_worker were excluded from the final WoE model.

## 6. Model Comparison

| Metric | Baseline Logistic | WoE Logistic |
|---|---:|---:|
| Accuracy | 0.78 | 0.78 |
| ROC-AUC | 0.8040 | 0.8027 |
| Bad-credit precision | 0.67 | 0.70 |
| Bad-credit recall | 0.53 | 0.47 |
| Bad-credit F1 | 0.59 | 0.56 |

The baseline model achieved slightly higher ROC-AUC and recall. The WoE model achieved higher precision.

WoE did not improve every performance metric.

## 7. Credit Risk Scorecard

The WoE Logistic Regression model was converted into a points-based scorecard.

Scorecard parameters:

- Base score: 600
- Base odds: 50:1
- Points to Double the Odds (PDO): 20

Score conversion:

Score = Offset + Factor × ln((1 − p) / p)

Where:

- p = predicted bad-credit probability
- Factor = PDO / ln(2)
- Offset = Base score − Factor × ln(Base odds)

Provisional risk bands:

- Low: Score >= 600
- Moderate: Score >= 550 and < 600
- High: Score < 550

## 8. Scorecard Validation

The scorecard was evaluated on 200 test records.

| Risk band | Applicants | Observed bad-credit rate |
|---|---:|---:|
| High | 152 | 36.84% |
| Moderate | 44 | 9.09% |
| Low | 4 | 0.00% |

Score-group validation:

- Lowest-score group: 69.05% observed bad-credit rate.
- Highest-score group: 10.26% observed bad-credit rate.

The results show that lower scores generally correspond to higher observed bad-credit rates.

The Low-risk group contains only four applicants, so its observed rate is not statistically reliable.

## 9. Limitations

- The dataset contains only 1,000 historical records.
- The dataset may not represent current lending conditions.
- The test set contains only 200 records.
- Predicted probabilities are not perfectly calibrated.
- Risk-band thresholds are provisional.
- The model requires further validation, fairness assessment and independent testing before any real lending use.

## 10. Conclusion

The project successfully demonstrates credit-risk exploration, Logistic Regression, WoE transformation, Information Value analysis, scorecard development and test-set validation.

The model provides an educational demonstration of credit-risk classification. It is not approved for real-world lending decisions.

## 11. Supporting Files

- data/processed/german_credit_clean.csv
- reports/05_information_value_results.csv
- reports/06_woe_information_value.csv
- reports/07_credit_risk_scorecard.csv
- reports/07_credit_risk_band_summary.csv
- reports/08_risk_band_validation.csv
- reports/08_score_group_validation.csv
