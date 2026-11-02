-- ==========================================
-- 02: BALANCE SHEET
-- Financial Analytics and Risk Reporting System
-- ==========================================

WITH account_balances AS (
    SELECT
        account_code,
        account_name,
        account_type,

        CASE
            WHEN account_type = ('Asset','Contra Asset')
                THEN SUM(debit - credit)

            WHEN account_type IN ('Liability', 'Equity')
                THEN SUM(credit - debit)

            ELSE 0
        END AS balance

    FROM financial_ledger
    WHERE account_type IN ('Asset', 'Liability', 'Equity')
    GROUP BY
        account_code,
        account_name,
        account_type
),

current_year_profit AS (
    SELECT
        SUM(
            CASE
                WHEN account_type = 'Revenue'
                    THEN credit - debit
                WHEN account_type = 'Expense'
                    THEN credit - debit
                ELSE 0
            END
        ) AS net_profit

    FROM financial_ledger
    WHERE account_type IN ('Revenue', 'Expense')
),

balance_sheet_items AS (
    SELECT
        account_type,
        account_name,
        balance
    FROM account_balances

    UNION ALL

    SELECT
        'Equity',
        'Current Year Net Profit',
        net_profit
    FROM current_year_profit
),

balance_sheet_totals AS (
    SELECT
        SUM(
            CASE WHEN account_type = 'Asset'
                THEN balance ELSE 0 END
        ) AS total_assets,

        SUM(
            CASE WHEN account_type = 'Liability'
                THEN balance ELSE 0 END
        ) AS total_liabilities,

        SUM(
            CASE WHEN account_type = 'Equity'
                THEN balance ELSE 0 END
        ) AS total_equity

    FROM balance_sheet_items
)

SELECT
    total_assets,
    total_liabilities,
    total_equity,

    total_liabilities + total_equity
        AS total_liabilities_and_equity,

    total_assets - (total_liabilities + total_equity)
        AS balance_difference,

    CASE
        WHEN ABS(
            total_assets - (total_liabilities + total_equity)
        ) < 0.01
        THEN 'BALANCED'
        ELSE 'NOT BALANCED'
    END AS balance_status

FROM balance_sheet_totals;