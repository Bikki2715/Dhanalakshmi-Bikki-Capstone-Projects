-- ==========================================
-- 01: PROFIT AND LOSS STATEMENT
-- Financial Analytics and Risk Reporting System
-- ==========================================

WITH financial_summary AS (
    SELECT
        SUM(
            CASE
                WHEN account_type = 'Revenue'
                THEN credit - debit
                ELSE 0
            END
        ) AS total_revenue,

        SUM(
            CASE
                WHEN account_type = 'Expense'
                THEN debit - credit
                ELSE 0
            END
        ) AS total_expenses

    FROM financial_ledger
    WHERE account_type IN ('Revenue', 'Expense')
)

SELECT
    total_revenue,
    total_expenses,

    total_revenue - total_expenses AS net_profit,

    ROUND(
        (total_revenue - total_expenses)
        / NULLIF(total_revenue, 0) * 100,
        2
    ) AS net_profit_margin_percentage

FROM financial_summary;