-- ==========================================
-- 04: BUDGET VS ACTUAL ANALYSIS
-- Financial Analytics and Risk Reporting System
-- ==========================================

WITH budget_summary AS (
    SELECT
        budget_month,

        SUM(
            CASE
                WHEN account_type = 'Revenue'
                    THEN budget_amount
                ELSE 0
            END
        ) AS revenue_budget,

        SUM(
            CASE
                WHEN account_type = 'Expense'
                    THEN budget_amount
                ELSE 0
            END
        ) AS expense_budget

    FROM project_monthly_budget_2025

    GROUP BY budget_month
),

actual_summary AS (
    SELECT
        DATE_TRUNC('month', transaction_date)::DATE
            AS reporting_month,

        SUM(
            CASE
                WHEN account_type = 'Revenue'
                    THEN credit - debit
                ELSE 0
            END
        ) AS actual_revenue,

        SUM(
            CASE
                WHEN account_type = 'Expense'
                    THEN debit - credit
                ELSE 0
            END
        ) AS actual_expenses

    FROM financial_ledger

    WHERE account_type IN ('Revenue', 'Expense')

    GROUP BY DATE_TRUNC('month', transaction_date)
)

SELECT
    TO_CHAR(b.budget_month, 'Mon YYYY')
        AS reporting_month,

    b.revenue_budget,
    a.actual_revenue,

    a.actual_revenue - b.revenue_budget
        AS revenue_variance,

    b.expense_budget,
    a.actual_expenses,

    a.actual_expenses - b.expense_budget
        AS expense_variance,

    b.revenue_budget - b.expense_budget
        AS budgeted_profit,

    a.actual_revenue - a.actual_expenses
        AS actual_profit,

    (a.actual_revenue - a.actual_expenses)
        - (b.revenue_budget - b.expense_budget)
        AS profit_variance

FROM budget_summary b

JOIN actual_summary a
    ON b.budget_month = a.reporting_month

ORDER BY b.budget_month;