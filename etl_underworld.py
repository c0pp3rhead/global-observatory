import requests
import pandas as pd
from bs4 import BeautifulSoup
import time

print("--- Starting Underworld Atlas Scraper ---")
URL = "https://en.wikipedia.org/wiki/List_of_criminal_enterprises,_gangs,_and_syndicates"

try:
    res = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(res.text, 'html.parser')

    all_groups = []
    current_region = "International"

    for element in soup.find_all(['h2', 'li']):
        if element.name == 'h2':
            text = element.text.strip().replace('[edit]', '')
            if text in ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']:
                current_region = text
                print(f"Scanning {current_region}...")

        elif element.name == 'li' and element.find('a'):
            link = element.find('a')
            if "cite" not in link.text and len(link.text) > 3:
                all_groups.append({
                    "Region": current_region,
                    "Group Name": link.text,
                    "Wiki_Link": "https://en.wikipedia.org" + link['href'],
                    "Status": "Active" # Default assumption
                })

    df = pd.DataFrame(all_groups)
    # Limit to 300 to prevent crashing the demo
    df = df.head(300) 
    df.to_csv("underworld_atlas.csv", index=False)
    print(f"--- SUCCESS: Found {len(df)} organizations ---")

except Exception as e:
    print(f"Error: {e}")
