import matplotlib.pyplot as plt
import numpy as np
import os

# Ensure folder exists
output_dir = "research_articles/1_Exoplanetary_Agriculture/images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# --- DATA: Substrate Physics ---
substrates = ['Earth Rockwool\n(Control)', 'Raw Martian Regolith\n(Unprocessed)', 'Sintered Basalt Fiber\n(Mars ISRU)']

# 1. Water Holding Capacity (% Volume) - "The Sponge Effect"
# Rockwool is famous for holding huge amounts of water. Regolith is sandy/dense.
whc = [85, 35, 82] 

# 2. Air-Filled Porosity (% Volume) - "Root Breathability"
# Roots need oxygen. Regolith suffocates them. Fibers breathe.
afp = [18, 5, 20]

x = np.arange(len(substrates))
width = 0.35

# --- PLOTTING ---
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 6))

# Plot Bars
rects1 = ax.bar(x - width/2, whc, width, label='Water Holding Capacity (%)', color='#3498db', alpha=0.8)
rects2 = ax.bar(x + width/2, afp, width, label='Air-Filled Porosity (%)', color='#2ecc71', alpha=0.8)

# Formatting
ax.set_title('Substrate Physics: Why Mars Needs Fiber, Not Dirt', fontsize=16, pad=20, color='white')
ax.set_ylabel('Volume Percentage (%)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(substrates, fontsize=11)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2)
ax.grid(axis='y', linestyle='--', alpha=0.2)

# Annotations
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}%',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points",
                    ha='center', va='bottom', color='white', fontweight='bold')

autolabel(rects1)
autolabel(rects2)

# Save
plt.savefig(f"{output_dir}/basalt_substrate_analysis.png", dpi=300, bbox_inches='tight')
print("Chart generated.")
