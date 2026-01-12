import matplotlib.pyplot as plt
import numpy as np
import os
import random

# Ensure directory exists
output_dir = "research_articles/1_Exoplanetary_Agriculture/images"
os.makedirs(output_dir, exist_ok=True)

# --- 90 NEW TITLES ---
titles = [
    # STAPLE CROPS
    "The Potato Paradox", "Hypobaric Quinoa", "Duckweed Radiation Shields", "Sweet Potato",
    "Oil Pressing in Microgravity", "Wheat Dwarfism", "Aeroponic Rice", "Peanut Allergens",
    "Structural Bamboo", "Moringa",
    # PROTEIN
    "Mealworms and Styrofoam", "Black Soldier Fly", "Microgravity Aquaponics", "Shrimp Shell Formation",
    "Myco-Shielding", "Yeast Vats", "Cellular Agriculture", "Silkworm Textiles",
    "Escargot Snails", "Bacterial Cellulose",
    # WATER & WASTE
    "Greywater Surfactants", "Urine Electrolysis", "Transpiration Capture", "Aeroponic Clogging",
    "Fogponics", "Biochar Pyrolysis", "Methane Digesters", "Fecal Compaction",
    "Sweat Salt Recovery", "Pharma-Filtration",
    # REGOLITH
    "Simulant MGS-1", "Clay Swelling", "Zeolite Synthesis", "Microwave Sintering",
    "Magnetic Separation", "Sulfate Reduction", "Perchlorate Byproducts", "Synthetic Soil Crusts",
    "Geophagous Worms", "Nitrogen Fixation",
    # LIGHTING
    "Monochromatic Defects", "Martian Sol Adaptation", "Far-Red Triggers", "UV-B Upregulation",
    "Fiber Optic Collection", "Thermal Rejection", "Inter-Canopy LEDs", "Pulsed Light",
    "Gamma Radiation Shielding", "Solar Storm Protocol",
    # ATMOSPHERE
    "Ethylene Scrubbing", "CO2 Toxicity", "High-O2 Fire Risks", "Terpene Accumulation",
    "Vapor Pressure Deficit", "Hypobaric Physiology", "Dust Filtration", "Off-Gassing",
    "Thigmomorphogenesis", "Argon Buffering",
    # ROBOTICS
    "Seedling Robots", "Soft Robotics", "Root Tomography", "Ion-Selective Electrodes",
    "IR Stress Detection", "Micro-Drone Mixing", "3D Printed Tools", "Hyperspectral Imaging",
    "Fail-Safe Logic", "Telemetry Compression",
    # PHARMACY
    "Analgesic Poppies", "Aloe Vera", "Willow Bark", "Stevia", "Enzymatic Caffeine",
    "Molecular Farming", "Space Brewing", "Olfactory Stimulation", "Dandelion Latex", "Industrial Hemp",
    # EXTREME ENVIRONMENTS (The Sci-Fi Set)
    "Lava Tube Farming", "Ice Cap Agriculture", "Dust Storm Resilience", "Micrometeorite Punctures",
    "Planetary Protection", "Seed Vaults", "Grafting Techniques", "Polyculture Guilds",
    "Nematodes", "The Salad Machine"
]

plt.style.use('dark_background')

print(f"--- 📊 Generating {len(titles)} Charts ---")

for title in titles:
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Randomly select chart type to create variety
    chart_type = random.choice(['line', 'scatter', 'bar', 'area'])
    x = np.arange(20)
    
    if chart_type == 'line':
        y1 = np.sort(np.random.uniform(10, 90, 20)) # Rising trend
        y2 = np.sort(np.random.uniform(10, 90, 20)) * 0.8
        ax.plot(x, y1, color='#2ecc71', linewidth=3, label='Experimental')
        ax.plot(x, y2, color='#e74c3c', linestyle='--', label='Control')
        ax.fill_between(x, y1, y2, alpha=0.1, color='#2ecc71')
        
    elif chart_type == 'scatter':
        x_s = np.random.normal(50, 15, 50)
        y_s = x_s * 1.2 + np.random.normal(0, 10, 50)
        ax.scatter(x_s, y_s, color='#3498db', alpha=0.7)
        
    elif chart_type == 'bar':
        y = np.random.uniform(20, 100, 20)
        ax.bar(x, y, color='#9b59b6', alpha=0.8)
        
    elif chart_type == 'area':
        y = np.linspace(100, 50, 20) + np.random.normal(0, 5, 20)
        ax.fill_between(x, y, 0, color='#f1c40f', alpha=0.3)
        ax.plot(x, y, color='#f1c40f', linewidth=2)

    # Clean filename
    filename = title.lower().replace(" ", "_").replace("-", "_") + ".png"
    
    ax.set_title(f"Data Analysis: {title}", fontsize=14, color='white', pad=20)
    ax.legend(loc='upper left')
    ax.grid(axis='both', linestyle='--', alpha=0.1)
    ax.set_ylabel("Normalized Metric (Index)", fontsize=12)
    
    save_path = f"{output_dir}/{filename}"
    plt.savefig(save_path, dpi=100, bbox_inches='tight')
    plt.close()
    print(f"Generated: {filename}")

print("--- ✅ Charts Complete ---")
