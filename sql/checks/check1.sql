-- checking row counts
SELECT (SELECT COUNT(*) FROM source_files)      AS source_files,
       (SELECT COUNT(*) FROM reporting_periods) AS reporting_periods,
       (SELECT COUNT(*) FROM emtl_observations) AS emtl_observations;

SELECT COUNT(*) AS periods,
       SUM(emtl_line_present = 1) AS with_emtl,
       SUM(emtl_line_present = 0) AS without_emtl
FROM reporting_periods;

-- check if there is any staging label with no row in recipient_mapping
SELECT DISTINCT TRIM(s.row_label_raw) AS unmapped_label
FROM stg_emtl_table1 s
LEFT JOIN recipient_mapping m ON m.row_label_raw = TRIM(s.row_label_raw)
WHERE s.row_type IN ('detail', 'total') AND m.row_label_raw IS NULL;

-- check observations by categories
SELECT recipient_category, COUNT(*) AS rows_loaded,
       SUM(amount_ngn <> 0) AS non_zero_rows, SUM(amount_ngn IS NULL) AS blank_rows
FROM emtl_observations
GROUP BY recipient_category
ORDER BY recipient_category;

-- sum of detail rows compared to the total rows
SELECT rp.revenue_month,
       MAX(CASE WHEN o.row_type = 'total'  THEN o.amount_ngn END) AS total_amount,
       SUM(CASE WHEN o.row_type = 'detail' THEN o.amount_ngn END) AS detail_sum
FROM reporting_periods rp JOIN emtl_observations o USING (period_id)
GROUP BY rp.period_id, rp.revenue_month
HAVING ABS(SUM(CASE WHEN o.row_type = 'detail' THEN o.amount_ngn END)
         - MAX(CASE WHEN o.row_type = 'total'  THEN o.amount_ngn END)) > 0.01;

-- check for duplicated periods or source cell
SELECT period_id, source_cell, COUNT(*) AS n
FROM emtl_observations GROUP BY period_id, source_cell HAVING COUNT(*) > 1;

USE emtl_analysis;

CREATE TEMPORARY TABLE audit_totals (
    revenue_month DATE PRIMARY KEY,
    amount_ngn    DECIMAL(24,2) NOT NULL
);

INSERT INTO audit_totals (revenue_month, amount_ngn) VALUES
    ('2024-07-01', 19602075826.00),
    ('2024-08-01', 15642981643.52);

SELECT a.revenue_month, a.amount_ngn AS audit_total, o.amount_ngn AS loaded_total
FROM audit_totals a
LEFT JOIN reporting_periods rp ON rp.revenue_month = a.revenue_month
LEFT JOIN emtl_observations o  ON o.period_id = rp.period_id AND o.row_type = 'total'
WHERE o.amount_ngn IS NULL OR ABS(o.amount_ngn - a.amount_ngn) > 0.005;


-- check again before rebuid test
SELECT (SELECT COUNT(*) FROM source_files) AS source_files,
		(SELECT COUNT(*) FROM reporting_periods) AS reporting_periods,
		(SELECT COUNT(*) FROM emtl_observations) AS emtl_observations,
		(SELECT COUNT(*) FROM stg_emtl_table1) AS staging_rows;