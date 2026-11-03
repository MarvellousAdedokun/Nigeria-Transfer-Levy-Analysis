USE emtl_analysis;
DESCRIBE reporting_periods;
DESCRIBE emtl_observations;
SELECT row_type FROM emtl_observations;

-- check how emtl total changed over revenue month
SELECT
    rp.period_id,
    rp.revenue_month,
    rp.allocation_month,
    rp.emtl_line_present,
    MAX(
        CASE WHEN o.row_type = 'total'
             THEN o.amount_ngn
        END
    ) AS reported_emtl_total_ngn
FROM reporting_periods AS rp
LEFT JOIN emtl_observations AS o
    ON o.period_id = rp.period_id
GROUP BY
    rp.period_id,
    rp.revenue_month,
    rp.allocation_month,
    rp.emtl_line_present
ORDER BY rp.revenue_month;