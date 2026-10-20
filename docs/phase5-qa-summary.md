# Phase 5 — QA Summary

## What was processed

- Excel workbooks processed: 18.
- EMTL heading found in Table I: 17.
- EMTL heading not found in Table I: 1.
- Staging rows: 276.
- Source register entries: 38 (original uploaded files and ZIP members).
- Detail-cell sums matching their EMTL TOTAL to two decimal places: 17 of 17.
- PDF headline entries: 17.
- PDF headline comparisons matching conventional two-decimal-billion rounding: 15 of 17.

## Important limits

1. The project expects 23 Excel workbooks: four 2024 reports, twelve 2025 reports, and January–July 2026. Only 18 workbooks were available in the files uploaded for this run. The March–July 2026 workbooks were not present, so they have not been extracted or marked missing by this run.
2. The February 2026 workbook is present. Its Table I has no EMTL heading; the staging record uses `status=column_not_found`, `emtl_found=False`, and a blank EMTL value. This is not treated as zero.
3. The four 2024 PDF binaries were not included in the current uploads. Their page-4 headline values were carried forward from the existing source-audit notes; the corresponding Excel totals were checked directly.
4. The July 2025 and August 2025 PDF headlines need manual review against the Excel totals. Their headlines are ₦30.37bn and ₦39.16bn, while the exact Excel totals conventionally round to ₦30.38bn and ₦39.17bn.
5. The March, April and May 2025 PDF Key Highlights contain period wording that conflicts with the Table I title/report month. The allocation month in the comparison uses the report filename/Table I title; the inconsistency is documented in `pdf-comparison-notes.md`.

## Files produced

- `source_register.csv`: file inventory and checksums.
- `staging_table1.csv`: row-level EMTL extraction with exact source-cell addresses.
- `pdf_headline_check.csv`: 17 headline figures for independent checking.
- `pdf_excel_comparison.csv`: comparison of headline figures with Excel Table I totals.
- `extraction-log.md`: per-workbook extraction results, source cells, sum checks and warnings.
- `structure-audit.md`: observed workbook layout.
- `staging-design.md`: staging fields and rules.
- `extract_table1.py`: reusable extractor script.
