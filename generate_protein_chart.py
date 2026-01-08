import matplotlib.pyplot as plt
import numpy as np
import os

# Ensure folder exists
output_dir = "research_articles/1_Exoplanetary_Agriculture/images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# --- DATA: The Efficiency of Protein ---
# Source: FAO (Food and Agriculture Organization)
labels = ['Beef (Cattle)', 'Pork (Swine)', 'Poultry', 'Crickets (Acheta)']
# Feed Conversion Ratio: kg of feed needed for 1 kg of weight gain
fcr_values = [25.0, 9.0, 4.5, 1.7] 
# Water Footprint: Liters per kg of protein
water_values = [15400, 6000, 4300, 2000] # Approximate averages

y_pos = np.arange(len(labels))

# --- PLOTTING ---
plt.style.use('dark_background')
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot FCR (Bars)
color = '#2ecc71' # Green
rects = ax1.barh(y_pos, fcr_values, color=color, alpha=0.7, label='Feed Conversion Ratio (Lower is Better)')
ax1.set_xlabel('Feed Input (kg) to produce 1kg Mass', color='white', fontsize=12)
ax1.set_yticks(y_pos)
ax1.set_yticklabels(labels, fontsize=12, color='white')
ax1.invert_yaxis()  # Labels read top-to-bottom

# Annotate values
for i, v in enumerate(fcr_values):
    ax1.text(v + 0.5, i, f"{v}:1", color=color, va='center', fontweight='bold')

ax1.set_title('Thermodynamic Efficiency: The Case for Entomophagy on Mars', fontsize=16, pad=20, color='white')

# Add "The Insight" Box
text_str = "Mars Constraint:\nMass & Water are scarce.\nCrickets require ~15x less\ninput than beef."
props = dict(boxstyle='round', facecolor='#2c3e50', alpha=0.5)
ax1.text(0.7, 0.6, text_str, transform=ax1.transAxes, fontsize=11,
        verticalalignment='top', bbox=props, fontname='monospace', color='white')

# Save
plt.savefig(f"{output_dir}/protein_efficiency_roi.png", dpi=300, bbox_inches='tight')
print("Chart generated.")
