import os
import random
import matplotlib.pyplot as plt  # <--- Corrected to 'plt'
import numpy as np
from openai import OpenAI
import time

# --- CONFIGURATION ---
API_KEY = "HIDDEN_FOR_SECURITY"
client = OpenAI(api_key=API_KEY)
TARGET_PER_PILLAR = 670  # approx 2010 total articles

pillars = {
    "1_Exoplanetary_Agriculture": "research_articles/1_Exoplanetary_Agriculture",
    "2_Climate_Finance": "research_articles/2_Climate_Finance",
    "3_Biosecurity_Illicit_Economies": "research_articles/3_Biosecurity_Illicit_Economies"
}

# --- ENGINEERING KEYWORD BANKS ---

space_engineering = {
    "systems": [
        "Membrane-Aerated Bioreactors", "Closed-Loop Hydroponics", "Sabatier Reactors", "Solid Oxide Electrolyzers", 
        "Algal Photobioreactors", "Zeolite Filtration Units", "Centrifugal Separators", "Aeroponic Atomizers", 
        "Mycelium Composites", "Thermal Control Loops", "Vacuum Distillation Units", "Radioisotope Thermoelectric Generators",
        "Ion-Exchange Resin Columns", "Haptic Tele-Robotics", "Bio-Regenerative Life Support (BLSS)", "Vapor Phase Catalysis",
        "Electrodialysis Reversal Systems", "Magnetohydrodynamic Pumps", "Variable Frequency Drives", "Quantum Dot LEDs",
        "Peristaltic Nutrient Injectors", "Anaerobic Digesters", "Cryogenic Seed Vaults", "Atmospheric Water Generators"
    ],
    "variables": [
        "Mass Transfer Coefficients", "Thermodynamic Efficiency", "Fluid Dynamics", "Metabolic Flux", "PID Control Logic", 
        "Heat Exchange Fouling", "Nutrient Stoichiometry", "VPD Optimization", "Sensor Fusion", "Power Load Balancing",
        "Reynolds Number Analysis", "Stoichiometric Balancing", "Enzymatic Kinetics", "Hydraulic Retention Time",
        "Redox Potential Stabilization", "Photosynthetic Photon Flux Density (PPFD)", "Gas-Liquid Interfacial Area",
        "Heat Dissipation Rates", "Microbial Population Dynamics", "Toxicity Thresholds"
    ],
    "context": [
        "in Microgravity", "for Mars Transit", "on Lunar South Pole", "in Vacuum Conditions", "under High Radiation", 
        "during Solar Particle Events", "in Pressurized Domes", "for Deep Space Habitats", "in Lagrange Point Stations",
        "using In-Situ Resources (ISRU)", "during Hypobaric Decompression", "for Interstellar Generation Ships",
        "in Regolith Lava Tubes", "under Artificial Gravity", "during Dust Storms"
    ]
}

climate_engineering = {
    "systems": [
        "Direct Air Capture (DAC)", "Bio-Energy with Carbon Capture (BECCS)", "Enhanced Weathering Silicates", 
        "Anaerobic Digesters", "Vertical Farming Arrays", "Desalination Plants", "Ocean Iron Fertilization", 
        "Precision Irrigation IoT", "Green Hydrogen Electrolyzers", "Pyrolysis Kilns", "Geothermal Heat Pumps",
        "Tidal Barrage Turbines", "Molten Salt Storage", "Perovskite Solar Cells", "Grid-Scale Batteries",
        "Mangrove Restoration Barriers", "Cloud Seeding Drones", "Biochar Kilns", "Synthetic Fuel Refineries"
    ],
    "metrics": [
        "Techno-Economic Analysis (TEA)", "Life Cycle Assessment (LCA)", "Levelized Cost of Carbon (LCOC)", 
        "Capital Expenditure (CapEx) Models", "Operational Risk Premia", "Supply Chain Volatility", 
        "Energy Return on Investment (EROI)", "Discount Rate Sensitivity", "Carbon Credit Arbitrage",
        "Thermodynamic Exergy Loss", "Water Withdrawal Rates", "Land Use Efficiency", "Marginal Abatement Cost",
        "Material Criticality Index", "Grid Interconnection Queue Times", "Insurance Payout Ratios"
    ],
    "context": [
        "in Emerging Markets", "for Sovereign Debt Restructuring", "under Net-Zero Mandates", 
        "for Carbon Offset Verification", "in Arid Climates", "for Grid Stabilization", "in Coastal Resilience Projects",
        "under 4°C Warming Scenarios", "for Stranded Asset Valuation", "in Post-Glacial Watersheds",
        "during Extreme Heat Events", "for Reinsurance Portfolios", "in Sub-Saharan Infrastructure"
    ]
}

bio_engineering = {
    "systems": [
        "Automated DNA Synthesizers", "Industrial Bioreactors", "Genomic Sequencers", "Air-Gapped Control Systems", 
        "Cold Chain Logistics", "Remote Sensing Satellites", "Forensic Genealogy Databases", "Autonomous Drones", 
        "Municipal Water Sensors", "CRISPR-Cas9 Editing Suites", "Microfluidic Lab-on-a-Chip", "Bio-Safety Level 4 Airlocks",
        "Encrypted Ledger Nodes", "Facial Recognition Gateways", "Isotope Ratio Mass Spectrometers",
        "Neural Network Classifiers", "Programmable Logic Controllers (PLCs)", "SCADA Systems"
    ],
    "threats": [
        "Cyber-Physical Vulnerabilities", "Hardware Trojans", "Adversarial AI Attacks", "Insider Threats", 
        "Supply Chain Interdiction", "Biometric Spoofing", "Encrypted Payloads", "Signal Jamming", "Data Poisoning",
        "Engineered Pathogen Leakage", "Dual-Use Research of Concern", "Side-Channel Attacks", "Zero-Day Exploits",
        "Man-in-the-Middle Attacks", "Protocol Fuzzing", "Sensor Saturation"
    ],
    "context": [
        "in High-Containment Labs", "for Illicit Trade Tracking", "in Dual-Use Facilities", "for Border Security", 
        "in Clandestine Labs", "on the Dark Web", "during Pandemics", "for Agricultural Defense",
        "in Failed States", "at Port of Entry Checkpoints", "within Crypto-Darknet Markets", "for Vaccine Distribution"
    ]
}

# --- FUNCTIONS ---

def generate_article_content(title, category):
    prompt = f"""
    Write a rigorous 'Biosystems Engineering' research note titled '{title}' for the category '{category}'.
    
    Style Guide:
    - Tone: Academic, Engineering-focused, Quantitative. "Hard Sci-Fi" realism.
    - Structure: 
        1. Engineering Abstract (Problem Statement)
        2. System Architecture (Technical components, inputs/outputs)
        3. Mathematical Framework (Describe the equations/logic used, e.g., Navier-Stokes, Black-Scholes, SIR Models)
        4. Simulation Results (Refer to Figure 1)
        5. Failure Modes & Risk Analysis
    - Length: ~1000-1200 words.
    - Content Requirements: Use specific units (kW, kg/day, MPa), chemical formulas, and cite specific algorithms/standards (ISO, IEEE).
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o", 
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error: {e}")
        return None

def generate_chart(folder, title):
    img_name = title.replace(" ", "_").replace("-", "_").replace(":", "").replace("__", "_")[:150] + ".png"
    save_path = f"{folder}/images/{img_name}"
    
    if os.path.exists(save_path): return

    plt.style.use('grayscale')
    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.linspace(0, 100, 50)
    y = np.sin(x/5) * np.exp(x/50) + np.random.normal(0, 0.1, 50) 
    
    ax.plot(x, y, color='black', linewidth=1.5, marker='.', markersize=5)
    ax.set_title(f"System Performance Data", fontsize=10)
    ax.set_ylabel("Efficiency / Output (Normalized)")
    ax.set_xlabel("Time (h) / Simulation Cycles")
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.savefig(save_path, dpi=100, bbox_inches='tight')
    plt.close()

# --- EXECUTION LOOP ---

tasks = [
    (pillars["1_Exoplanetary_Agriculture"], space_engineering, "Biosystems Engineering (Space)", "Space"),
    (pillars["2_Climate_Finance"], climate_engineering, "Biosystems Engineering (Finance)", "Climate"),
    (pillars["3_Biosecurity_Illicit_Economies"], bio_engineering, "Biosystems Engineering (Security)", "Bio")
]

print(f"--- ⚙️ STARTING GENERATION (Target: {TARGET_PER_PILLAR} Articles per Pillar) ---")

for folder, keywords, category_name, key_type in tasks:
    
    current_files = [f for f in os.listdir(folder) if f.endswith(".md")]
    count = len(current_files)
    print(f"\n📂 Pillar: {category_name} | Current: {count} | Target: {TARGET_PER_PILLAR}")
    
    while count < TARGET_PER_PILLAR:
        if key_type == "Space":
            title = f"{random.choice(keywords['variables'])} of {random.choice(keywords['systems'])} {random.choice(keywords['context'])}"
        elif key_type == "Climate":
            title = f"{random.choice(keywords['metrics'])} of {random.choice(keywords['systems'])} {random.choice(keywords['context'])}"
        else: # Bio
            title = f"{random.choice(keywords['threats'])} in {random.choice(keywords['systems'])} {random.choice(keywords['context'])}"
            
        safe_filename = title.replace(" ", "_").replace("-", "_").replace(":", "").replace("__", "_")[:150] + ".md"
        file_path = f"{folder}/{safe_filename}"
        
        if os.path.exists(file_path):
            continue
            
        print(f"  [{count+1}/{TARGET_PER_PILLAR}] Generating: {title[:60]}...")
        
        content = generate_article_content(title, category_name)
        
        if content:
            full_text = f"# {title}\n**Domain:** {category_name} | **Read Time:** 15 min\n**Keywords:** Biosystems, Engineering, Modeling\n\n" + content
            with open(file_path, "w") as f:
                f.write(full_text)
            generate_chart(folder, title)
            count += 1
            time.sleep(0.5)

print("\n✅ MISSION COMPLETE. 2000 Articles Live.")
