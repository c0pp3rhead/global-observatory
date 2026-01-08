import matplotlib.pyplot as plt
import numpy as np
import os

# Ensure folder exists
output_dir = "research_articles/1_Exoplanetary_Agriculture/images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Calculation Logic
human_o2_req_kg_day = 0.84 
perchlorate_concentration = 0.006 
oxygen_yield_ratio = 0.643 

def soil_needed(people):
    return (people * human_o2_req_kg_day) / (perchlorate_concentration * oxygen_yield_ratio)

crew_sizes = np.arange(1, 7, 1)
soil_requirements = [soil_needed(p) for p in crew_sizes]

# Plotting
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(crew_sizes, soil_requirements, color='#e74c3c', alpha=0.8)

ax.set_title('ISRU Analysis: Regolith Processing for O2 Life Support', fontsize=16, color='white')
ax.set_xlabel('Crew Size', fontsize=12)
ax.set_ylabel('Regolith Required (kg/day)', fontsize=12)

# Labels
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{int(height)} kg', xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points", ha='center', color='#f1c40f')

# Save
plt.savefig(f"{output_dir}/mars_oxygen_balance.png", dpi=300, bbox_inches='tight')
print("Graph generated successfully.")
