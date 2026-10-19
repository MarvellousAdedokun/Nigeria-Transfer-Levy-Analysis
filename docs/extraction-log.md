# Table I EMTL extraction log

This log records what the script found in each Excel workbook. It does not treat a missing EMTL column as zero.

- Raw directory: `data\raw\faac`
- Excel workbooks processed: 23
- Staging rows written: 281
- Status counts: `{'found': 17, 'column_not_found': 6}`

| Source workbook | Sheet | Title cell | Revenue period (raw) | Allocation period (raw) | Heading row | EMTL heading cell | TOTAL label cell | EMTL total cell | Overall total cell | Status | Rows | Sum check | Manual fix | Warning |
|---|---|---|---|---|---:|---|---|---|---|---|---:|---|---|---|
| Disbursement April, 2025.xlsx | Sum & FG | A4 | March, 2025 | April, 2025 | 5 | E5 | B22 | E22 | G22 | found | 16 | True | No |  |
| Disbursement April, 2026.xlsx | Sum & FG | A4 | March, 2026 | April, 2026 | 5 |  | B20 |  | G20 | column_not_found | 1 |  | No | No EMTL heading found in the Table I header row; this is missing/not reported, not zero. |
| Disbursement August, 2025.xlsx | Sum & FG | A4 | July , 2025 | August, 2025 | 6 | E6 | B25 | E25 | H25 | found | 18 | True | No |  |
| Disbursement December, 2025.xlsx | Sum & FG | A4 | November, 2025 | December, 2025 | 6 | D6 | B21 | D21 | G21 | found | 14 | True | No |  |
| Disbursement February, 2025.xlsx | Sum & FG | A4 | January, 2025 | February, 2025 | 5 | E5 | B23 | E23 | G23 | found | 17 | True | No |  |
| Disbursement February, 2026.xlsx | Sum & FG | A4 | January, 2026 | February, 2026 | 5 |  | B19 |  | F19 | column_not_found | 1 |  | No | No EMTL heading found in the Table I header row; this is missing/not reported, not zero. |
| Disbursement January, 2025.xlsx | Sum & FG | A4 | December, 2024 | January, 2025 | 5 | E5 | B22 | E22 | G22 | found | 16 | True | No |  |
| Disbursement July, 2026.xlsx | Sum & FG | A4 | June, 2026 | July, 2026 | 5 |  | B25 |  | F25 | column_not_found | 1 |  | No | No EMTL heading found in the Table I header row; this is missing/not reported, not zero. |
| Disbursement June, 2025.xlsx | Sum & FG | A4 | May , 2025 | June, 2025 | 5 | E5 | B23 | E23 | G23 | found | 17 | True | No |  |
| Disbursement June, 2026.xlsx | Sum & FG | A4 | May, 2026 | June, 2026 | 5 |  | B21 |  | E21 | column_not_found | 1 |  | No | No EMTL heading found in the Table I header row; this is missing/not reported, not zero. |
| Disbursement March, 2025.xlsx | Sum & FG | A4 | February, 2025 | March, 2025 | 5 | F5 | B22 | F22 | H22 | found | 16 | True | No |  |
| Disbursement March, 2026.xlsx | Sum & FG | A4 | February, 2026 | March, 2026 | 5 |  | B20 |  | E20 | column_not_found | 1 |  | No | No EMTL heading found in the Table I header row; this is missing/not reported, not zero. |
| Disbursement May, 2025.xlsx | Sum & FG | A4 | April, 2025 | May, 2025 | 5 | E5 | B22 | E22 | G22 | found | 16 | True | No |  |
| Disbursement May, 2026.xlsx | Sum & FG | A4 | April, 2026 | May, 2026 | 5 |  | B21 |  | F21 | column_not_found | 1 |  | No | No EMTL heading found in the Table I header row; this is missing/not reported, not zero. |
| Disbursement_ July, 2025.xlsx | Sum & FG | A4 | June , 2025 | July, 2025 | 6 | E6 | B25 | E25 | I25 | found | 18 | True | No |  |
| Disbursement_December_2024.xlsx | Sum & FG | A4 | November, 2024 | December, 2024 | 5 | E5 | B22 | E22 | G22 | found | 16 | True | No |  |
| Disbursement_November_2024.xlsx | Sum & FG | A4 | October, 2024 | November, 2024 | 5 | E5 | B22 | E22 | H22 | found | 16 | True | No |  |
| Disbursement_November_2025.xlsx | Sum & FG | A4 | October, 2025 | November, 2025 | 6 | D6 | B22 | D22 | G22 | found | 15 | True | No |  |
| Disbursement_October_2025.xlsx | Sum & FG | A4 | September, 2025 | October, 2025 | 6 | D6 | B21 | D21 | G21 | found | 14 | True | No |  |
| Disbursement_September_2024.xlsx | Sum & FG | A4 | August, 2024 | September, 2024 | 5 | E5 | B22 | E22 | G22 | found | 16 | True | No |  |
| Disbursement_September_2025.xlsx | Sum & FG | A4 | August, 2025 | September, 2025 | 6 | E6 | B26 | E26 | H26 | found | 19 | True | No |  |
| FAAC_Disbursement_August_2024.xlsx | Sum & FG | A4 | July, 2024 | August, 2024 | 5 | F5 | B23 | F23 | H23 | found | 17 | True | No |  |
| FAAC_Disbursement_January_2026.xlsx | Sum & FG | A4 | December, 2025 | January, 2026 | 6 | D6 | B21 | D21 | G21 | found | 14 | True | No |  |

## Review notes

- `found` means the EMTL heading was located in Table I; it does not mean the amount is positive.
- `column_not_found` means the Table I heading row did not contain an EMTL heading. It does not mean EMTL collected or distributed was zero.
- `sum_matches_total` in the staging CSV checks whether the extracted detail cells add to the Table I EMTL TOTAL after rounding to two decimal places.
- Any warning must be reviewed before the staging table is used for analysis.
\n## Duplicate workbook copies skipped\n\nNo duplicate workbook bytes were found.\n