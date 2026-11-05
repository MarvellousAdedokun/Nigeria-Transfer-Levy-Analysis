import pandas as pd
import matplotlib.pyplot as plt
import os
os.getcwd()

df = pd.read_csv(r"C:\Users\HP\Documents\GitHub\Nigeria Transfer Levy Analysis\data\processed\annual_emtl_revenue_generated_total.csv")

df["revenue_year"] = df["revenue_year"].astype(int)
df["total_reported_emtl_ngn"] = df["total_reported_emtl_ngn"]/1e9

plt.figure(figsize=(12, 6))
plt.bar(df['revenue_year'], df['total_reported_emtl_ngn'], color="#ffd901")

plt.tight_layout()

output_dir = r"C:\Users\HP\Documents\GitHub\Nigeria Transfer Levy Analysis\reports\figures"
os.makedirs(output_dir, exist_ok=True)

plt.savefig(os.path.join(output_dir, "annual_emtl_totals.png"), bbox_inches='tight', dpi=300)
plt.show()