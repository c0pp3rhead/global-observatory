import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import re

print("--- Starting Underworld Deep Dive (Hybrid Mode) ---")

URL = "https://en.wikipedia.org/wiki/List_of_criminal_enterprises,_gangs,_and_syndicates"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}

# --- MANUAL INTEL OVERRIDE (The "Silver Bullet" for VIPs) ---
# If the scraper fails, these values will be forced.
MANUAL_INTEL = {
    "Sinaloa Cartel": {
        "Est. Revenue": "$3 Billion - $39 Billion",
        "Membership": "100,000+ (est)",
        "Founded": "1987",
        "Criminal Activities": "International drug trafficking, money laundering, kidnapping"
    },
    "Jalisco New Generation Cartel": {
        "Est. Revenue": "$20 Billion+",
        "Membership": "18,800 - 20,000",
        "Founded": "2009",
        "Criminal Activities": "Drug trafficking, arms trafficking, fuel theft"
    },
    "Medellín Cartel": {
        "Est. Revenue": "$30 Billion (peak)",
        "Membership": "70,000+",
        "Founded": "1976",
        "Criminal Activities": "Drug trafficking, narcoterrorism"
    },
    "Gulf Cartel": {
        "Est. Revenue": "Unknown",
        "Membership": "50,000 - 100,000",
        "Founded": "1930s",
        "Criminal Activities": "Drug trafficking, racketeering"
    },
    "Yamaguchi-gumi": { # Largest Yakuza
        "Est. Revenue": "$6 Billion+",
        "Membership": "8,900",
        "Founded": "1915",
        "Criminal Activities": "Extortion, gambling, arms trafficking"
    },
    "Solntsevskaya Bratva": { # Russian Mafia
        "Est. Revenue": "$8.5 Billion",
        "Membership": "5,000 - 9,000",
        "Founded": "1980s",
        "Criminal Activities": "Racketeering, fraud, drug trafficking"
    }
}

try:
    res = requests.get(URL, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    groups_to_scan = []
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

    print(f"Found {len(groups_to_scan)} targets. Extracting & Applying Overrides...")
    detailed_data = []

    for group in groups_to_scan:
        name = group['Group Name']
        
        # 1. Check for Manual Override FIRST
        if name in MANUAL_INTEL:
            print(f"   > [OVERRIDE] Applying fixed data for: {name}")
            data = MANUAL_INTEL[name]
            detailed_data.append({
                "Group Name": name,
                "Wiki_Link": group['Wiki_Link'],
                "Est. Revenue": data["Est. Revenue"],
                "Membership": data["Membership"],
                "Founded": data["Founded"],
                "Criminal Activities": data["Criminal Activities"]
            })
            continue # Skip scraping for this one

        # 2. Proceed with Scraping for others
        print(f"   > Scanning: {name}...")
        try:
            g_res = requests.get(group['Wiki_Link'], headers=headers)
            g_soup = BeautifulSoup(g_res.text, 'html.parser')
            
            # Infobox Search
            infobox = g_soup.find('table', {'class': 'infobox'})
            revenue, membership, founded, activities = "Unknown", "Unknown", "Unknown", "Unknown"
            
            if infobox:
                for row in infobox.find_all('tr'):
                    if row.find('th') and row.find('td'):
                        head = row.find('th').text.lower()
                        val = row.find('td').text.strip().split('[')[0]
                        if any(x in head for x in ["revenue", "income", "profit"]): revenue = val
                        if any(x in head for x in ["membership", "members", "manpower", "strength"]): membership = val
                        if any(x in head for x in ["founded", "formed", "start"]): founded = val
                        if any(x in head for x in ["activities", "acts", "specialty"]): activities = val[:100] + "..."

            # Body Text Fallback
            if revenue == "Unknown" or membership == "Unknown":
                body_text = ""
                paragraphs = g_soup.select('div.mw-parser-output > p')
                for p in paragraphs[:3]: body_text += p.get_text() + " "
                
                if revenue == "Unknown":
                    m = re.search(r'\$(\d+(?:\.\d+)?\s+(?:billion|million))', body_text, re.IGNORECASE)
                    if m: revenue = m.group(0)
                if membership == "Unknown":
                    m = re.search(r'(\d+(?:,\d+)?\s+(?:members|associates))', body_text, re.IGNORECASE)
                    if m: membership = m.group(0)
                if founded == "Unknown":
                    m = re.search(r'(?:founded|formed|established)\s+in\s+(\d{4})', body_text, re.IGNORECASE)
                    if m: founded = m.group(1)

            detailed_data.append({
                "Group Name": name,
                "Wiki_Link": group['Wiki_Link'],
                "Est. Revenue": revenue,
                "Membership": membership,
                "Founded": founded,
                "Criminal Activities": activities
            })
            time.sleep(0.1)
        except: pass

    # Save and Sort
    df = pd.DataFrame(detailed_data)
    # Sort to ensure groups with data appear first
    df['HasData'] = df['Membership'].apply(lambda x: 0 if str(x) == 'Unknown' else 1)
    df = df.sort_values('HasData', ascending=False).drop('HasData', axis=1)
    
    df.to_csv("underworld_rich_data.csv", index=False)
    print("--- SUCCESS: Hybrid Dataset Created ---")

except Exception as e:
    print(f"Critical Error: {e}")
