USE emtl_analysis;
-- sumarry of amounts in detail rows by category
SELECT 
	recipient_category,
    COUNT(*) AS details_rows,
    SUM(amount_ngn <> 0) AS non_zero_rows,
    SUM(amount_ngn IS NULL) AS blank_amount_rows,
    SUM(amount_ngn) AS sum_of_recorded_amounts_ngn
FROM emtl_observations
WHERE row_type = 'detail'
GROUP BY recipient_category
ORDER BY recipient_category;

-- check the total when sums are added against report totals
-- return reports where the detail sum differs from the total by more that 0.01
SELECT
	rp.revenue_month,
    MAX(CASE WHEN o.row_type = 'total'
				THEN o.amount_ngn END) AS total_amaount_ngn,
	SUM(CASE WHEN o.row_type = 'detail'
				THEN o.amount_ngn END) AS detail_sum_ngn,
	SUM(CASE WHEN o.row_type = 'detail'
				THEN o.amount_ngn END) 
	- MAX(CASE WHEN o.row_type = 'total'
				THEN o.amount_ngn END) AS difference_ngn
FROM reporting_periods AS rp 
JOIN emtl_observations AS o
	ON o.period_id = rp.period_id
GROUP BY rp.period_id, rp.revenue_month
HAVING ABS(
	SUM(CASE WHEN o.row_type = 'detail' THEN o.amount_ngn END)
    - MAX(CASE WHEN o.row_type = 'total' THEN o.amount_ngn END)
    ) > 0.01
ORDER BY rp.revenue_month;

-- check and investigate the periods without EMTL headings
SELECT 
    revenue_month,
    allocation_month,
    emtl_line_present,
    extraction_status
FROM
    reporting_periods
WHERE
    emtl_line_present = 0
ORDER BY revenue_month;