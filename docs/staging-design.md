# Phase 5 — Staging Table Design

## Grain

One row per source cell in the EMTL column of Table I, including the Table I `TOTAL` row. A workbook with no EMTL heading gets one explicit sentinel row so the missing column is recorded rather than silently dropped.

## Fields

| Field | Meaning |
|---|---|
| `source_file` | Workbook filename as supplied by the source |
| `source_path` | Relative source path; ZIP members use `archive.zip::member.xlsx` |
| `source_container` | ZIP archive name when the workbook came from an archive |
| `sha256` | SHA-256 checksum of the workbook bytes |
| `archive_sha256` | SHA-256 checksum of the original ZIP, if applicable |
| `sheet` | Worksheet used for Table I |
| `title_cell` | Cell containing the Table I title, observed as `A4` |
| `title_raw` | Original title text from the workbook |
| `revenue_period_raw` | Month/year text taken from the title, not converted to a date |
| `allocation_period_raw` | Sharing month/year text from the title, or filename fallback |
| `allocation_period_source` | `title`, `filename_fallback`, or `not_stated` |
| `header_row` | Row containing Table I column headings |
| `header_cell` | Exact cell containing the EMTL heading |
| `header_label_raw` | EMTL heading text as written in the workbook |
| `row_label_cell` | Cell containing the Table I row label, normally column B |
| `row_label_raw` | Row label such as FGN, State, LGCs, FIRS, RMAFC, or TOTAL |
| `cell` | Exact EMTL source cell for this row |
| `value_raw` | Numeric value read from the cell; blank if the cell is blank |
| `row_type` | `detail`, `total`, `missing_column`, or `extraction_error` |
| `emtl_found` | Whether an EMTL heading was found in Table I |
| `status` | Extraction status such as `found` or `column_not_found` |
| `total_label_cell` | Exact cell containing the Table I TOTAL label |
| `emtl_total_cell` | EMTL value cell on the Table I TOTAL row |
| `emtl_total_value_raw` | EMTL total as stored in that cell |
| `overall_total_cell` | Overall `Total` column cell on the same row (not the EMTL total) |
| `overall_total_value_raw` | Overall Table I total, kept separate from EMTL |
| `detail_sum_raw` | Sum of EMTL detail cells, excluding the TOTAL row |
| `sum_matches_total` | Whether detail values equal the EMTL total to two decimal places |
| `warning` | Any extraction or validation warning |

## Missing-column rule

For February 2026, the Table I heading row has no EMTL column. The staging table records one row with `row_type=missing_column`, `emtl_found=False`, and `status=column_not_found`. The overall table total is retained for context, but the EMTL value stays blank. This means “not reported in this table,” not zero.

## Why keep the periods raw?

The project should not turn text into dates during extraction. Keeping the original title and period strings makes the extraction traceable. Period cleaning and standard date fields belong in Phase 6.
