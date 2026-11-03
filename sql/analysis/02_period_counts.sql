-- count periods with and without the emtl
USE emtl_analysis;
DESCRIBE reporting_periods;
SELECT COUNT(*) AS total_periods, SUM(emtl_line_present=1) AS periods_with_emtl, SUM(emtl_line_present=0) AS periods_without_emtl FROM reporting_periods;