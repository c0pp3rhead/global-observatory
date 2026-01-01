import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
import time

print("--- Starting Underworld Asset Tracker (Deep Scan Mode) ---")

# 1. Get List of Groups
URL = "https://en.wikipedia.org/wiki/List_of_criminal_enterprises,_gangs,_and_syndicates"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}

groups_to_scan = []
try:
    res = requests.get(URL, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    content = soup.find('div', {'id': 'bodyContent'})
    
    BANNED = ["list of", "gangs", "mafias", "syndicates", "crime in", "organized crime"]
    
    count = 0
    if content:
        for link in content.find_all('a'):
            href = link.get('href')
            text = link.get_text(strip=True)
            if not text: continue
            
            if href and href.startswith('/wiki/') and count < 80:
                if len(text) > 2 and text[0].isupper() and not any(b in text.lower() for b in BANNED):
                    keywords = ['cartel', 'mafia', 'triad', 'syndicate', 'gang', 'family', 'clan', 'posse', 'yakuza', 'outfit', 'bratva']
                    if any(k in text.lower() for k in keywords):
                        groups_to_scan.append({"Group Name": text, "Wiki_Link": "https://en.wikipedia.org" + href})
                        count += 1
except: pass

print(f"Targeting {len(groups_to_scan)} groups for asset recovery analysis...")

seizure_events = []

# 2. Deep Dive for Seizure Data
for group in groups_to_scan:
    try:
        print(f"   > Auditing: {group['Group Name']}...")
        g_res = requests.get(group['Wiki_Link'], headers=headers)
        g_soup = BeautifulSoup(g_res.text, 'html.parser')
        
        # FIX: Scan both Paragraphs (<p>) AND Lists (<li>)
        content_items = g_soup.select('div.mw-parser-output p, div.mw-parser-output li')
        
        for item in content_items:
            text = item.get_text().strip()
            if len(text) < 20: continue # Skip short fragments
            
            # BROADENED KEYWORDS
            triggers = ['seized', 'confiscated', 'recovered', 'captured', 'intercepted', 'raid', 'bust', 'found']
            if any(x in text.lower() for x in triggers):
                
                # RELAXED REGEX (Catches more variations)
                # Money: $100m, $100 million, $50,000
                money = re.search(r'\$[\d,.]+\s*(?:billion|million|bn|m|k|thousand)?', text, re.IGNORECASE)
                
                # Drugs: 10 tonnes, 50kg, 1000 pounds
                drugs = re.search(r'[\d,.]+\s*(?:tonnes?|tons?|kg|kilos?|kilograms?|lbs?|pounds?)\s+(?:of\s+)?(?:cocaine|heroin|meth|fentanyl|marijuana|cannabis|drugs|narcotics)', text, re.IGNORECASE)
                
                # Weapons: 50 guns, 100 rifles
                weapons = re.search(r'\d+(?:,\d+)?\s*(?:guns|rifles|firearms|weapons|pistols|assault rifles)', text, re.IGNORECASE)
                
                # Year extraction
                year_match = re.search(r'\b(19|20)\d{2}\b', text)
                year = year_match.group(0) if year_match else "Unknown"
                
                # Log if ANY asset is found
                if money or drugs or weapons:
                    assets_found = []
                    if money: assets_found.append(f"💰 {money.group(0)}")
                    if drugs: assets_found.append(f"💊 {drugs.group(0)}")
                    if weapons: assets_found.append(f"🔫 {weapons.group(0)}")
                    
                    if assets_found:
                        seizure_events.append({
                            "Group": group['Group Name'],
                            "Year": year,
                            "Seized Assets": " | ".join(assets_found),
                            "Full Description": text[:300].strip(),
                            "Source_Link": group['Wiki_Link']
                        })
        time.sleep(0.1) # Respectful scraping
    except: pass

# 3. Save
df = pd.DataFrame(seizure_events)
if not df.empty:
    # Deduplicate based on description
    df = df.drop_duplicates(subset=['Full Description'])
    df.to_csv("seizure_log.csv", index=False)
    print(f"--- SUCCESS: Logged {len(df)} Asset Seizure Events ---")
    print(df[['Group', 'Seized Assets']].head())
else:
    print("No seizures found. (Check internet connection or Wiki structure)")
