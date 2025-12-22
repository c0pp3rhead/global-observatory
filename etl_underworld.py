import requests
import pandas as pd
from bs4 import BeautifulSoup
import re

print("--- Starting Underworld Atlas Scraper (Browser Mode) ---")
URL = "https://en.wikipedia.org/wiki/List_of_criminal_enterprises,_gangs,_and_syndicates"

try:
    # 1. Use a Real Browser Header (Prevents blocks/mobile views)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    }
    res = requests.get(URL, headers=headers)
    print(f"DEBUG: Status Code: {res.status_code}") # Should be 200

    soup = BeautifulSoup(res.text, 'html.parser')
    
    # 2. Target the main content ID (More stable than class names)
    content = soup.find('div', {'id': 'bodyContent'})
    if not content:
        print("Fallback: Scanning entire body tag...")
        content = soup.body

    all_groups = []
    current_region = "Global" 
    
    # 3. Iterate
    for element in content.find_all(['h2', 'li']):
        
        # --- HEADER DETECTION ---
        if element.name == 'h2':
            text = element.get_text(strip=True).replace('[edit]', '').lower()
            
            # Update Region
            if 'africa' in text: current_region = "Africa"
            elif 'asia' in text: current_region = "Asia"
            elif 'europe' in text: current_region = "Europe"
            elif 'north america' in text: current_region = "North America"
            elif 'south america' in text: current_region = "South America"
            elif 'oceania' in text: current_region = "Oceania"

        # --- LIST ITEM DETECTION ---
        elif element.name == 'li':
            link = element.find('a')
            if link and link.get('href'):
                text = link.get_text(strip=True)
                href = link.get('href')
                
                # --- FILTERS ---
                if not href.startswith('/wiki/'): continue
                if len(text) < 3: continue
                
                # Banned terms (Navigation garbage)
                banned = ["list of", "gangs in", "crime in", "edit", "template", 
                          "category", "portal", "timeline", "main page", "help", "contact"]
                if any(b in text.lower() for b in banned): continue
                
                all_groups.append({
                    "Region": current_region,
                    "Group Name": text,
                    "Wiki_Link": "https://en.wikipedia.org" + href,
                    "Status": "Active"
                })

    # Save
    if len(all_groups) > 0:
        df = pd.DataFrame(all_groups)
        df = df.drop_duplicates(subset=['Group Name'])
        # Limit to 300
        df = df.head(300)
        df.to_csv("underworld_atlas.csv", index=False)
        print(f"--- SUCCESS: Found {len(df)} organizations ---")
        print(df['Region'].value_counts())
    else:
        print("FAILED. No data found.")

except Exception as e:
    print(f"Critical Error: {e}")
