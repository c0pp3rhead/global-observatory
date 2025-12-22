import requests
import pandas as pd
from bs4 import BeautifulSoup

print("--- Starting Underworld Atlas Scraper ---")
URL = "https://en.wikipedia.org/wiki/List_of_criminal_enterprises,_gangs,_and_syndicates"

try:
    res = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(res.text, 'html.parser')
    
    all_groups = []
    current_region = "International"
    
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
            # SAFETY CHECK: Only proceed if link exists AND has an 'href'
            if link and link.get('href'):
                # Exclude garbage links (citations, small text)
                if "cite" not in link.text and len(link.text) > 3:
                    full_link = "https://en.wikipedia.org" + link.get('href')
                    all_groups.append({
                        "Region": current_region,
                        "Group Name": link.text,
                        "Wiki_Link": full_link,
                        "Status": "Active" # Default
                    })
    
    # Save
    if len(all_groups) > 0:
        df = pd.DataFrame(all_groups)
        # Limit to 300 to keep file size small for demo
        df = df.head(300) 
        df.to_csv("underworld_atlas.csv", index=False)
        print(f"--- SUCCESS: Found {len(df)} organizations ---")
        print(df.head())
    else:
        print("Warning: No groups found. Check Wikipedia layout.")
    
except Exception as e:
    print(f"Critical Error: {e}")
