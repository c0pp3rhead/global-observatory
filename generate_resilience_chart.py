import matplotlib.pyplot as plt
import numpy as np
import os

# Ensure folder exists
output_dir = "research_articles/2_Climate_Finance/images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# --- SIMULATED DATA: 20-Year Project Cycle ---
years = np.arange(0, 21)

# 1. Grey Infrastructure (Concrete Seawall)
# High CapEx ($10M), High O&M ($0.5M/yr), Fixed Protection Value
capex_grey = 10
maintenance_grey = 0.5
value_grey = 1.2 # Avoided flood damages per year
# Cumulative Cash Flow
net_grey = [-capex_grey]
for i in range(20):
    net_grey.append(net_grey[-1] + value_grey - maintenance_grey)

# 2. Green Infrastructure (Mangrove Restoration)
# Low CapEx ($2M), Negative Maintenance (Self-repairing), Growing Value (Carbon + Fish)
capex_green = 2
value_green_base = 0.8 # Flood protection starts lower (trees are small)
# Value grows as trees mature (Carbon credits + Fisheries)
net_green = [-capex_green]
current_val = -capex_green
for i in range(20):
    # Trees grow: protection + carbon value increases by 10% per year
    annual_benefit = value_green_base * (1.1 ** i) 
    current_val += annual_benefit
    net_green.append(current_val)

# --- PLOTTING ---
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 6))

# Plot Lines
ax.plot(years, net_grey, color='#95a5a6', linewidth=3, linestyle='--', label='Grey Infra (Seawalls)')
ax.plot(years, net_green, color='#2ecc71', linewidth=3, label='Green Infra (Mangroves)')

# Zero Line (Break Even)
ax.axhline(0, color='white', linewidth=1, alpha=0.5)

# Formatting
ax.set_title('Disaster Resilience ROI: Cumulative Net Present Value (NPV)', fontsize=14, pad=20, color='white')
ax.set_ylabel('Cumulative Net Value ($ Millions)', fontsize=12)
ax.set_xlabel('Project Year', fontsize=12)
ax.legend(loc='upper left')
ax.grid(axis='both', linestyle='--', alpha=0.2)

# Annotations
ax.annotate('Break-Even Point (Year 4)', xy=(4, 0), xytext=(6, -5),
            arrowprops=dict(facecolor='white', shrink=0.05),
            fontsize=10, color='white')

ax.annotate('The "Appreciating Asset" Gap\n(Carbon + Fisheries Value)', xy=(19, net_green[-1]), xytext=(12, 30),
            arrowprops=dict(facecolor='#2ecc71', shrink=0.05),
            fontsize=10, color='#2ecc71')

# Save
plt.savefig(f"{output_dir}/infrastructure_roi.png", dpi=300, bbox_inches='tight')
print("Chart generated.")
