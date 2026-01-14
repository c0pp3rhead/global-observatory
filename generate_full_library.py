import os
import random
import matplotlib.pyplot as plt
import numpy as np
from openai import OpenAI
import time

# --- 1. CONFIGURATION ---
API_KEY = "HIDDEN_KEY"
client = OpenAI(api_key=API_KEY)

pillars = {
    "1_Exoplanetary_Agriculture": "research_articles/1_Exoplanetary_Agriculture",
    "2_Climate_Finance": "research_articles/2_Climate_Finance",
    "3_Biosecurity_Illicit_Economies": "research_articles/3_Biosecurity_Illicit_Economies"
}

# --- 2. EXPANDED TITLE DATA BANKS (Fixes the Infinite Loop) ---
space_keywords = {
    "topics": [
        "Aeroponic Systems", "Regolith Remediation", "Algae Photobioreactors", "Mycelium Structural Materials", 
        "Closed-Loop Hydrology", "Automated Pollination", "Substrate Engineering", "Genomic Resilience", 
        "Entomophagy Protein", "Centrifugal Agriculture", "Hydroponic Nutrient Films", "Atmospheric Water Generators",
        "Synthetic Soil Microbes", "Lunar Lava Tube Greenhouses", "Radiation Shielding Polymers", "Biomass Fermentation",
        "Genetic Seed Vaults", "Waste-Heat Capture", "Vertical Farming Arrays", "Cryogenic Seed Dormancy"
    ],
    "contexts": [
        "in Low Earth Orbit", "for Martian Colonization", "in Deep Space Transit", "for Lunar Outposts", 
        "under High Radiation", "in Zero-G Environments", "with Limited Biomass", "for Long-Duration Missions",
        "in Pressurized Domes", "using In-Situ Resources", "during Solar Flares", "for Interstellar Arks"
    ]
}

climate_keywords = {
    "topics": [
        "Carbon Border Adjustment", "Greenflation", "Lithium Supply Chain", "Catastrophe Bonds", 
        "Grid Resilience", "Aquifer Depletion", "Blue Carbon", "Methane Leak Detection", 
        "Direct Air Capture", "Rare Earth Geopolitics", "Hydrogen Electrolysis Costs", "Cobalt Mining Ethics",
        "Nuclear Fusion Investment", "Geothermal Base Load", "Tidal Energy Yields", "Electric Vehicle ROI",
        "Sustainable Aviation Fuel", "Climate Refugee Migration", "Coastal Property Devaluation", "Crop Yield Volatility"
    ],
    "contexts": [
        "and Sovereign Debt", "in Emerging Markets", "Volatility Modeling", "Risk Premiums", 
        "Arbitrage Strategies", "Regulatory Impact", "Supply Chain Shocks", "Insurance Failures",
        "in the Global South", "under Net-Zero Targets", "during Heat Waves", "post-Paris Agreement"
    ]
}

bio_keywords = {
    "topics": [
        "Narco-Submarine Logistics", "Crypto-Laundering", "Drone Asymmetry", "Precursor Tracking", 
        "The Blood Avocado Trade", "Human Smuggling Tariffs", "Counterfeit Pharma", "Wildlife Trafficking", 
        "Trade-Based Laundering", "Dark Web Markets", "Ransomware Payment Flows", "Illegal Sand Mining",
        "Gold Smuggling Routes", "Conflict Diamond Certification", "Organ Trafficking Networks", "Identity Theft Farms",
        "Synthetic Opioid Labs", "Maritime Piracy Insurance", "Art Fraud Valuation", "Passport Forgery Rings"
    ],
    "contexts": [
        "in the Global South", "and Blockchain Forensics", "Supply Chain Vulnerabilities", "Shadow Economic Theory", 
        "Border Enforcement Models", "Port Security Analysis", "Financial Interdiction", "Network Topology",
        "using Shell Companies", "via Satellite Evasion", "in Failed States", "through Free Trade Zones"
    ]
}

# --- 3. FUNCTIONS ---

def generate_titles(base_list, keywords, count=100):
    """Generates a list of 100 titles without getting stuck."""
    titles = base_list[:]
    attempts = 0
    max_attempts = 500 # Safety brake
    
    while len(titles) < count and attempts < max_attempts:
        topic = random.choice(keywords["topics"])
        context = random.choice(keywords["contexts"])
        new_title = f"{topic} {context}"
        if new_title not in titles:
            titles.append(new_title)
        attempts += 1
        
    return titles[:count]

def generate_article_content(title, category):
    prompt = f"""
    Write a comprehensive, technical research article titled '{title}' for the category '{category}'.
    
    Target Audience: PhD level / Sci-Fi readers.
    Tone: Professional, Analytical, "Hard Sci-Fi" realism.
    Length: Approximately 1200-1500 words.
    
    Structure:
    1. Executive Summary
    2. Historical Context (1990-2020)
    3. Technical Architecture / Methodology
    4. Data Analysis (Reference 'Figure 1' in the text)
    5. Economic Impact Models
    6. Risk Assessment
    7. Future Outlook (2030-2050)
    
    Content: Invent plausible data, citations, and specific chemical/financial details.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"  [Error] API Issue: {e}")
        return None

def generate_chart(folder, title):
    img_name = title.replace(" ", "_").replace("-", "_").replace(":", "").replace("__", "_") + ".png"
    save_path = f"{folder}/images/{img_name}"
    # Try/Except to handle long filenames
    try:
        if len(save_path) > 250: save_path = save_path[:245] + ".png"
        
        plt.style.use('grayscale')
        fig, ax = plt.subplots(figsize=(10, 5))
        x = np.arange(2020, 2040)
        trend = np.linspace(10, random.uniform(50, 150), len(x)) 
        noise = np.random.normal(0, 10, len(x))
        y = trend + noise
        
        ax.plot(x, y, color='black', linewidth=2.5, marker='o', markersize=4)
        ax.set_title(f"Projected Impact Analysis", fontsize=12, pad=20)
        ax.set_ylabel("Efficiency Index")
        ax.set_xlabel("Fiscal Year")
        ax.grid(True, linestyle='--', alpha=0.3)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        plt.savefig(save_path, dpi=100, bbox_inches='tight')
        plt.close()
    except Exception as e:
        print(f"  [Error] Chart failed: {e}")

# --- 4. EXECUTION LOOP ---

# Define Hero Lists
space_hero = ["Algae Photobioreactors", "Automated Pollination", "Biosphere 2 Revisited", "Closed-Loop Hydrology", "Psychological Botany", "Waste-to-Biomass", "Genetic Resilience", "Hydroponic Substrates", "The Caloric ROI of Entomophagy", "Regolith Remediation"]
climate_hero = ["Air Quality Mortality", "Aluminum Smelting Energy", "Aquifer Depletion Bonds", "Battery Storage Arbitrage", "Biochar Market Liquidity", "Carbon Border Adjustment Mechanism", "Catastrophe Bond Spreads", "Central Bank Climate Stress Tests", "Cobalt Supply Shocks", "Greenflation Metrics"]
bio_hero = ["Agro-Terrorism Simulations", "Counterfeit Pharmaceuticals", "Crypto-Laundering", "Drone Asymmetry", "Narco-Submarine Engineering", "Precursor Logistics", "The Blood Avocado Model", "The Human Smuggling Tariff", "Trade-Based Money Laundering", "Zoonotic Spillover Economics"]

# Master List
tasks = [
    (pillars["1_Exoplanetary_Agriculture"], generate_titles(space_hero, space_keywords), "Exoplanetary Agriculture"),
    (pillars["2_Climate_Finance"], generate_titles(climate_hero, climate_keywords), "Climate Finance"),
    (pillars["3_Biosecurity_Illicit_Economies"], generate_titles(bio_hero, bio_keywords), "Biosecurity & Illicit Economies")
]

print("--- 🟢 STARTING AI GENERATION V2 (Expanded Vocabulary) ---")

total_count = 0
for folder, titles, category in tasks:
    print(f"\nProcessing Category: {category}...")
    
    for title in titles:
        safe_filename = title.replace(" ", "_").replace("-", "_").replace(":", "").replace("__", "_") + ".md"
        # Truncate filename if too long to prevent OS errors
        if len(safe_filename) > 200: safe_filename = safe_filename[:195] + ".md"
        
        file_path = f"{folder}/{safe_filename}"
        
        # Skip if already exists (allows resuming)
        if os.path.exists(file_path):
            print(f"  [Skip] {title} exists.")
            continue
            
        print(f"  [Generating] {title}...")
        
        content = generate_article_content(title, category)
        if content:
            full_text = f"# {title}\n**Category:** {category} | **Read Time:** 10-12 min\n\n" + content
            with open(file_path, "w") as f:
                f.write(full_text)
            generate_chart(folder, title)
            total_count += 1
            # Sleep 1s to be nice to API
            time.sleep(1) 
        
print(f"\n✅ COMPLETE. Generated {total_count} unique articles.")
