import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import re

print("--- Starting Underworld Deep Dive (Clean Filter) ---")

# 1. Scrape the Master List
URL = "https://en.wikipedia.org/wiki/List_of_criminal_enterprises,_gangs,_and_syndicates"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}

try:
    res = requests.get(URL, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    groups_to_scan = []
    content = soup.find('div', {'id': 'bodyContent'})
    
    # BANNED TERMS (Generic pages to skip)
    BANNED = ["list of", "gangs", "mafias", "syndicates", "crime in", "organized crime", "cartel", "triad", "mafia"]
    
    count = 0
    if content:
        for link in content.find_all('a'):
            href = link.get('href')
            text = link.get_text(strip=True)
            
            # --- SAFETY CHECK: Skip empty text ---
            if not text: continue

            if href and href.startswith('/wiki/') and count < 60:
                # Check if it looks like a real group name
                
                # 1. Must be capitalized (Real names are Proper Nouns)
                # We use safe access here just in case
                if len(text) > 0 and not text[0].isupper(): continue
                
                # 2. Must not be a generic "List of" page
                if any(b in text.lower() for b in ["list of", "crime in"]): continue
                
                # 3. Must not be just a generic word like "Gangs"
                if text.lower() in BANNED: continue
                
                # 4. Keyword Check (Must sound like a group)
                keywords = ['cartel', 'mafia', 'triad', 'syndicate', 'gang', 'family', 'brotherhood', 'organization', 'clan', 'posse']
                if any(k in text.lower() for k in keywords):
                    groups_to_scan.append({
                        "Group Name": text,
                        "Wiki_Link": "https://en.wikipedia.org" + href
                    })
                    count += 1
                
    print(f"Found {len(groups_to_scan)} VALID targets. Extracting dossiers...")

    detailed_data = []

    # 2. Visit each page
    for group in groups_to_scan:
        print(f"   > Analyzing: {group['Group Name']}...")
        try:
            g_res = requests.get(group['Wiki_Link'], headers=headers)
            g_soup = BeautifulSoup(g_res.text, 'html.parser')
            infobox = g_soup.find('table', {'class': 'infobox'})
            
            # Defaults
            activities = "Unknown"
            revenue = "Unknown"
            membership = "Unknown"
            founded = "Unknown"
            
            if infobox:
                for row in infobox.find_all('tr'):
                    if row.find('th') and row.find('td'):
                        head = row.find('th').text.lower()
                        val = row.find('td').text.strip().split('[')[0]
                        
                        if any(x in head for x in ["activities", "acts", "specialty"]): activities = val[:120] + "..."
                        if any(x in head for x in ["revenue", "income", "profit"]): revenue = val
                        if any(x in head for x in ["membership", "members", "size", "manpower"]): membership = val
                        if "founded" in head: founded = val

            detailed_data.append({
                "Group Name": group['Group Name'],
                "Wiki_Link": group['Wiki_Link'],
                "Criminal Activities": activities,
                "Est. Revenue": revenue,
                "Membership": membership,
                "Founded": founded
            })
            time.sleep(0.3)
            
        except: pass

    # Save
    if detailed_data:
        df = pd.DataFrame(detailed_data)
        df.to_csv("underworld_rich_data.csv", index=False)
        print("--- SUCCESS: Clean Dossiers Updated ---")
        print(df[['Group Name', 'Membership']].head())
    else:
        print("Warning: No dossiers extracted.")

except Exception as e:
    print(f"Critical Error: {e}")
