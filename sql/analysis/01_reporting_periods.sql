USE emtl_analysis;
DESCRIBE reporting_periods;

DESCRIBE recipient_mapping;

DESCRIBE emtl_observations;

-- which of the reporting periods have emtl line and which doesnt
SELECT revenue_month, allocation_month, emtl_line_present FROM reporting_periods ORDER BY revenue_month;