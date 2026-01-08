import os

print("--- Setting up PhD Portfolio (Final Vision) ---")

# The 3 New Pillars (Folder Names)
topics = [
    "1_Exoplanetary_Agriculture",      # Martian Ag
    "2_Climate_Finance",               # Weather & Money
    "3_Biosecurity_Illicit_Economies"  # Risky Crops/Crime
]

base_dir = "research_articles"

# Create folders
for topic in topics:
    path = os.path.join(base_dir, topic)
    if not os.path.exists(path):
        os.makedirs(path)
        os.makedirs(os.path.join(path, "images"), exist_ok=True)
        print(f"Created pillar: {topic}")
        
        # Create a sample note in each
        with open(f"{path}/00_Intro.md", "w") as f:
            f.write(f"# Research Focus: {topic.replace('_', ' ')}\n")
            f.write("This section explores the intersection of systems, economics, and security.\n")

print("--- SUCCESS: New Structure Ready ---")
