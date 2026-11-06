from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUT_DIR = PROJECT_ROOT / "reports" / "figures"

csv_file = DATA_DIR / "monthly_emtl_trend.csv"

df = pd.read_csv(csv_file)

required = ["revenue_month", "reported_emtl_total_ngn"]
missing = [col for col in required if col not in df.columns]
if missing:
    raise ValueError(f"CSV is missing columns: {missing}")

df["revenue_month"] = pd.to_datetime(df["revenue_month"], errors="coerce")
df["reported_emtl_total_ngn"] = pd.to_numeric(
    df["reported_emtl_total_ngn"], errors="coerce"
)

if df["revenue_month"].isna().any():
    raise ValueError("Some revenue_month values are not valid dates.")

# Make every date the first day of its month.
df["revenue_month"] = df["revenue_month"].dt.to_period("M").dt.to_timestamp()

# One row per revenue month is expected.
if df["revenue_month"].duplicated().any():
    raise ValueError("Duplicate revenue months found. Check the SQL export.")

df = df.set_index("revenue_month").sort_index()

# Add any missing months between the first and last dates.
# Missing values stay NaN; they are NOT changed to zero.
all_months = pd.date_range(df.index.min(), df.index.max(), freq="MS")
df = df.reindex(all_months)
df.index.name = "revenue_month"
df["emtl_total_bn"] = df["reported_emtl_total_ngn"] / 1_000_000_000

missing_months = df.index[df["reported_emtl_total_ngn"].isna()]

fig, ax = plt.subplots(figsize=(13, 6))
ax.plot(
    df.index,
    df["emtl_total_bn"],
    marker="o",
    linewidth=2,
    label="Reported EMTL total"
)

# Shade months with no reported amount so the gaps are easy to see.
for i, month in enumerate(missing_months):
    ax.axvspan(
        month - pd.Timedelta(days=14),
        month + pd.Timedelta(days=14),
        alpha=0.18,
        label="No EMTL figure reported" if i == 0 else None
    )

ax.set_title("Monthly Reported EMTL Total", pad=14)
ax.set_xlabel("Revenue month")
ax.set_ylabel("Reported EMTL total (₦ billion)")
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
ax.grid(axis="y", linestyle="--", alpha=0.4)
ax.legend()

fig.text(
    0.08, 0.02,
    "Shaded months have no reported EMTL amount. They are missing/not "
    "reported, not zero.",
    ha="left", fontsize=9
)
fig.autofmt_xdate()
fig.tight_layout(rect=[0, 0.07, 1, 1])

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
output_file = OUTPUT_DIR / "monthly_emtl_trend.png"
fig.savefig(output_file, dpi=300, bbox_inches="tight")

print(f"Chart saved to: {output_file}")
print(f"Months shown: {len(df)}")
print(f"Months with reported amounts: {df['reported_emtl_total_ngn'].notna().sum()}")
print(f"Months without reported amounts: {len(missing_months)}")
plt.show()
