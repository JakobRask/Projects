-- High risk customers
SELECT
    customer_id,
    risk_score,
    loan_amount
FROM customer_portfolio
WHERE risk_score > 70
ORDER BY risk_score DESC;

-- Delinquency trends
SELECT
    report_month,
    AVG(delinquency_rate)
FROM portfolio_kris
GROUP BY report_month
ORDER BY report_month;

-- Concentration risk
SELECT
    region,
    SUM(loan_amount)
FROM customer_portfolio
GROUP BY region
ORDER BY SUM(loan_amount) DESC;