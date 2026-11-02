from pathlib import Path
from datetime import datetime
import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
)

# Project folders
PROJECT_ROOT = Path(__file__).resolve().parent.parent
REPORTS_DIR = PROJECT_ROOT / "reports"
REPORTS_DIR.mkdir(exist_ok=True)

# Input files
pnl_file = REPORTS_DIR / "profit_and_loss_report.csv"
balance_file = REPORTS_DIR / "balance_sheet_report.csv"
monthly_file = REPORTS_DIR / "monthly_financial_performance_report.csv"
budget_file = REPORTS_DIR / "budget_vs_actual_report.csv"

# Output PDF
pdf_file = REPORTS_DIR / "monthly_board_report.pdf"

# Load report data
files = {
    "Profit & Loss": pnl_file,
    "Balance Sheet": balance_file,
    "Monthly Performance": monthly_file,
    "Budget vs Actual": budget_file,
}

for report_name, file_path in files.items():
    if not file_path.exists():
        raise FileNotFoundError(
            f"Missing {report_name} report: {file_path}"
        )

pnl = pd.read_csv(pnl_file)
balance = pd.read_csv(balance_file)
monthly = pd.read_csv(monthly_file)
budget = pd.read_csv(budget_file)

styles = getSampleStyleSheet()
story = []

story.append(Paragraph(
    "Monthly Financial Board Report",
    styles["Title"]
))
story.append(Paragraph(
    f"Reporting period: January–December 2025",
    styles["Heading2"]
))
story.append(Paragraph(
    f"Generated on: {datetime.now():%d %B %Y, %I:%M %p}",
    styles["Normal"]
))
story.append(Spacer(1, 18))

def add_dataframe_table(title, dataframe, max_rows=15):
    story.append(Paragraph(title, styles["Heading2"]))

    display_df = dataframe.head(max_rows).fillna("")
    data = [list(display_df.columns)]
    data += display_df.astype(str).values.tolist()

    table = Table(data, repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1F4E78")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTSIZE", (0, 0), (-1, -1), 7),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1),
         [colors.white, colors.HexColor("#EAF2F8")]),
    ]))
    story.append(table)
    story.append(Spacer(1, 15))

add_dataframe_table("Profit and Loss Summary", pnl)
add_dataframe_table("Balance Sheet Summary", balance)
add_dataframe_table("Monthly Financial Performance", monthly)
add_dataframe_table("Budget vs Actual Analysis", budget)

story.append(Spacer(1, 10))
story.append(Paragraph(
    "Note: This report uses synthetic project data for academic "
    "demonstration. It is not an audited financial statement.",
    styles["Italic"]
))

document = SimpleDocTemplate(
    str(pdf_file),
    pagesize=A4,
    rightMargin=30,
    leftMargin=30,
    topMargin=35,
    bottomMargin=35
)

document.build(story)

print(f"Board report generated successfully: {pdf_file}")