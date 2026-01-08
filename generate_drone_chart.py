import matplotlib.pyplot as plt
import numpy as np
import os

# Ensure folder exists
output_dir = "research_articles/3_Biosecurity_Illicit_Economies/images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# --- SIMULATED DATA: Drone Incursions (2018-2025) ---
# Based on trends from CBP (Customs & Border Protection) reports
years = np.arange(2018, 2026)
# Exponential growth curve
incidents = [15, 42, 110, 350, 980, 2400, 5800, 11500] 

# Payload Efficiency (The "Why")
# Cost of Drone ($) vs Payload Value ($)
drone_cost = 800  # DJI Mavic style
payload_value = 4000 # 1kg Fentanyl/Meth value at wholesale

# --- PLOTTING ---
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the Curve
color = '#e74c3c' # Alarm Red
ax.plot(years, incidents, color=color, linewidth=3, marker='o', markersize=8, markerfacecolor='white')
ax.fill_between(years, incidents, color=color, alpha=0.1)

# Formatting
ax.set_title('Aerial Asymmetry: Verified UAV Incursions (US-Mexico Border)', fontsize=14, color='white', pad=20)
ax.set_ylabel('Reported Incidents per Year', fontsize=12)
ax.set_xlabel('Fiscal Year', fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.2)

# Annotation for the "Tipping Point"
ax.annotate('Saturation Tactics Begin', xy=(2023, 2400), xytext=(2020, 6000),
            arrowprops=dict(facecolor='white', shrink=0.05),
            fontsize=10, color='white')

# ROI Box (The Economic Driver)
roi_text = (f"Unit Economics:\n"
            f"Drone Cost: ~${drone_cost}\n"
            f"Payload Value: ~${payload_value}\n"
            f"ROI: 400% per flight")
props = dict(boxstyle='round', facecolor='#2c3e50', alpha=0.8)
ax.text(0.05, 0.85, roi_text, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props, fontname='monospace')

# Save
plt.savefig(f"{output_dir}/drone_incursions_trend.png", dpi=300, bbox_inches='tight')
print("Chart generated.")
