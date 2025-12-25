import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import re

print("--- Starting Underworld Deep Dive (Aggressive Mode) ---")

URL = "https://en.wikipedia.org/wiki/List_of_criminal_enterprises,_gangs,_and_syndicates"
headers = {'User-Agent': 'Mozilla/5.0'}

try:
    res = requests.get(URL, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    groups_to_scan = []
    content = soup.find('div', {'id': 'bodyContent'})
    
    # BANNED TERMS
    BANNED = ["list of", "gangs", "mafias", "syndicates", "crime in", "organized crime"]
    
    count = 0
    if content:
        for link in content.find_all('a'):
            href = link.get('href')
            text = link.get_text(strip=True)
            
            if not text: continue
            
            # Simple Filter: Must be a Wiki link, Capitalized, and not banned
            if href and href.startswith('/wiki/') and count < 65:
                if len(text) > 2 and text[0].isupper() and not any(b in text.lower() for b in BANNED):
                    
                    # Must look like a group name
                    keywords = ['cartel', 'mafia', 'triad', 'syndicate', 'gang', 'family', 'brotherhood', 'clan', 'posse', 'yakuza']
                    if any(k in text.lower() for k in keywords):
                        groups_to_scan.append({"Group Name": text, "Wiki_Link": "https://en.wikipedia.org" + href})
                        count += 1

    print(f"Found {len(groups_to_scan)} targets. Extracting dossiers...")
    detailed_data = []

    for group in groups_to_scan:
        print(f"   > Scanning: {group['Group Name']}...")
        try:
            g_res = requests.get(group['Wiki_Link'], headers=headers)
            g_soup = BeautifulSoup(g_res.text, 'html.parser')
            infobox = g_soup.find('table', {'class': 'infobox'})
            
            # Defaults
            row_data = {
                "Group Name": group['Group Name'], 
                "Wiki_Link": group['Wiki_Link'],
                "Est. Revenue": "Unknown", "Membership": "Unknown", "Founded": "Unknown", "Criminal Activities": "Unknown"
            }
            
            if infobox:
                for row in infobox.find_all('tr'):
                    if row.find('th') and row.find('td'):
                        head = row.find('th').text.lower()
                        val = row.find('td').text.strip().split('[')[0] # Clean [1]
                        
                        # Aggressive Matching
                        if any(x in head for x in ["revenue", "income", "profit", "budget", "turnover"]): 
                            row_data["Est. Revenue"] = val
                        
                        if any(x in head for x in ["membership", "members", "size", "manpower", "employees", "strength"]): 
                            row_data["Membership"] = val
                            
                        if any(x in head for x in ["founded", "formed", "established", "start"]): 
                            row_data["Founded"] = val

                        if any(x in head for x in ["activities", "acts", "specialty"]): 
                            row_data["Criminal Activities"] = val[:100] + "..."

            detailed_data.append(row_data)
            time.sleep(0.2)
        except: pass

    df = pd.DataFrame(detailed_data)
    df.to_csv("underworld_rich_data.csv", index=False)
    print("--- SUCCESS: Aggressive Dossier Extraction Complete ---")

except Exception as e:
    print(f"Critical Error: {e}")
