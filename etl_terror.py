import pandas as pd
import requests
from bs4 import BeautifulSoup

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
            
            # We need to find WHICH column number is 'Location' and 'Deaths'
            try:
                # Find index of header containing 'location' or 'place'
                loc_idx = next(i for i, h in enumerate(headers) if 'location' in h or 'place' in h)
                
                # Find index of header containing 'deaths' or 'dead'
                death_idx = next(i for i, h in enumerate(headers) if 'deaths' in h or 'dead' in h or 'fatalities' in h)
                
                # Find index of header containing 'date'
                date_idx = next(i for i, h in enumerate(headers) if 'date' in h)
                
            except StopIteration:
                continue # Skip tables that don't have these columns

            # 2. Extract Data using Smart Indices
            rows = table.find_all('tr')
            for row in rows[1:]:
                cols = row.find_all('td')
                
                # Ensure row has enough columns
                if len(cols) > max(loc_idx, death_idx, date_idx):
                    try:
                        # Extract Location
                        place = cols[loc_idx].text.strip()
                        
                        # Extract Country (Split by comma: "City, Country" -> "Country")
                        if "," in place:
                            country = place.split(",")[-1].strip()
                        else:
                            country = place 
                        
                        # CLEAN COUNTRY NAMES (Critical for Map)
                        country = country.replace("Democratic Republic of the Congo", "DR Congo")
                        country = country.replace("United States", "USA")
                        country = country.replace("State of Palestine", "Palestine")
                        country = country.replace("Islamic Republic of Iran", "Iran")
                        country = country.replace("Republic of Ireland", "Ireland")
                        # Remove footnotes like "Turkey[12]" -> "Turkey"
                        country = country.split("[")[0]

                        # Extract Deaths
                        deaths_txt = cols[death_idx].text.strip().split('[')[0] # Remove [citation]
                        try: 
                            deaths = int(deaths_txt)
                        except: 
                            # Handle "12(+1)" format
                            if '(' in deaths_txt:
                                try: deaths = int(deaths_txt.split('(')[0])
                                except: deaths = 0
                            else:
                                deaths = 0
                        
                        # Extract Date
                        date = cols[date_idx].text.strip()

                        # Link
                        link = url
                        if cols[date_idx].find('a'):
                            link = "https://en.wikipedia.org" + cols[date_idx].find('a')['href']

                        if deaths > 0:
                            all_incidents.append({
                                "Date": f"{date}, {year}",
                                "Location": place,
                                "Country": country,
                                "Deaths": deaths,
                                "Perpetrator": "Unknown", # Optional
                                "Source_Link": link
                            })
                    except Exception as e:
                        pass # Skip bad rows

    except Exception as e:
        print(f"Error accessing {year}: {e}")

df = pd.DataFrame(all_incidents)
# Debug: Show us what countries we found to verify the fix
if not df.empty:
    print("SUCCESS. Countries identified for map:")
    print(df['Country'].unique()[:10]) # Print first 10
else:
    print("WARNING: No data found.")

df.to_csv("global_terror_log.csv", index=False)
