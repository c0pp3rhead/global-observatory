import matplotlib.pyplot as plt
import numpy as np
import os

# Ensure folder exists
output_dir = "research_articles/3_Biosecurity_Illicit_Economies/images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# --- SIMULATED DATA: Tractor Exports (HS Code 8701) ---
# N = 200 shipments
n_shipments = 200
shipment_ids = np.arange(n_shipments)

# 1. Normal Trade (The Cluster)
# Average tractor price $50k +/- $10k
normal_prices = np.random.normal(50000, 5000, 180)

# 2. TBML Anomalies (The Outliers)
# Over-invoicing (Moving money OUT of the destination)
over_invoiced = np.random.normal(150000, 20000, 10) 
# Under-invoicing (Moving value INTO the destination to avoid taxes/tariffs)
under_invoiced = np.random.normal(5000, 1000, 10)

# Combine
all_prices = np.concatenate([normal_prices, over_invoiced, under_invoiced])
np.random.shuffle(all_prices) # Mix them up

# --- PLOTTING ---
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 6))

# Plot "Normal" Zone
ax.axhspan(40000, 60000, color='#2ecc71', alpha=0.1, label='Fair Market Value (Range)')

# Plot Shipments
colors = ['#e74c3c' if (p > 80000 or p < 20000) else '#3498db' for p in all_prices]
ax.scatter(shipment_ids, all_prices, c=colors, alpha=0.7, s=50, edgecolor='white', linewidth=0.5)

# Formatting
ax.set_title('Trade-Based Money Laundering: Unit Price Anomalies (HS Code 8701)', fontsize=14, color='white', pad=20)
ax.set_ylabel('Declared Unit Price (USD)', fontsize=12)
ax.set_xlabel('Shipment Transaction ID', fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.2)

# Annotations
ax.annotate('Over-Invoicing\n(Capital Flight/Laundering)', xy=(180, 150000), xytext=(120, 120000),
            arrowprops=dict(facecolor='white', shrink=0.05),
            fontsize=9, color='#e74c3c')

ax.annotate('Under-Invoicing\n(Tax Evasion/Value Transfer)', xy=(180, 5000), xytext=(120, 25000),
            arrowprops=dict(facecolor='white', shrink=0.05),
            fontsize=9, color='#e74c3c')

# Save
plt.savefig(f"{output_dir}/tbml_scatter_analysis.png", dpi=300, bbox_inches='tight')
print("Chart generated.")
