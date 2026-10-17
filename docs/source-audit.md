# Nigeria EMTL Project — Source Audit

## 1. What are we trying to find out?

Our starting question is:

What do official Nigerian reports tell us about EMTL amounts over time, and how is the money shared if the reports provide that information?

We are checking whether the available reports can answer this question reliably.

## 2. Where did I search?

- Official catalogue: NGA-NBS-FAAC
- Related materials page: https://microdata.nigerianstat.gov.ng/index.php/catalog/156/related-materials
- Date I searched: [15/10/2026]. Months found in 2024: August, September, November, December. There was no file for October.
- Search notes: Other months were also completed in the catalogue, including complete 2025 data. I have not audited the 2025 files yet.

## 3. Source register

| Source ID | Exact document title | Publisher | Period shown | File type | URL | Download date | Local path | EMTL present? | Notes |
|---|---|---|---|---|---|---|---|---|---|
| P-AUG | [AUGUST 2024 FAAC Disbursment Report] | National Bureau of Statistics (data from the Office of the Accountant General of the Federation) | Gotten July 2024, shared August 2024 | PDF | [https://microdata.nigerianstat.gov.ng/index.php/catalog/156/download/1124] | [15/10/26] | [C:\Users\HP\Documents\GitHub\Nigeria Transfer Levy Analysis\data\raw\FAAC_August_2024.pdf] | Yes | |
| P-SEP | [September 2024 FAAC Disbursement Report] | NBS (data from OAGF) | Gotten August 2024, shared September 2024 | PDF | [https://microdata.nigerianstat.gov.ng/index.php/catalog/156/download/1152] | [date] | [path] | Yes | |
| P-NOV | [November 2024 FAAC Disbursement Report] | NBS (data from OAGF) | Gotten October 2024, shared November 2024 | PDF | [https://microdata.nigerianstat.gov.ng/index.php/catalog/156/download/1207] | [date] | [path] | Yes | |
| P-DEC | December 2024 FAAC Disbursement Report | NBS (data from OAGF) | Gotten November 2024, shared December 2024 | PDF | [https://microdata.nigerianstat.gov.ng/index.php/catalog/156/download/1206] | [date] | [path] | Yes | Report date on cover: February 2025 |
| X-AUG | FAAC_Disbursement_August_2024.xlsx | NBS (OAGF Federation Account Department tables) | Same as P-AUG | Excel | [https://microdata.nigerianstat.gov.ng/index.php/catalog/156/download/1125] | [date] | [path] | Yes | |
| X-SEP | Disbursement_September_2024.xlsx | Same | Same as P-SEP | Excel | [https://microdata.nigerianstat.gov.ng/index.php/catalog/156/download/1153] | [date] | [path] | Yes | |
| X-NOV | Disbursement_November_2024.xlsx | Same | Same as P-NOV | Excel | [https://microdata.nigerianstat.gov.ng/index.php/catalog/156/download/1204] | [date] | [path] | Yes | |
| X-DEC | Disbursement_December_2024.xlsx | Same | Same as P-DEC | Excel | [https://microdata.nigerianstat.gov.ng/index.php/catalog/156/download/1205] | [date] | [path] | Yes | |

The file name shows the month the money was SHARED. The data is for the month before. I take the period from the table titles and the Key Highlights page.

## 4. What does each report measure?

Same for all four months (P-AUG, P-SEP, P-NOV, P-DEC and their Excel files):

- Exact EMTL row label: the column "Electronic Money Transfer Levy (EMTL)" in Table I.
- Table heading: "Summary of Gross Revenue Allocation by Federation Account Allocation Committee for the Month of [month], 2024 Shared in [month], 2024".
- Currency and unit: naira (₦), full amounts to 2 decimals, not billions.
- Page or worksheet: PDF page 17 (Table I), page 18 (Table II, FGN), page 19 (Table III, states). Excel: sheet "Sum & FG" (Tables I and II), "State Details" (Table III), LGC sheet (Table IV, Excel only).
- Does it report collections, allocations, disbursements, or something else? Allocations/disbursements shared by FAAC. It is not a count of transfers and it is not shown per company.
- Footnote seen: the "Others*" figure on the summary page is the Exchange Gain and EMTL together.

| Source | Amount exactly as printed (EMTL total, Table I) | Revenue period | Allocation/disbursement period |
|---|---|---|---|
| P-AUG | 19,602,075,826.00 | July 2024 | August 2024 |
| P-SEP | 15,642,981,643.52 | August 2024 | September 2024 |
| P-NOV | 17,823,739,533.00 | October 2024 | November 2024 |
| P-DEC | 15,673,196,093.19 | November 2024 | December 2024 |

- Publication date, if known: only December is known (February 2025). [add the others if shown]
- What remains unclear: the methodology page is one sentence, so the reports do not explain how EMTL is defined or whether the EMTL figure is everything collected or only part of it. I do not know what the "SOKU" row in the August and September state tables is.

## 5. PDF and Excel comparison

Excel values were compared to 2 decimals (some Excel cells hold extra decimals).

| Source/report | Figure checked | PDF value | Excel value | Match? | Explanation/status |
|---|---|---|---|---|---|
| Aug | EMTL total | 19,602,075,826.00 | 19,602,075,826.00 | Yes | |
| Aug | FGN | 2,822,698,918.94 | 2,822,698,918.94 | Yes | |
| Aug | States | 9,408,996,396.48 | 9,408,996,396.48 | Yes | |
| Aug | LGCs | 6,586,297,477.54 | 6,586,297,477.54 | Yes | |
| Aug | FIRS cost of collection | 784,083,033.04 | 784,083,033.04 | Yes | |
| Sep | EMTL total | 15,642,981,643.52 | 15,642,981,643.52 | Yes | |
| Sep | FGN | 2,252,589,356.67 | 2,252,589,356.67 | Yes | |
| Sep | States | 7,508,631,188.89 | 7,508,631,188.89 | Yes | |
| Sep | LGCs | 5,256,041,832.22 | 5,256,041,832.22 | Yes | |
| Sep | FIRS cost of collection | 625,719,265.74 | 625,719,265.74 | Yes | |
| Nov | EMTL total | 17,823,739,533.00 | 17,823,739,533.00 | Yes | |
| Nov | FGN | 2,566,618,492.75 | 2,566,618,492.75 | Yes | |
| Nov | States | 8,555,394,975.84 | 8,555,394,975.84 | Yes | |
| Nov | LGCs | 5,988,776,483.09 | 5,988,776,483.09 | Yes | |
| Nov | FIRS cost of collection | 712,949,581.32 | 712,949,581.32 | Yes | |
| Dec | EMTL total | 15,673,196,093.19 | 15,673,196,093.19 | Yes | |
| Dec | FGN | 2,256,940,237.42 | 2,256,940,237.42 | Yes | Table II total is 2,256,940,237.41, 1 kobo different (rounding) |
| Dec | States | 7,523,134,124.73 | 7,523,134,124.73 | Yes | |
| Dec | LGCs | 5,266,193,887.31 | 5,266,193,887.31 | Yes | |
| Dec | FIRS cost of collection | 626,927,843.73 | 626,927,843.73 | Yes | |
| All 4 months | EMTL for each state (Table III, 36 states) | PDF page 19 | State Details sheet | Yes | August and September also have a row called SOKU with 0 EMTL (a dash in the PDF) |
| All 4 months | LGC grand total | n/a (the PDFs do not have the LGC table) | LGC sheet grand total | Yes | I checked it against the LGCs line in Table I. Only the Excel has LGC-level data |

## 6. Coverage and consistency

- Which periods/files did I find? 2024 files shared in August, September, November and December (revenue months July, August, October, November 2024). Complete 2025 data also exists in the catalogue but is not audited yet.
- Which periods/files could I not find? The file shared in October 2024 (revenue month September 2024).
- Do the figures refer to comparable periods? Yes, each is one revenue month, but the 4 months are not consecutive.
- Are the units consistent? Yes, naira in full amounts in all four files.
- Do the row labels and definitions stay consistent? The EMTL label stays the same. The columns around it change: August has a Solid Mineral column, and November has a new column of 100,000,000,000.00 about non-oil revenue. The EMTL column is not in the same place in every Excel file. Sheet names also change (LGC Details, LG Details, LGCs Details; and SumSum, Sumlgcs, Sum, Summary).
- What geographic or recipient breakdowns are available? FGN (only FGN CRF Account and FCT-Abuja received EMTL), 36 states, LGCs (Excel only), and the FIRS cost of collection.
- Are any totals or figures difficult to reconcile? The EMTL lines reconcile. Not EMTL: in November, FGN VAT is 93,346,882,558.89 in Table I and 93,676,882,558.89 in Table II (a 330,000,000 difference), and it is the same in the PDF.
- What changes or gaps did I notice? The MONTHENTRY sheet is full of #REF! and shows the wrong date in all four files (9/2024, 1/2025, 5/2025, 1/2025). The September Excel skips S/n 9 in Table I and a column number in Table II. Every month FIRS takes 4 out of every 100 of the EMTL, and the rest is split 15 to FGN, 50 to States and 35 to LGCs. I still need to confirm the law behind this before calling it a rule.

## 7. Can the data answer our questions?

| Question | Answerable / partly answerable / not answerable | Evidence or reason |
|---|---|---|
| How do reported EMTL amounts change over time? | Partly answerable | I have 4 non-consecutive months in 2024 (19.60, 15.64, 17.82 and 15.67 billion naira). The 2025 files can extend this once audited. |
| How is the money shared, if the source provides that detail? | Answerable for these months | Table I, Table II, Table III and the LGC sheet show FGN, States, LGCs and the FIRS cost of collection. The legal basis is not confirmed. |
| Can we tell how many transfers Nigerians made? | Not answerable | The reports show amounts shared, not transfers. Dividing by 50 is only an estimate because exemptions are unknown. |
| Can we tell how much a specific fintech collected? | Not answerable | There is no company breakdown in these reports. |
| Can we explain why the reported amounts changed? | Not answerable from these sources | The reports contain no explanations. |

## 8. Main problems and limitations

- The file for September 2024 revenue (shared in October) is missing, so the 2024 months do not follow each other.
- The file name is the sharing month, not the revenue month.
- The columns, sheet names and the EMTL column position change between files, so loading must use heading names.
- The MONTHENTRY sheet is broken and cannot be used for dates.
- The PDFs have no LGC table, so LGC-level data comes from the Excel only.
- The methodology page does not define EMTL, and I do not know what the SOKU row is.
- The reports show what FAAC shared, not what was collected by any company or how many transfers were charged.
- The 2025 files have not been audited.

## 9. Source feasibility decision

GO WITH REVISED SCOPE

My decision: GO WITH REVISED SCOPE

Evidence for my decision:
- The EMTL line is present in all 4 files and the PDF and Excel agree for every figure I checked.
- The reports can show how EMTL amounts changed and who received them. They cannot show transfers, company collections or reasons.
- One month (September 2024 revenue) is missing.

Questions still unresolved:
- What is the SOKU row?
- What is the legal basis for the 4, 15, 50 and 35 split?
- Do the 2025 files follow the same structure?

## 10. Next action

Based on what I found, the next thing to do is audit the 2025 files with the same checks (period, EMTL line, column positions, PDF against Excel). After that, I design the first warehouse table: decide what one row means, then build the raw table and the clean table.