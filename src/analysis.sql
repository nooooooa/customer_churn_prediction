SELECT
    churn,
    COUNT(*) AS total_customers
FROM customers
GROUP BY churn;

-- Churn rate calculation
SELECT
    COUNT(*) AS total_customers,
    SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*),
        2
    ) AS churn_rate
FROM customers;

-- Churn Rate by Contract
SELECT
    contract,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        AVG(
            CASE WHEN churn = 'Yes' THEN 1.0 ELSE 0.0 END
        ) * 100,
        2
    ) AS churn_rate
FROM customers
GROUP BY contract
ORDER BY churn_rate DESC;

-- Churn Rate by tenure group
SELECT
    CASE
        WHEN tenure <= 12 THEN '0-12 Months'
        WHEN tenure <= 24 THEN '13-24 Months'
        WHEN tenure <= 48 THEN '25-48 Months'
        ELSE '49-72 Months'
    END AS tenure_group,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        AVG(CASE WHEN churn = 'Yes' THEN 1.0 ELSE 0.0 END) * 100,
        2
    ) AS churn_rate
FROM customers
GROUP BY tenure_group
ORDER BY MIN(tenure);