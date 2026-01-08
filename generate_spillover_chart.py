import matplotlib.pyplot as plt
import numpy as np
import os

# Ensure folder exists
output_dir = "research_articles/3_Biosecurity_Illicit_Economies/images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# --- SIMULATED DATA: The Edge Effect ---
# Fragmentation Index (0 to 100) -> How chopped up the forest is
fragmentation = np.linspace(10, 90, 50)

# 1. Biological Contact Rate (Viral Chatter)
# Exponential rise as humans enter deep forest
contact_risk = 0.5 * np.exp(0.06 * fragmentation) 

# 2. Economic Cost of Abatement (Conservation)
# It gets cheaper to prevent pandemics by conserving land than treating them
# But we plot the *Cost of Outbreak Response* here
outbreak_cost = 2 * contact_risk**1.2 # Non-linear cost scaling

# --- PLOTTING ---
plt.style.use('dark_background')
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot Risk Curve
color_risk = '#e74c3c'
ax1.plot(fragmentation, contact_risk, color=color_risk, linewidth=3, label='Probability of Zoonotic Spillover')
ax1.set_xlabel('Forest Fragmentation Index (%)', fontsize=12)
ax1.set_ylabel('Viral Risk Score (Normalized)', color=color_risk, fontsize=12)
ax1.tick_params(axis='y', labelcolor=color_risk)
ax1.fill_between(fragmentation, contact_risk, color=color_risk, alpha=0.1)

# Plot Cost (Secondary Axis)
ax2 = ax1.twinx()
color_cost = '#f1c40f'
ax2.plot(fragmentation, outbreak_cost, color=color_cost, linestyle='--', linewidth=2, label='Projected Economic Impact ($Bn)')
ax2.set_ylabel('Economic Impact ($ Billions)', color=color_cost, fontsize=12)
ax2.tick_params(axis='y', labelcolor=color_cost)

# Formatting
ax1.set_title('The Edge Effect: Deforestation vs. Pandemic Risk', fontsize=14, pad=20, color='white')
ax1.grid(axis='x', linestyle='--', alpha=0.2)

# Annotation: The Danger Zone
ax1.axvline(x=60, color='white', linestyle=':', linewidth=1)
ax1.text(62, 20, 'Critical Threshold:\n"Fishbone" Patterning', color='white', fontsize=10)

# Save
plt.savefig(f"{output_dir}/spillover_risk_model.png", dpi=300, bbox_inches='tight')
print("Chart generated.")
