## reported_emtl_amount
- Definition: EMTL amount shown in the FAAC report for one revenue month
- Formula: none, taken as reported
- Unit: naira (₦), full amount, not billions
- Time basis: revenue_month (from the table title, not the file name)
- Grain: one row per revenue month
- Source: Excel Sum & FG, Table I, EMTL column
- Rules: use the EMTL column, never "Others"; include the EMTL amount in the RMAFC row
- Limits: allocation, not transfers counted
- Validation: matches the PDF page 4 figure to the nearest ₦0.01bn