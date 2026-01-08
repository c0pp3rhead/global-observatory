import matplotlib.pyplot as plt
import numpy as np
import os

# Ensure folder exists
output_dir = "research_articles/1_Exoplanetary_Agriculture/images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# --- SIMULATED DATA: Dose-Response Curve ---
# X-Axis: Radiation Dosage in Grays (Gy)
# Mars surface is ~0.25 Gy/year, but solar flares can spike this.
dosage = np.linspace(0, 10, 50) 

# Y-Axis: Biomass Yield (normalized to 100% at 0 radiation)
# 1. Wild Type (Normal Potato): Dies off quickly as radiation increases
wild_type_yield = 100 * np.exp(-0.5 * dosage) 

# 2. CRISPR-Cas9 Variant (Enhanced DNA Repair): Resists damage longer
# Modeled using a logistic decay curve (more resilience)
crispr_yield = 100 / (1 + np.exp(0.8 * (dosage - 6))) 

# Add some experimental "noise" (error bars logic)
noise = np.random.normal(0, 2, 50)
wild_type_yield += noise
crispr_yield += noise

# --- PLOTTING ---
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 6))

# Plot Lines
ax.plot(dosage, wild_type_yield, color='#95a5a6', linestyle='--', linewidth=2, label='Wild Type (Control)')
ax.plot(dosage, crispr_yield, color='#2ecc71', linewidth=3, label='CRISPR-Cas9 Variant (D. radiodurans gene)')

# Fill area to show the "Gain"
ax.fill_between(dosage, wild_type_yield, crispr_yield, color='#2ecc71', alpha=0.1, label='Yield Gain')

# Formatting
ax.set_title('Radio-Resistance: Biomass Yield under Gamma Irradiation', fontsize=14, color='white', pad=20)
ax.set_xlabel('Radiation Dosage (Gy)', fontsize=12)
ax.set_ylabel('Biomass Yield (% of Baseline)', fontsize=12)
ax.legend(loc='lower left')
ax.grid(axis='both', linestyle='--', alpha=0.2)

# Annotation: Mars Context
ax.axvline(x=2.5, color='#e74c3c', linewidth=1, linestyle=':')
ax.text(2.6, 90, 'Simulated Solar\nParticle Event (SPE)', color='#e74c3c', fontsize=9)

# Save
plt.savefig(f"{output_dir}/potato_radiation_yield.png", dpi=300, bbox_inches='tight')
print("Chart generated.")
