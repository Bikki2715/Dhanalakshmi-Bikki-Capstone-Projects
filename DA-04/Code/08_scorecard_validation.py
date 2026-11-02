
import pandas as pd
from pathlib import Path

# Load scorecard results
file_path = (
    Path(__file__).resolve().parent.parent
    / "reports"
    / "07_credit_risk_scorecard.csv"
)

df = pd.read_csv(file_path)

print("========== SCORECARD OVERVIEW ==========")
print("Dataset shape:", df.shape)
print(df.head())

# 1. Score distribution
print("\n========== SCORE DISTRIBUTION ==========")
print(df["credit_score"].describe().round(2))

print("\nScore percentiles:")
print(
    df["credit_score"]
    .quantile([0.10, 0.25, 0.50, 0.75, 0.90])
    .round(2)
)

# 2. Risk band validation
print("\n========== RISK BAND VALIDATION ==========")

risk_summary = (
    df.groupby("risk_band", observed=True)
    .agg(
        applicants=("actual_bad_credit", "count"),
        average_score=("credit_score", "mean"),
        observed_bad_rate=("actual_bad_credit", "mean"),
        average_predicted_probability=(
            "predicted_bad_probability", "mean"
        )
    )
)

risk_summary["observed_bad_rate"] *= 100
risk_summary["average_predicted_probability"] *= 100

print(risk_summary.round(2))

# 3. Score group validation
print("\n========== SCORE GROUP VALIDATION ==========")

df["score_group"] = pd.qcut(
    df["credit_score"],
    q=5,
    duplicates="drop"
)

score_summary = (
    df.groupby("score_group", observed=True)
    .agg(
        applicants=("actual_bad_credit", "count"),
        average_score=("credit_score", "mean"),
        observed_bad_rate=("actual_bad_credit", "mean"),
        predicted_bad_rate=(
            "predicted_bad_probability", "mean"
        )
    )
)

score_summary["observed_bad_rate"] *= 100
score_summary["predicted_bad_rate"] *= 100

print(score_summary.round(2))

# 4. Save validation reports
output_path = (
    Path(__file__).resolve().parent.parent
    / "reports"
)

risk_summary.to_csv(
    output_path / "08_risk_band_validation.csv"
)

score_summary.to_csv(
    output_path / "08_score_group_validation.csv"
)

print("\nVALIDATION REPORTS SAVED SUCCESSFULLY")
print(output_path)
