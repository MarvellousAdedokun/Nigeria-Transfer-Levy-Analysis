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

