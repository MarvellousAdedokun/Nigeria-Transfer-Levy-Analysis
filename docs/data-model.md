# Data Model

Database: `emtl_analysis`

## 1. What this database is for

This database holds the Electronic Money Transfer Levy (EMTL) figures from the official FAAC monthly reports. It lets me ask questions with SQL, such as how the reported EMTL changed from month to month, while keeping a trail back to the exact cell in the exact source workbook.

The figures are what the reports show as allocated. They are not a count of transfers.

## 2. The three layers

I keep the data in layers. Each layer has one job.

| Layer | Tables | Job |
|---|---|---|
| Raw (staging) | `stg_emtl_table1` | An exact copy of the extracted CSV. Everything is text. Nothing is cleaned or changed. |
| Clean (core) | `source_files`, `reporting_periods`, `emtl_observations`, `recipient_mapping` | Real dates, real numbers, one row per thing, and rules that stop bad data. |
| Answers | views and queries (Phase 7) | Built only from the clean layer. |

Why layers: if a number looks wrong, I can walk back through the layers and find the step that changed it. The raw layer is never edited, so it is always there as evidence.

## 3. The tables

### `stg_emtl_table1` (raw copy)
- **One row is:** one row of the extraction CSV (281 rows).
- **Key:** `stg_id`, a number the database assigns.
- **Contains:** all 29 CSV columns as text, plus `loaded_at`.
- **Why it exists:** it keeps the extraction evidence exactly as it came in, including blank values and period text.

### `source_files` (one row per workbook)
- **One row is:** one FAAC workbook (23 rows).
- **Key:** `source_file_id`. `source_path` must be unique.
- **Contains:** file name, path, checksum (`sha256`) and the sheet and title used.
- **Why it exists:** every clean row can say which workbook it came from.

### `reporting_periods` (one row per report)
- **One row is:** one report (23 rows).
- **Key:** `period_id`. Each `source_file_id` and each `revenue_month` appears once.
- **Connects to:** `source_files` through `source_file_id`.
- **Contains:** `revenue_month` (when the revenue was generated), `allocation_month` (when it was shared), whether an EMTL column was found, and the extraction status.
- **Why it exists:** it keeps the two months separate and records which reports have no EMTL line.

### `recipient_mapping` (label review)
- **One row is:** one distinct row label from Table I.
- **Key:** `row_label_raw`.
- **Contains:** the original label, a reviewed category, and a review status.
- **Why it exists:** labels are spelled in different ways. I decide what each one means on purpose, and I record that decision. I never change the original label.

### `emtl_observations` (the clean amounts)
- **One row is:** one Table I row for one report (275 rows: 258 detail and 17 total).
- **Key:** `observation_id`. The pair `(period_id, source_cell)` must be unique.
- **Connects to:** `reporting_periods` through `period_id`.
- **Contains:** the original label, the category, `row_type`, the source cell, and `amount_ngn`.
- **Why it exists:** these are the amounts I analyse. The `source_cell` tells me exactly where each number came from in the workbook.

### The helper view `v_stg_periods`
- It reads the period text in staging (such as `July , 2025`), removes the commas and extra spaces, and turns it into real dates.
- I use a view so the date logic lives in one place.

## 4. How the tables connect

```
source_files  1 ---- 1  reporting_periods  1 ---- many  emtl_observations
                                   
stg_emtl_table1  (raw copy; the clean tables are built from it)
recipient_mapping (label decisions; used when building the observations)
```

## 5. Choices I made, and why

- **`DECIMAL(24,4)` for money.** It stores exact numbers. Some source cells have up to four decimals, and approximate number types can drift.
- **Blank means NULL, never zero.** A blank cell is missing information. A zero is a value.
- **Six reports have no EMTL column.** They are kept as reports with status "column not found". They have no observations and are not zero.
- **Two month columns.** Revenue month and allocation month are separate, and I never work one out from the other.
- **Case-insensitive labels in the mapping.** The database treats `Non-oil` and `non-oil` as the same text. Two labels that differ only by case therefore share one mapping row. Each observation still holds its original spelling.
- **Foreign keys.** They stop an observation from pointing at a report that does not exist.
- **Unique keys.** They stop the same cell from being loaded twice, which makes reruns safe.
- **Raw data is never edited.** All cleaning happens in the later tables.

## 6. How to rebuild the database

1. Create the database and staging table.
2. Create the mapping, core tables and the period view.
3. Load the mapping and the staging data. The staging loader is `python src/load/load_staging.py staging`, run from the repository root.
4. Run the three transform statements (source files, reporting periods, observations).
5. Run the checks in `sql/checks/` and record the results in `docs/validation-log.md`.

To rebuild only the clean layer, empty `emtl_observations`, `reporting_periods` and `source_files` (in that order, with foreign key checks switched off for the moment), then run the three transform statements again. The staging data and the mapping are not touched.

## 7. Rules for using this data in Phase 7

1. **Use `row_type = 'detail'` for recipient amounts.** Total rows are in the same table only for checking. Adding detail and total together would count everything twice.
2. **NULL is not zero.** A blank amount must stay out of sums unless I decide otherwise and write down why.
3. **Reports with no EMTL column are missing data, not zero collections.**
4. **Revenue month and allocation month are different.** Always say which one a chart or table uses.
5. **Only use mappings that have been reviewed** for any result that depends on recipient categories.
6. **Say what the data can and cannot show.** These are reported allocations. They do not show transfers made or who paid.

## 8. Current counts (to re-check if the data changes)

| Item | Count |
|---|---|
| Workbooks (`source_files`) | 23 |
| Reports (`reporting_periods`) | 23 |
| Staging rows | 281 |
| Staging rows by type | 258 detail, 17 total, 6 missing_column |
| Reports with EMTL / without | 17 / 6 |
| Observations | 275 (258 detail, 17 total) |

## 9. Known limits

- The reports do not say why EMTL is missing from February to July 2026.
- Some recipient labels are still waiting for review.
- The figures come from FAAC reports. They are allocations, not transfer counts.
