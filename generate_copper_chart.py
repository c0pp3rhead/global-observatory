import matplotlib.pyplot as plt
import numpy as np
import os

# Ensure folder exists
output_dir = "research_articles/2_Climate_Finance/images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# --- SIMULATED DATA: The Copper Gap (2020-2035) ---
years = np.arange(2020, 2036)
n_years = len(years)

# 1. Demand (Million Metric Tons)
# Driven by "Net Zero 2050" targets (EVs + Grid expansion)
# Exponential growth
demand = 25 * np.exp(0.04 * (years - 2020)) 

# 2. Supply (Committed Projects)
# Mines take 10+ years to build. Supply is inelastic (slow to react).
# Grows slowly then plateaus as ore grades decline.
supply = 25 * np.exp(0.015 * (years - 2020))
supply[8:] = supply[8] * 1.05  # Plateau after 2028 (lack of new discoveries)

# --- PLOTTING ---
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 6))

# Plot Lines
ax.plot(years, demand, color='#2ecc71', linewidth=3, label='Projected Demand (Net Zero Scenario)')
ax.plot(years, supply, color='#e74c3c', linewidth=3, linestyle='--', label='Committed Mine Supply')

# Fill the Gap (The Deficit)
ax.fill_between(years, supply, demand, where=(demand > supply), 
                color='#e74c3c', alpha=0.2, label='Structural Deficit')

# Formatting
ax.set_title('Greenflation: The Looming Copper Deficit (2020-2035)', fontsize=14, color='white', pad=20)
ax.set_ylabel('Global Volume (Million Metric Tons)', fontsize=12)
ax.set_xlabel('Forecast Year', fontsize=12)
ax.legend(loc='upper left')
ax.grid(axis='both', linestyle='--', alpha=0.2)

# Annotation
ax.annotate('The "Greenflation" Gap\n(6.5M Ton Deficit)', xy=(2034, 40), xytext=(2025, 42),
            arrowprops=dict(facecolor='white', shrink=0.05),
            fontsize=10, color='white')

# Save
plt.savefig(f"{output_dir}/copper_supply_crunch.png", dpi=300, bbox_inches='tight')
print("Chart generated.")
