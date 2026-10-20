# Phase 5 — Table I Structure Audit

## Scope

I inspected the `Sum & FG` sheet in all 18 Excel workbooks available in this run: four 2024 reports, twelve 2025 reports, and January–February 2026. The March–July 2026 workbooks were not included in the files available for this run.

## Common structure observed

- **Sheet:** `Sum & FG`
- **Table:** `Table I`
- **Title cell:** `A4`
- **Title text:** begins `Summary of Gross Revenue Allocation by Federation Account Allocation Committee...`
- **Table I heading row:** row 5 in some files and row 6 in others.
- **EMTL heading text:** `Electronic Money Transfer Levy (EMTL)` in the files where the column is present. The column letter changes.
- **TOTAL label:** column B, with the text `TOTAL`.
- **EMTL total:** the cell in the EMTL column on the same row as the `TOTAL` label.
- **Overall total:** a different cell in the `Total` column on that same row. Do not confuse this with the EMTL total.
- **Currency row:** a row of `₦` labels may appear directly below the heading row. It is not a data row.
- **Other tables:** later rows in `Sum & FG` can contain another EMTL heading. The extractor must stay within Table I and stop at its TOTAL row.

## Workbook-specific layout observed

| Revenue period | Allocation month | Sheet | Title cell | Heading row | EMTL heading cell | TOTAL label cell | EMTL total cell | EMTL present? |
|---|---|---|---|---:|---|---|---|---|
| July 2024 | August 2024 | Sum & FG | A4 | 5 | F5 | B23 | F23 | Yes |
| August 2024 | September 2024 | Sum & FG | A4 | 5 | E5 | B22 | E22 | Yes |
| October 2024 | November 2024 | Sum & FG | A4 | 5 | E5 | B22 | E22 | Yes |
| November 2024 | December 2024 | Sum & FG | A4 | 5 | E5 | B22 | E22 | Yes |
| December 2024 | January 2025 | Sum & FG | A4 | 5 | E5 | B22 | E22 | Yes |
| January 2025 | February 2025 | Sum & FG | A4 | 5 | E5 | B23 | E23 | Yes |
| February 2025 | March 2025 | Sum & FG | A4 | 5 | F5 | B22 | F22 | Yes |
| March 2025 | April 2025 | Sum & FG | A4 | 5 | E5 | B22 | E22 | Yes |
| April 2025 | May 2025 | Sum & FG | A4 | 5 | E5 | B22 | E22 | Yes |
| May 2025 | June 2025 | Sum & FG | A4 | 5 | E5 | B23 | E23 | Yes |
| June 2025 | July 2025 | Sum & FG | A4 | 6 | E6 | B25 | E25 | Yes |
| July 2025 | August 2025 | Sum & FG | A4 | 6 | E6 | B25 | E25 | Yes |
| August 2025 | September 2025 | Sum & FG | A4 | 6 | E6 | B26 | E26 | Yes |
| September 2025 | October 2025 | Sum & FG | A4 | 6 | D6 | B21 | D21 | Yes |
| October 2025 | November 2025 | Sum & FG | A4 | 6 | D6 | B22 | D22 | Yes |
| November 2025 | December 2025 | Sum & FG | A4 | 6 | D6 | B21 | D21 | Yes |
| December 2025 | January 2026 | Sum & FG | A4 | 6 | D6 | B21 | D21 | Yes |
| January 2026 | February 2026 | Sum & FG | A4 | 5 | Not found | B19 | Not applicable | No |

**Period note:** The month in the workbook filename is the allocation/sharing month. The title in `A4` supplies the revenue period and, when stated, the allocation period. For some 2025/2026 files, the sharing month is not repeated in the title, so the filename is used as a documented fallback. The `MONTHENTRY` sheet has `#REF!` errors and is not used to determine periods.

## Implications for the extractor

1. Do not hard-code the EMTL column letter.
2. Do not hard-code the heading row.
3. Find the heading row by identifying `Beneficiaries` and `Total` in the Table I header.
4. Search for the EMTL label only within that header row.
5. Find the exact `TOTAL` label in column B before the next table begins.
6. Save both the EMTL total cell and the overall Table I total cell as separate fields.
7. If the EMTL heading is absent, write an explicit missing-column record. Do not fill in zero.
