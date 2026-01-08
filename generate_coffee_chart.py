import matplotlib.pyplot as plt
import numpy as np
import os

# Ensure folder exists
output_dir = "research_articles/2_Climate_Finance/images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# --- SIMULATED DATA ---
months = np.arange(60)
rainfall_anomaly = np.random.normal(0, 5, 60)
rainfall_anomaly[35:48] -= 20  # Simulate Drought

# Simulate Price Reaction (Lagged)
base_price = 2200
price_shock = np.zeros(60)
for t in range(4, 60):
    if rainfall_anomaly[t-4] < -10:
        price_shock[t] += (abs(rainfall_anomaly[t-4]) * 35)

robusta_price = base_price + price_shock + np.random.normal(0, 50, 60)

# --- PLOTTING ---
plt.style.use('dark_background')
fig, ax1 = plt.subplots(figsize=(10, 6))

# Rainfall (Blue Bars)
color = '#3498db'
ax1.set_xlabel('Timeline (Months)', fontsize=12)
ax1.set_ylabel('Rainfall Deficit (mm)', color=color, fontsize=12)
ax1.bar(months, rainfall_anomaly, color=color, alpha=0.3, label='Rainfall')
ax1.tick_params(axis='y', labelcolor=color)

# Price (Red Line)
ax2 = ax1.twinx()
color = '#e74c3c'
ax2.set_ylabel('Robusta Futures ($/Ton)', color=color, fontsize=12)
ax2.plot(months, robusta_price, color=color, linewidth=2.5, label='Price')
ax2.tick_params(axis='y', labelcolor=color)

ax1.set_title('The Lag Effect: Rainfall Deficits vs. Price', fontsize=14, color='white')

# Save
plt.savefig(f"{output_dir}/robusta_lag_correlation.png", dpi=300, bbox_inches='tight')
print("Graph generated successfully.")
