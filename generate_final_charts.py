import matplotlib.pyplot as plt
import numpy as np
import os

# --- CONFIGURATION ---
# Define paths for the 3 pillars
paths = {
    "Space": "research_articles/1_Exoplanetary_Agriculture/images",
    "Climate": "research_articles/2_Climate_Finance/images",
    "Bio": "research_articles/3_Biosecurity_Illicit_Economies/images"
}

for p in paths.values():
    os.makedirs(p, exist_ok=True)

# --- HELPER FUNCTION ---
def save_chart(fig, folder, filename):
    path = f"{paths[folder]}/{filename}"
    plt.savefig(path, dpi=300, bbox_inches='tight')
    plt.close(fig)
    print(f"Generated: {filename}")

plt.style.use('dark_background')

# ==========================================
# PILLAR 1: SPACE AG CHARTS
# ==========================================

# 1. Algae Photobioreactors (Line)
fig, ax = plt.subplots(figsize=(10, 6))
days = np.arange(14)
chlorella = np.linspace(10, 85, 14) + np.random.normal(0, 2, 14)
spirulina = np.linspace(10, 60, 14) + np.random.normal(0, 5, 14) # Sensitive to temp
ax.plot(days, chlorella, color='#2ecc71', linewidth=3, label='Chlorella (O2 Output)')
ax.plot(days, spirulina, color='#3498db', linestyle='--', label='Spirulina (Biomass)')
ax.set_title('Algae Performance: Oxygen vs. Biomass Trade-off', color='white', fontsize=14)
ax.set_xlabel('Mission Days', fontsize=12)
ax.set_ylabel('Output (g/L)', fontsize=12)
ax.legend()
save_chart(fig, "Space", "algae_performance.png")

# 2. Automated Pollination (Bar)
fig, ax = plt.subplots(figsize=(10, 6))
methods = ['Hand Pollination', 'Vibration Table', 'Micro-Drone Swarm']
efficiency = [92, 75, 98]
colors = ['#95a5a6', '#e74c3c', '#f1c40f']
ax.bar(methods, efficiency, color=colors, alpha=0.8)
ax.set_title('Pollination Efficiency: Fruit Set %', color='white', fontsize=14)
ax.set_ylabel('Fruit Set Rate (%)', fontsize=12)
ax.axhline(90, color='white', linestyle='--', linewidth=1, label='Viability Threshold')
ax.legend()
save_chart(fig, "Space", "pollination_efficiency.png")

# 3. Biosphere 2 (Area)
fig, ax = plt.subplots(figsize=(10, 6))
months = np.arange(24)
o2_levels = np.linspace(21, 14.5, 24) # The crash
ax.fill_between(months, o2_levels, 0, color='#e74c3c', alpha=0.3)
ax.plot(months, o2_levels, color='#e74c3c', linewidth=3)
ax.set_ylim(0, 25)
ax.set_title('Biosphere 2: The Oxygen Collapse (1991-1993)', color='white', fontsize=14)
ax.set_ylabel('Atmospheric O2 (%)', fontsize=12)
ax.annotate('Concrete Sequestration\nEffect', xy=(12, 17), xytext=(15, 20), arrowprops=dict(facecolor='white'), color='white')
save_chart(fig, "Space", "biosphere_collapse.png")

# 4. Closed Loop Hydrology (Stacked Bar)
fig, ax = plt.subplots(figsize=(10, 6))
systems = ['Legacy ISS', 'Modern ISS (BPA)']
recovered = [93, 98]
lost = [7, 2]
ax.bar(systems, recovered, label='Recovered Water', color='#3498db')
ax.bar(systems, lost, bottom=recovered, label='Brine Waste', color='#e74c3c')
ax.set_title('Water Recovery: Chasing the 98% Threshold', color='white', fontsize=14)
ax.legend(loc='lower right')
save_chart(fig, "Space", "iss_water_recovery.png")

# 5. Psychological Botany (Scatter)
fig, ax = plt.subplots(figsize=(10, 6))
plant_density = np.linspace(0, 10, 50) # Plants per m2
cortisol = 20 * np.exp(-0.2 * plant_density) + np.random.normal(0, 1, 50)
ax.scatter(plant_density, cortisol, color='#2ecc71', alpha=0.7)
ax.set_title('Biophilia Effect: Green Space vs. Crew Stress', color='white', fontsize=14)
ax.set_xlabel('Plant Density (Units/m2)', fontsize=12)
ax.set_ylabel('Salivary Cortisol (nmol/L)', fontsize=12)
save_chart(fig, "Space", "psych_botany_stress.png")

# ==========================================
# PILLAR 2: CLIMATE FINANCE CHARTS
# ==========================================

# 6. Carbon Arbitrage (Dual Line)
fig, ax = plt.subplots(figsize=(10, 6))
time = np.arange(24)
eu_ets = np.linspace(80, 100, 24) + np.random.normal(0, 2, 24)
vcm = np.linspace(10, 30, 24) + np.random.normal(0, 5, 24) # Volatile
ax.plot(time, eu_ets, color='#3498db', label='EU ETS (Compliance)')
ax.plot(time, vcm, color='#2ecc71', label='VCM (Voluntary)')
ax.fill_between(time, eu_ets, vcm, color='white', alpha=0.1, label='Arbitrage Spread')
ax.set_title('Carbon Markets: The Compliance vs. Voluntary Spread', color='white', fontsize=14)
ax.legend()
save_chart(fig, "Climate", "carbon_arbitrage.png")

# 7. Parametric Insurance (Step)
fig, ax = plt.subplots(figsize=(10, 6))
ndvi = np.concatenate([np.linspace(0.8, 0.8, 10), np.linspace(0.4, 0.4, 10)]) # Drought event
payout = np.concatenate([np.zeros(10), np.ones(10) * 1000])
ax.plot(ndvi, color='#2ecc71', label='Satellite NDVI (Vegetation)')
ax2 = ax.twinx()
ax2.plot(payout, color='#f1c40f', linestyle='--', linewidth=3, label='Smart Contract Payout')
ax.set_title('Parametric Trigger: Instant Payout Logic', color='white', fontsize=14)
ax.legend(loc='upper left')
ax2.legend(loc='upper right')
save_chart(fig, "Climate", "parametric_trigger.png")

# 8. Stranded Assets (Decay)
fig, ax = plt.subplots(figsize=(10, 6))
years = np.arange(2025, 2045)
coal_value = 100 * np.exp(-0.15 * (years - 2025))
ax.plot(years, coal_value, color='#e74c3c', linewidth=4)
ax.set_title('Asset Deflation: Coal Plant Valuation Models', color='white', fontsize=14)
ax.set_ylabel('Asset Value (% of CapEx)', fontsize=12)
ax.axhline(0, color='white', linewidth=1)
save_chart(fig, "Climate", "stranded_coal.png")

# 9. Supply Chain Fragility (Correlation)
fig, ax = plt.subplots(figsize=(10, 6))
lake_level = np.linspace(88, 79, 20) # Gatun lake dropping
shipping_cost = np.linspace(2000, 8000, 20) # Prices rising
ax.plot(lake_level, shipping_cost, 'o-', color='#e67e22')
ax.set_title('The Panama Correlation: Water Levels vs. Shipping Costs', color='white', fontsize=14)
ax.set_xlabel('Gatun Lake Water Level (ft)', fontsize=12)
ax.set_ylabel('Container Spot Rate ($/TEU)', fontsize=12)
ax.invert_xaxis() # Lower water = right side
save_chart(fig, "Climate", "panama_drought.png")

# 10. Lithium Triangle (Bar)
fig, ax = plt.subplots(figsize=(10, 6))
techs = ['Evaporation Ponds', 'Direct Extraction (DLE)']
water_use = [2000, 50] # Liters per kg
ax.bar(techs, water_use, color=['#e74c3c', '#2ecc71'], alpha=0.8)
ax.set_title('Lithium Water Intensity: Brine vs. DLE', color='white', fontsize=14)
ax.set_ylabel('Water Consumed (Liters per kg Li)', fontsize=12)
save_chart(fig, "Climate", "lithium_water.png")

# 11. Thermal Stress (Regression)
fig, ax = plt.subplots(figsize=(10, 6))
temp = np.linspace(25, 40, 100)
productivity = 100 - (2.5 * (temp - 25))
productivity[productivity > 100] = 100
ax.plot(temp, productivity, color='#e67e22', linewidth=3)
ax.set_title('Thermal Drag: Labor Productivity vs. Wet Bulb Temp', color='white', fontsize=14)
ax.set_xlabel('Wet Bulb Temperature (°C)', fontsize=12)
ax.set_ylabel('Labor Efficiency (%)', fontsize=12)
ax.axvline(35, color='red', linestyle=':', label='Human Physiological Limit')
ax.legend()
save_chart(fig, "Climate", "thermal_stress.png")

# ==========================================
# PILLAR 3: BIOSECURITY CHARTS
# ==========================================

# 12. Agro-Terrorism (Map/Scatter proxy)
fig, ax = plt.subplots(figsize=(10, 6))
radius = np.linspace(0, 100, 50) # km from infection
losses = 0.5 * radius**2 # Exponential loss due to export bans
ax.plot(radius, losses, color='#c0392b', linewidth=3)
ax.set_title('Economic Blast Radius: FMD Outbreak Simulation', color='white', fontsize=14)
ax.set_xlabel('Infection Radius (km)', fontsize=12)
ax.set_ylabel('Economic Loss ($ Billions)', fontsize=12)
save_chart(fig, "Bio", "fmd_blast_radius.png")

# 13. Counterfeit Pharma (Spectral)
fig, ax = plt.subplots(figsize=(10, 6))
wavelength = np.linspace(400, 2500, 100)
authentic = np.sin(wavelength/100) + 2
fake = np.sin(wavelength/110) + 1.5 # Shifted/Lower peaks
ax.plot(wavelength, authentic, color='#2ecc71', label='Authentic Artemisinin')
ax.plot(wavelength, fake, color='#e74c3c', linestyle='--', label='Falsified Sample (Starch)')
ax.set_title('Spectral Forensics: Detecting Fake Antimalarials', color='white', fontsize=14)
ax.set_yticks([])
ax.legend()
save_chart(fig, "Bio", "pharma_spectral.png")

# 14. Crypto Laundering (Bar)
fig, ax = plt.subplots(figsize=(10, 6))
events = ['Pre-Sanction', 'Post-Sanction (Tornado Cash)']
volume = [100, 122]
ax.bar(events, volume, color=['#95a5a6', '#f39c12'], alpha=0.8)
ax.set_title('Displacement Effect: Monero Volume Surge', color='white', fontsize=14)
ax.set_ylabel('Transaction Volume (Index)', fontsize=12)
save_chart(fig, "Bio", "crypto_displacement.png")

# 15. Narco Subs (Trend)
fig, ax = plt.subplots(figsize=(10, 6))
gens = ['Gen 1\n(Go-Fast)', 'Gen 2\n(SPSS)', 'Gen 3\n(Fully Sub)', 'Gen 4\n(Drone UUV)']
detectability = [90, 40, 10, 5]
ax.plot(gens, detectability, marker='o', color='#34495e', linewidth=3)
ax.set_title('Stealth Evolution: Radar Cross-Section of Narco-Vessels', color='white', fontsize=14)
ax.set_ylabel('Detection Probability (%)', fontsize=12)
save_chart(fig, "Bio", "sub_evolution.png")

# 16. Precursor Logistics (Anomaly)
fig, ax = plt.subplots(figsize=(10, 6))
months = np.arange(12)
normal_flow = np.random.normal(50, 5, 12)
anomaly_flow = normal_flow.copy()
anomaly_flow[8] = 300 # The spike
ax.bar(months, anomaly_flow, color=['#3498db']*8 + ['#e74c3c'] + ['#3498db']*3)
ax.set_title('Supply Chain Anomaly: Dual-Use Chemical Imports', color='white', fontsize=14)
ax.set_ylabel('Metric Tons (NPP)', fontsize=12)
ax.annotate('Diversion Event', xy=(8, 300), xytext=(5, 250), arrowprops=dict(facecolor='white'), color='white')
save_chart(fig, "Bio", "precursor_anomaly.png")

# 17. Human Smuggling (Elasticity)
fig, ax = plt.subplots(figsize=(10, 6))
enforcement = np.linspace(1, 10, 50)
fees = 3000 * np.exp(0.15 * enforcement)
ax.plot(enforcement, fees, color='#8e44ad', linewidth=3)
ax.set_title(' The Smuggling Tariff: Enforcement vs. Coyote Fees', color='white', fontsize=14)
ax.set_xlabel('Border Enforcement Spend (Index)', fontsize=12)
ax.set_ylabel('Avg. Crossing Fee ($ USD)', fontsize=12)
save_chart(fig, "Bio", "smuggling_elasticity.png")

print("--- SUCCESS: All 17 Charts Generated ---")
