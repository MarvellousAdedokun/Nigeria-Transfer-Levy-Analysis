from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUT_DIR = PROJECT_ROOT / "reports" / "figures"

annual_file = DATA_DIR / "annual_emtl_revenue_generated_total.csv"
monthly_file = DATA_DIR / "monthly_emtl_trend.csv"
if not monthly_file.exists():
    monthly_file = DATA_DIR / "montly_emtl_trend.csv"

if not annual_file.exists():
    raise FileNotFoundError(f"Could not find {annual_file}")
if not monthly_file.exists():
    raise FileNotFoundError("Monthly trend CSV is needed to show month coverage.")

annual = pd.read_csv(annual_file)
monthly = pd.read_csv(monthly_file)

required_annual = ["revenue_year", "total_reported_emtl_ngn"]
required_monthly = ["revenue_month", "reported_emtl_total_ngn"]

for col in required_annual:
    if col not in annual.columns:
        raise ValueError(f"Annual CSV is missing column: {col}")
for col in required_monthly:
    if col not in monthly.columns:
        raise ValueError(f"Monthly CSV is missing column: {col}")

annual["revenue_year"] = pd.to_numeric(annual["revenue_year"], errors="coerce")
annual["total_reported_emtl_ngn"] = pd.to_numeric(
    annual["total_reported_emtl_ngn"], errors="coerce"
)
monthly["revenue_month"] = pd.to_datetime(
    monthly["revenue_month"], errors="coerce"
)
monthly["reported_emtl_total_ngn"] = pd.to_numeric(
    monthly["reported_emtl_total_ngn"], errors="coerce"
)

if annual["revenue_year"].isna().any() or monthly["revenue_month"].isna().any():
    raise ValueError("A year or month value could not be read.")

annual["revenue_year"] = annual["revenue_year"].astype(int)
# Standardise each date to the first day of its month.
monthly["revenue_month"] = (
    monthly["revenue_month"].dt.to_period("M").dt.to_timestamp()
)

if monthly["revenue_month"].duplicated().any():
    raise ValueError("Duplicate revenue months found in the monthly CSV.")

# Build the full month range. This counts months even when a whole row
# is missing from the CSV.
monthly = monthly.set_index("revenue_month").sort_index()
all_months = pd.date_range(monthly.index.min(), monthly.index.max(), freq="MS")
monthly = monthly.reindex(all_months)
monthly.index.name = "revenue_month"
monthly["revenue_year"] = monthly.index.year

# Count all months in the covered date range and months with reported amounts.
coverage = (
    monthly.groupby("revenue_year")
    .agg(
        months_in_data=("reported_emtl_total_ngn", "size"),
        months_reported=("reported_emtl_total_ngn", lambda x: x.notna().sum())
    )
    .reset_index()
)

chart_data = annual.merge(coverage, on="revenue_year", how="left")
chart_data = chart_data.sort_values("revenue_year")
chart_data["total_emtl_bn"] = (
    chart_data["total_reported_emtl_ngn"] / 1_000_000_000
)

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(
    chart_data["revenue_year"].astype(str),
    chart_data["total_emtl_bn"]
)

ax.set_title("Annual Reported EMTL Total", pad=14)
ax.set_xlabel("Revenue year")
ax.set_ylabel("Reported EMTL total (₦ billion)")
ax.grid(axis="y", linestyle="--", alpha=0.4)

# Show the amount above each bar.
for bar, amount in zip(bars, chart_data["total_emtl_bn"]):
    ax.annotate(
        f"₦{amount:,.2f}bn",
        (bar.get_x() + bar.get_width() / 2, bar.get_height()),
        xytext=(0, 5), textcoords="offset points",
        ha="center", fontsize=9
    )

# Show reported months / months covered under each year.
labels = []
for _, row in chart_data.iterrows():
    covered = int(row["months_in_data"]) if pd.notna(row["months_in_data"]) else 0
    reported = int(row["months_reported"]) if pd.notna(row["months_reported"]) else 0
    labels.append(f"{int(row['revenue_year'])}\n{reported}/{covered} months reported")

ax.set_xticks(range(len(labels)))
ax.set_xticklabels(labels)

fig.text(
    0.08, 0.02,
    "Totals are sums of reported figures. Month coverage comes from the "
    "monthly dataset; a year is not automatically a complete 12-month year.",
    ha="left", fontsize=8.5
)
fig.tight_layout(rect=[0, 0.09, 1, 1])

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
output_file = OUTPUT_DIR / "annual_emtl_totals.png"
fig.savefig(output_file, dpi=300, bbox_inches="tight")

print(f"Chart saved to: {output_file}")
print(chart_data[
    ["revenue_year", "total_reported_emtl_ngn", "months_reported", "months_in_data"]
].to_string(index=False))
plt.show()
