import matplotlib.pyplot as plt
import numpy as np
import os

# Ensure folder exists
output_dir = "research_articles/3_Biosecurity_Illicit_Economies/images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# --- SIMULATED DATA (2015-2025) ---
years = np.arange(2015, 2026)
n_years = len(years)

# 1. Total Market Value (Billions USD) - Growing steady
market_value = np.linspace(1.5, 3.2, n_years) 

# 2. Cartel "Tax" Rate (Extortion % per hectare/kg)
# Simulating a rise as cartels consolidated power in Michoacan
# 2015: ~1%, 2025: ~12% estimates
cartel_tax_rate = np.linspace(0.015, 0.12, n_years) + np.random.normal(0, 0.005, n_years)

# Calculate Revenues
cartel_revenue = market_value * cartel_tax_rate
legitimate_revenue = market_value - cartel_revenue

# --- PLOTTING ---
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 6))

# Stack plot
ax.stackplot(years, legitimate_revenue, cartel_revenue, 
             labels=['Legitimate Ag Revenue', 'Illicit Cartel Rent (Extortion)'],
             colors=['#27ae60', '#c0392b'], alpha=0.8)

# Formatting
ax.set_title('The Shadow Tax: Est. Cartel Revenue from Avocado Exports', fontsize=14, color='white', pad=20)
ax.set_ylabel('Annual Value (Billions USD)', fontsize=12)
ax.set_xlabel('Year', fontsize=12)
ax.legend(loc='upper left', frameon=False)
ax.grid(axis='y', linestyle='--', alpha=0.3)

# Annotation of the "tipping point"
ax.annotate('Fragmented Groups\nconsolidate control', xy=(2019, 2.0), xytext=(2016, 2.5),
            arrowprops=dict(facecolor='white', shrink=0.05),
            fontsize=9, color='white')

# Save
plt.savefig(f"{output_dir}/cartel_revenue_model.png", dpi=300, bbox_inches='tight')
print("Chart generated.")
