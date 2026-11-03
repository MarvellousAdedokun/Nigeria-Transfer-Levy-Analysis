USE emtl_analysis;
DESCRIBE reporting_periods;
DESCRIBE emtl_observations;
-- which month has the highest emtl total and which has lowest

SELECT 
    rp.revenue_month, o.amount_ngn AS reported_emtl_total_ngn
FROM
    reporting_periods AS rp
        JOIN
    emtl_observations AS o ON o.period_id = rp.period_id
WHERE
    o.row_type = 'total'
        AND o.amount_ngn IS NOT NULL
ORDER BY o.amount_ngn DESC;

-- what is the emtl total for each year across available reported months
SELECT
	YEAR(rp.revenue_month) AS revenue_year,
    COUNT(*) AS reported_months,
    SUM(o.amount_ngn) AS total_reported_emtl_ngn
FROM reporting_periods AS rp
	JOIN emtl_observations AS o ON o.period_id = rp.period_id
    WHERE o.row_type = 'total'
AND o.amount_ngn IS NOT NULL
GROUP BY YEAR(rp.revenue_month)
ORDER BY revenue_year;

-- count the recipient categories and check their review status
SELECT 
    recipient_category,
    review_status,
    COUNT(*) AS number_of_labels
FROM
    recipient_mapping
GROUP BY recipient_category , review_status
ORDER BY recipient_category , review_status;