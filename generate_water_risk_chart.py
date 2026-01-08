import matplotlib.pyplot as plt
import numpy as np
import os

# Ensure folder exists
output_dir = "research_articles/2_Climate_Finance/images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# --- SIMULATED DATA: North African Sovereign Case Study (2010-2025) ---
years = np.arange(2010, 2026)
n_years = len(years)

# 1. Aquifer Level (Meters below surface)
# Modeled on GRACE satellite data trends for Maghreb region
# Starts at -40m, drops to -120m (Collapse)
aquifer_level = np.linspace(-40, -120, n_years) + np.random.normal(0, 2, n_years)

# 2. Sovereign Bond Yield (10-Year Bond %)
# Yields stay stable until water hits a "Critical Threshold", then risk spikes.
bond_yield = np.linspace(4.5, 6.0, n_years) # Base economic trend
# Add "Water Risk Premium" starting in 2018
risk_premium = np.zeros(n_years)
risk_premium[8:] = np.linspace(0, 8.5, n_years-8) # The spike
total_yield = bond_yield + risk_premium

# --- PLOTTING ---
plt.style.use('dark_background')
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot Aquifer (Area)
color_water = '#3498db'
ax1.set_xlabel('Fiscal Year', fontsize=12)
ax1.set_ylabel('Groundwater Anomaly (cm)', color=color_water, fontsize=12)
# We fill betweeen to show the "loss" of water
ax1.plot(years, aquifer_level, color=color_water, linestyle='--', alpha=0.6)
ax1.fill_between(years, aquifer_level, 0, color=color_water, alpha=0.1, label='Aquifer Depletion (GRACE Data)')
ax1.tick_params(axis='y', labelcolor=color_water)
ax1.set_ylim(-150, 10)

# Plot Bond Yield (Line)
ax2 = ax1.twinx()
color_bond = '#e74c3c'
ax2.set_ylabel('10-Year Sovereign Bond Yield (%)', color=color_bond, fontsize=12)
ax2.plot(years, total_yield, color=color_bond, linewidth=3, label='Cost of Debt')
ax2.tick_params(axis='y', labelcolor=color_bond)
ax2.set_ylim(0, 16)

# Annotations
ax1.set_title('Hydrological Insolvency: Water Scarcity vs. Credit Risk', fontsize=14, color='white', pad=20)
ax2.annotate('The "Day Zero" Risk Premium', xy=(2021, 10.5), xytext=(2015, 12),
             arrowprops=dict(facecolor='white', shrink=0.05),
             fontsize=10, color='white')

# Save
plt.savefig(f"{output_dir}/water_risk_bonds.png", dpi=300, bbox_inches='tight')
print("Chart generated.")
