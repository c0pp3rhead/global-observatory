import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

print("--- Starting Global Terror Monitor (Smart Column Fix) ---")

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
            # 1. Map Headers to Index (The Smart Part)
            headers = [th.text.strip().lower() for th in table.find_all('th')]
            
            try:
                # Find dynamic column indices
                loc_idx = next(i for i, h in enumerate(headers) if 'location' in h or 'place' in h)
                date_idx = next(i for i, h in enumerate(headers) if 'date' in h)
                
                # Deaths sometimes labeled "Dead", "Fatalities", or "Deaths"
                death_idx = next(i for i, h in enumerate(headers) if any(x in h for x in ['deaths', 'dead', 'fatalities']))
                
            except StopIteration:
                continue # Skip tables that don't match the format

            # 2. Extract Data
            rows = table.find_all('tr')
            for row in rows[1:]:
                cols = row.find_all('td')
                
                if len(cols) > max(loc_idx, death_idx, date_idx):
                    try:
                        # Extract Location & Country
                        place = cols[loc_idx].text.strip()
                        
                        # Logic: Take the last part of the string (City, Country -> Country)
                        if "," in place:
                            country = place.split(",")[-1].strip()
                        else:
                            country = place 
                        
                        # CLEAN COUNTRY NAMES (Critical for Map)
                        country = country.split("[")[0] # Remove footnotes
                        country = country.replace("Democratic Republic of the Congo", "DR Congo")
                        country = country.replace("United States", "USA")
                        country = country.replace("State of Palestine", "Palestine")
                        country = country.replace("Islamic Republic of Iran", "Iran")
                        country = country.replace("Republic of Ireland", "Ireland")

                        # Extract Deaths (Handle "12(+1)" or "Unknown")
                        deaths_txt = cols[death_idx].text.strip().split('[')[0]
                        deaths = 0
                        if deaths_txt.isdigit():
                            deaths = int(deaths_txt)
                        elif '(' in deaths_txt: # Handle "3 (+1 perp)"
                             try: deaths = int(re.search(r'\d+', deaths_txt).group())
                             except: pass
                        
                        # Extract Date
                        date_str = cols[date_idx].text.strip()
                        
                        # Extract Link
                        link = url
                        if cols[date_idx].find('a'):
                            link = "https://en.wikipedia.org" + cols[date_idx].find('a')['href']

                        if deaths > 0:
                            all_incidents.append({
                                "Date": f"{date_str}, {year}",
                                "Location": place,
                                "Country": country,
                                "Deaths": deaths,
                                "Source_Link": link
                            })
                    except: pass

    except Exception as e:
        print(f"Error accessing {year}: {e}")

df = pd.DataFrame(all_incidents)
# Debug: Verify we have real countries now
if not df.empty:
    print("SUCCESS. Countries identified for map:")
    print(df['Country'].unique()[:10]) 

df.to_csv("global_terror_log.csv", index=False)