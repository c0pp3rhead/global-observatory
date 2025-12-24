import pandas as pd
import requests
from bs4 import BeautifulSoup

print("--- Starting Global Terror Monitor Scraper (Enriched) ---")

YEARS = [2024, 2023]
all_incidents = []

for year in YEARS:
    url = f"https://en.wikipedia.org/wiki/List_of_terrorist_incidents_in_{year}"
    print(f"Scanning Security Logs: {year}...")
    
    try:
        res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(res.text, 'html.parser')
        tables = soup.find_all('table', {'class': 'wikitable'})
        
        for table in tables:
            headers = [th.text.strip().lower() for th in table.find_all('th')]
            if 'date' in headers and 'location' in headers:
                rows = table.find_all('tr')
                for row in rows[1:]:
                    cols = row.find_all('td')
                    if len(cols) >= 4:
                        # 1. Extract Data
                        date = cols[0].text.strip()
                        place = cols[1].text.strip()
                        deaths_txt = cols[2].text.strip().split('[')[0]
                        try: deaths = int(deaths_txt)
                        except: deaths = 0
                        perpetrator = cols[3].text.strip()
                        
                        # 2. Extract Country for Map (Simple split by comma)
                        if "," in place:
                            country = place.split(",")[-1].strip()
                        else:
                            country = place # Fallback
                        
                        # 3. Extract Source Link (from the Date column usually)
                        link = "Unknown"
                        if cols[0].find('a'):
                            link = "https://en.wikipedia.org" + cols[0].find('a')['href']
                        else:
                            link = url # Fallback to main page
                        
                        all_incidents.append({
                            "Date": f"{date}, {year}",
                            "Location": place,
                            "Country": country,
                            "Deaths": deaths,
                            "Perpetrator": perpetrator,
                            "Source_Link": link
                        })
    except Exception as e:
        print(f"Error scanning {year}: {e}")

df = pd.DataFrame(all_incidents)
# Clean up Country names for Map matching
df['Country'] = df['Country'].replace({"United States": "USA", "Democratic Republic of the Congo": "DR Congo"})
df = df[df['Deaths'] > 0]
df.to_csv("global_terror_log.csv", index=False)
print(f"--- SUCCESS: Logged {len(df)} Incidents with Sources ---")
