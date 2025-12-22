import requests
import pandas as pd
from bs4 import BeautifulSoup

print("--- Starting Underworld Atlas Scraper (Smart Filter) ---")
URL = "https://en.wikipedia.org/wiki/List_of_criminal_enterprises,_gangs,_and_syndicates"

try:
    res = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(res.text, 'html.parser')
    
    all_groups = []
    current_region = "International"
    
    # Define "Banned" keywords that appear in navigation menus
    BANNED_TERMS = ["Main Page", "Contents", "Current events", "Random article", 
                    "About Wikipedia", "Contact us", "Donate", "Help", "Log in", 
                    "Create account", "Contributions", "Upload file", "Special:", 
                    "Wikipedia:", "Portal:", "Talk", "Template", "Category"]

    for element in soup.find_all(['h2', 'li']):
        # Detect Region Header
        if element.name == 'h2':
            text = element.text.strip().replace('[edit]', '')
            if text in ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']:
                current_region = text
                print(f"Scanning {current_region}...")
        
        # Detect List Items
        elif element.name == 'li':
            link = element.find('a')
            if link and link.get('href'):
                text = link.text
                href = link.get('href')
                
                # SMART FILTER: Only add if it's NOT a navigation link
                if not any(banned in text for banned in BANNED_TERMS) and \
                   not any(banned in href for banned in BANNED_TERMS) and \
                   len(text) > 3:
                    
                    full_link = "https://en.wikipedia.org" + href
                    all_groups.append({
                        "Region": current_region,
                        "Group Name": text,
                        "Wiki_Link": full_link,
                        "Status": "Active" # Default
                    })
    
    # Save
    if len(all_groups) > 0:
        df = pd.DataFrame(all_groups)
        # Remove duplicates
        df = df.drop_duplicates(subset=['Group Name'])
        # Limit to 300 for speed/demo
        df = df.head(300) 
        df.to_csv("underworld_atlas.csv", index=False)
        print(f"--- SUCCESS: Found {len(df)} VALID organizations ---")
        print(df[['Group Name', 'Region']].head())
    else:
        print("Warning: No groups found.")
    
except Exception as e:
    print(f"Critical Error: {e}")
