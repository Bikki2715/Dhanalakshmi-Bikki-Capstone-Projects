-- ==========================================
-- 03: MONTHLY FINANCIAL PERFORMANCE
-- Financial Analytics and Risk Reporting System
-- ==========================================

SELECT
    TO_CHAR(
        DATE_TRUNC('month', transaction_date),
        'Mon YYYY'
    ) AS reporting_month,

    DATE_TRUNC('month', transaction_date)::DATE
        AS month_date,

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
    ) AS total_expenses,

    SUM(
        CASE
            WHEN account_type = 'Revenue'
                THEN credit - debit
            WHEN account_type = 'Expense'
                THEN credit - debit
            ELSE 0
        END
    ) AS net_profit,

    ROUND(
        SUM(
            CASE
                WHEN account_type = 'Revenue'
                    THEN credit - debit
                WHEN account_type = 'Expense'
                    THEN credit - debit
                ELSE 0
            END
        )
        /
        NULLIF(
            SUM(
                CASE
                    WHEN account_type = 'Revenue'
                        THEN credit - debit
                    ELSE 0
                END
            ),
            0
        ) * 100,
        2
    ) AS profit_margin_percentage

FROM financial_ledger

WHERE
    account_type IN ('Revenue', 'Expense')
    AND transaction_date >= '2025-01-01'
    AND transaction_date < '2026-01-01'

GROUP BY DATE_TRUNC('month', transaction_date)

ORDER BY month_date;