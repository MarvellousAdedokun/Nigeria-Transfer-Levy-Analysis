import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
os.getcwd()

pd.set_option('display.float_format', lambda x: '%.2f' % x)


df = pd.read_csv(r"C:\Users\HP\Documents\GitHub\Nigeria Transfer Levy Analysis\data\processed\montly_emtl_trend.csv")


# 2. Convert to datetime and sort sequentially (Step 6 & 7)
df["revenue_month"] = pd.to_datetime(df["revenue_month"])
df = df.sort_values(by="revenue_month")

# 3. Create the clean plot layout (Step 8 & 9)
plt.figure(figsize=(12, 6))

# Strictly uses 'reported_emtl_total_ngn' on Y-axis but scales by 1e9 inline for simplicity
# Gaps are preserved naturally because pandas loads SQL NULLs as NaN values
plt.plot(df['revenue_month'], df['reported_emtl_total_ngn'] / 1e9, marker='o', color='#1f77b4', linewidth=2)

# 4. Format X-Axis Dates dynamically to 'Jan 2026' style
ax = plt.gca()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))  # Abbreviated month + Year
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))  # Shows every 2nd month to prevent crowding

# 5. Polish design aesthetics, labels, and axis margins (Step 10)
plt.title('Monthly Reported EMTL Revenue Trend', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Revenue Month', fontsize=11, labelpad=10)
plt.ylabel('Total Revenue (In Billions ₦)', fontsize=11, labelpad=10)
plt.grid(True, linestyle='--', alpha=0.5)
plt.ylim(0, (df['reported_emtl_total_ngn'].max() / 1e9) * 1.1)

# Clean, automated date layout tilting handling
plt.gcf().autofmt_xdate()

# 6. Required explicit analytical note (Step 10)
plt.figtext(
    0.12, 0.01, 
    "Note: Gaps in the trend line indicate missing periods where the EMTL heading was not found in Table I.", 
    horizontalalignment='left', fontsize=9.5, style='italic', color='#d9534f'
)

# Adjust layout margins explicitly so the bottom figtext note fits nicely
plt.tight_layout()
plt.subplots_adjust(bottom=0.15) 

# 7. Save final file asset cleanly to target tree (Step 11)
output_dir = r"C:\Users\HP\Documents\GitHub\Nigeria Transfer Levy Analysis\reports\figures"
os.makedirs(output_dir, exist_ok=True)

plt.savefig(os.path.join(output_dir, "monthly_emtl_trend.png"), bbox_inches='tight', dpi=300)
plt.show()
