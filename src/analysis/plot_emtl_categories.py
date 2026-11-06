from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUT_DIR = PROJECT_ROOT / "reports" / "figures"

csv_file = DATA_DIR / "emtl_by_category.csv"
if not csv_file.exists():
    raise FileNotFoundError(f"Could not find {csv_file}")

df = pd.read_csv(csv_file)

required = ["recipient_category", "sum_of_recorded_amounts_ngn"]
missing = [col for col in required if col not in df.columns]
if missing:
    raise ValueError(f"Category CSV is missing columns: {missing}")

df["sum_of_recorded_amounts_ngn"] = pd.to_numeric(
    df["sum_of_recorded_amounts_ngn"], errors="coerce"
)
if df["recipient_category"].isna().any():
    raise ValueError("Some recipient_category values are blank.")
"""if df["sum_of_recorded_amounts_ngn"].isna().any():
    raise ValueError("Some category amounts are blank or not numeric.")"""

df["amount_bn"] = df["sum_of_recorded_amounts_ngn"] / 1_000_000_000
df = df.sort_values("amount_bn", ascending=True)

# Give long category lists enough vertical space.
chart_height = max(6, len(df) * 0.4)
fig, ax = plt.subplots(figsize=(12, chart_height))

bars = ax.barh(df["recipient_category"], df["amount_bn"])

ax.set_title("Recorded EMTL Amount by Recipient Category", pad=14)
ax.set_xlabel("Sum of recorded amounts (₦ billion)")
ax.set_ylabel("Recipient category")
ax.grid(axis="x", linestyle="--", alpha=0.4)

# Put the amount beside each bar.
for bar, amount in zip(bars, df["amount_bn"]):
    ax.annotate(
        f"{amount:,.2f}",
        (bar.get_width(), bar.get_y() + bar.get_height() / 2),
        xytext=(5, 0), textcoords="offset points",
        va="center", fontsize=8
    )

fig.text(
    0.08, 0.01,
    "Amounts are summed across the periods in the SQL query. Category "
    "names depend on the recipient mapping; proposed mappings need review.",
    ha="left", fontsize=8.5
)
fig.tight_layout(rect=[0, 0.04, 1, 1])

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
output_file = OUTPUT_DIR / "emtl_by_category.png"
fig.savefig(output_file, dpi=300, bbox_inches="tight")

print(f"Chart saved to: {output_file}")
print(f"Number of categories shown: {len(df)}")
plt.show()
