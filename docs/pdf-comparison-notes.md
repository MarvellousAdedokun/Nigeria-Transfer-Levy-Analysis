# PDF Headline Cross-Check Notes

## Method

For the PDFs inside the uploaded ZIP archives, I extracted the EMTL headline from page 4 (`KEY HIGHLIGHTS`) and compared it with the exact EMTL `TOTAL` cell from Table I in the corresponding Excel workbook. The headline is shown in billions to two decimal places, so the comparison uses conventional rounding to two decimal places in billions.

The four 2024 PDFs were not included in the current upload. Their headline values in `pdf_headline_check.csv` were carried forward from the existing source-audit notes and are marked as such; the Excel totals were checked directly.

## Results

- 17 headline values recorded.
- 15 match the Excel total at conventional two-decimal-billion rounding.
- Two require manual review.

### July 2025

- PDF page 4 headline: **₦30.37 billion**.
- Excel Table I EMTL total: **₦30,379,578,750.00**, which conventionally rounds to **₦30.38 billion**.
- Status: **Review required.** The PDF headline may have been truncated or may contain a small inconsistency. Do not silently change either source value.

### August 2025

- PDF page 4 headline: **₦39.16 billion**.
- Excel Table I EMTL total: **₦39,168,321,000.00**, which conventionally rounds to **₦39.17 billion**.
- Status: **Review required.** The PDF headline may have been truncated or may contain a small inconsistency. Do not silently change either source value.

## Period wording errors in PDF Key Highlights

- **March 2025 report:** page 4 says the allocation was for December 2024, but the report filename and Table I title indicate March 2025 sharing of February 2025 revenue.
- **April 2025 report:** page 4's allocation paragraph refers to December 2024, while the report filename and Table I title indicate April 2025 sharing of March 2025 revenue.
- **May 2025 report:** page 4's allocation paragraph refers to January 2025, while the report filename and Table I title indicate May 2025 sharing of April 2025 revenue.

For the comparison, the allocation month is taken from the report filename/Table I title, not from the inconsistent paragraph. The original wording is not edited in the source files.

## February 2026

Page 4 does not list EMTL among the revenue items in the Key Highlights, and the Table I heading row in Excel has no EMTL column. This is recorded as **not listed in the report**, not as zero EMTL collected.
