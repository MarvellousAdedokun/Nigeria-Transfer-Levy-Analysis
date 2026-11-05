import pandas as pd
import matplotlib.pyplot as plt
import os
os.getcwd()

df = pd.read_csv(r"data\processed\emtl_by_category.csv")
df = df.sort_values(by = "sum_of_recorded_amounts_ngn", ascending = 0)

plt.figure(figsize=(12, 6))
plt.barh(df['recipient_category'], df['sum_of_recorded_amounts_ngn']/1e9, color="#0105ff")

plt.tight_layout()

output_dir = r"C:\Users\HP\Documents\GitHub\Nigeria Transfer Levy Analysis\reports\figures"
os.makedirs(output_dir, exist_ok=True)

plt.savefig(os.path.join(output_dir, "emtl_by_category.png"), bbox_inches='tight', dpi=300)
plt.show()