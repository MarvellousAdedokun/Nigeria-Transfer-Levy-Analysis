# Phase 6 Validation Log

This file is the record of the checks I ran on the EMTL database.
Expected values come from the Phase 6 guide. The **Actual** and **Result** columns are filled in with what I saw on my own machine.

- Date:
- Database and version (run `SELECT VERSION();`):
- Database name: `emtl_analysis`

---

## 1. Why this log exists

Loading data without errors does not prove the data is right. These checks answer three questions:

1. Did every row arrive? (counts)
2. Are the numbers the same as the source? (totals)
3. Can I rebuild the clean tables safely? (rerun test)

Rule: if a check fails, I do not edit or delete rows to make it pass. I write down what I saw, find the cause, and fix the cause.

---

## 2. Step 8 checks

| # | What I checked | Expected | Actual | Result (PASS / FAIL) |
|---|---|---|---|---|
| 1 | Rows in `source_files`, `reporting_periods`, `emtl_observations` | 23, 23, 275 | | |
| 2 | Reports with EMTL / without EMTL | 17 / 6 | | |
| 3 | Staging labels with no row in `recipient_mapping` | no rows | | |
| 4 | Observations with category `UNMAPPED` | no rows | | |
| 5 | Non-zero amounts by category | only FGN, STATES, LGCS, COST_OF_COLLECTION, RMAFC and TOTAL have non-zero amounts | | |
| 5b | Observations with a blank (NULL) amount | 8 (from an earlier test on 18 workbooks; confirm on the full data) | | |
| 6 | Reports where the detail rows differ from the total by more than 0.01 | no rows | | |
| 7 | Duplicate `(period_id, source_cell)` | no rows | | |
| 8 | Loaded totals that differ from `source-audit.md` | no rows | | |

Notes on how to read these:
- "No rows" is a pass. Those queries only list problems.
- A blank amount is stored as NULL, never as zero.

### What I saw (write anything unexpected here)

-

---

## 3. Step 9 rerun test

| Moment | `source_files` | `reporting_periods` | `emtl_observations` | `stg_emtl_table1` |
|---|---|---|---|---|
| Before the rerun (expected 23, 23, 275, 281) | | | | |
| After running the loader and the transform again (expected the same as above) | | | | |
| After emptying the three core tables (expected 0, 0, 0, and 281 in staging) | | | | |
| After running the transform again (expected 23, 23, 275, 281) | | | | |

Result: the rerun test **passes** if the first, second and last rows match and the empty row shows zeros.

- Result (PASS / FAIL):
- Problems and how I fixed them:

---

## 4. Decisions I made (and why)

1. **Blank amounts stay NULL.** A blank cell in the source is not the same as a zero, so it is stored as NULL.
2. **Six reports have no EMTL column.** These are the reports shared from February to July 2026 (as far as the extraction shows). They are recorded as "EMTL not reported in Table I". They are not zero collections, and they have no observation rows.
3. **Revenue month and allocation month are separate columns.** The month the revenue was generated and the month it was shared can differ. I never fill one from the other.
4. **The database ignores upper and lower case in labels.** Two labels that differ only by case, such as `Transfer to Non-oil Excess Account` and `Transfer to non-oil Excess account`, share one row in `recipient_mapping`. Each observation still keeps its original spelling. I still need to confirm that these two labels never carry a non-zero amount.
5. **Total rows are stored in `emtl_observations` with `row_type = 'total'`.** I use them to check the detail rows. Any analysis of recipients must use `row_type = 'detail'` only, or the numbers will be counted twice.
6. **Amounts use `DECIMAL(24,4)`.** Some source cells have up to four decimal places, and money must not use approximate numbers.
7. **Raw staging data is never edited.** All cleaning happens in the later tables.

---

## 5. Open items

- Why EMTL is missing from the 2026 reports is not explained in the reports.
- The recipient mapping still contains labels marked as needing review. Those must be reviewed before any analysis uses them.

---

## 6. Sign-off

Phase 6 passes when:
- [ ] every check in section 2 shows PASS
- [ ] the rerun test in section 3 shows PASS
- [ ] the decisions in section 4 match what I actually did
- [ ] this log, the SQL files and the data model are committed to Git

Date completed:
