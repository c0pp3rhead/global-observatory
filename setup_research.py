import os

print("--- Setting up Research Archive Architecture ---")

# 1. Define the 6 PhD Pillars
structure = {
    "1_Environmental_Economics": "Commodity prices, weather patterns, and resource scarcity.",
    "2_Public_Health_Demography": "Mortality trends, pandemics, and social determinants of health.",
    "3_Conflict_Studies_Geopolitics": "Civil unrest, war, and news volume intensity.",
    "4_Political_Communication": "Media bias, sentiment analysis, and agenda setting.",
    "5_Criminology_Illicit_Finance": "Organized crime structures and asset seizure analysis.",
    "6_Global_Security_Studies": "Terrorism, asymmetric warfare, and threat monitoring."
}

# 2. Create Folders
base_dir = "research_articles"
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

for folder, desc in structure.items():
    path = os.path.join(base_dir, folder)
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created pillar: {folder}")

# 3. Create a Dummy Article (So you see how it works)
sample_article = """
# The El Niño Effect: Correlating 2024 Coffee Futures
**Date:** Jan 1, 2026 | **Author:** Cristian Morales

## Abstract
This research note explores the correlation between rolling 30-day rainfall averages in Vietnam and the spike in Robusta futures traded on the ICE.

## Initial Findings
Data gathered via the *Global Observatory* indicates a -0.8 correlation between precipitation levels in the Central Highlands and monthly price volatility.

### Key Data Points
* **Rainfall Deficit:** 120mm below average
* **Price Impact:** +15% YTD

## Conclusion
Climate volatility is becoming the primary driver of soft commodity inflation, outpacing traditional supply chain metrics.
"""

# Save dummy article in Pillar 1
with open(f"{base_dir}/1_Environmental_Economics/sample_note.md", "w") as f:
    f.write(sample_article)

print("--- SUCCESS: Research Repository Ready ---")
print("You can now drop .md text files into the 'research_articles' folders.")
