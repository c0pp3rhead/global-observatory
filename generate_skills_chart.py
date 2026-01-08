import matplotlib.pyplot as plt
import numpy as np
import os

# Ensure assets folder exists
output_dir = "assets/images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# --- DATA: The Interdisciplinary Candidate ---
categories = [
    'Bio-Systems\nEngineering', 
    'Financial\nEconometrics', 
    'Geospatial\nIntelligence (OSINT)', 
    'Python/Data\nScience', 
    'Policy &\nGovernance'
]
# Score out of 10 (Self-Assessment for PhD)
values = [9, 8, 8, 9, 7]

# --- PLOTTING (Radar Chart) ---
# Repeat the first value to close the circle
values += values[:1]
N = len(categories)

# Calculate angles
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Draw the polygon
ax.plot(angles, values, color='#f1c40f', linewidth=2, linestyle='solid')
ax.fill(angles, values, color='#f1c40f', alpha=0.2)

# Formatting
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=11, color='white')
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['2', '4', '6', '8', '10'], color='#95a5a6', fontsize=9)
ax.set_ylim(0, 10)

# Title
ax.set_title('Research Capabilities Matrix', fontsize=16, color='white', pad=30)

# Save
plt.savefig(f"{output_dir}/skills_radar.png", dpi=300, bbox_inches='tight', transparent=True)
print("Skills Chart generated.")
