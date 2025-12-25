import pandas as pd
import requests
from bs4 import BeautifulSoup

print("--- Starting Global Terror Monitor Scraper (Map Fix) ---")

YEARS = [2024, 2023]
all_incidents = []

for year in YEARS:
    url = f"https://en.wikipedia.org/wiki/List_of_terrorist_incidents_in_{year}"
    print(f"Scanning: {year}...")
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
                        place = cols[1].text.strip()
                        country = place.split(",")[-1].strip()
                        
                        # --- CLEAN COUNTRY NAMES FOR MAPPING ---
                        country = country.replace("Democratic Republic of the Congo", "DR Congo")
                        country = country.replace("United States", "USA")
                        country = country.replace("State of Palestine", "Palestine")
                        
                        deaths_txt = cols[2].text.strip().split('[')[0]
                        try: deaths = int(deaths_txt)
                        except: deaths = 0
                        
                        # Extract Link
                        link = url
                        if cols[0].find('a'):
                            link = "https://en.wikipedia.org" + cols[0].find('a')['href']

                        if deaths > 0:
                            all_incidents.append({
                                "Date": f"{cols[0].text.strip()}, {year}",
                                "Location": place,
                                "Country": country,
                                "Deaths": deaths,
                                "Perpetrator": cols[3].text.strip(),
                                "Source_Link": link
                            })
    except: pass

df = pd.DataFrame(all_incidents)
df.to_csv("global_terror_log.csv", index=False)
print(f"--- SUCCESS: {len(df)} Incidents Logged for Map ---")
