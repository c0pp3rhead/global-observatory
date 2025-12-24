import pandas as pd
import requests
from bs4 import BeautifulSoup

print("--- Starting Global Terror Monitor Scraper ---")

# We target the yearly lists
YEARS = [2024, 2023]
all_incidents = []

for year in YEARS:
    url = f"https://en.wikipedia.org/wiki/List_of_terrorist_incidents_in_{year}"
    print(f"Scanning Security Logs: {year}...")
    
    try:
        res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(res.text, 'html.parser')
        
        # Wiki stores these in tables class="wikitable"
        tables = soup.find_all('table', {'class': 'wikitable'})
        
        for table in tables:
            # Check headers to ensure it's an incident table
            headers = [th.text.strip().lower() for th in table.find_all('th')]
            if 'date' in headers and 'location' in headers:
                
                rows = table.find_all('tr')
                for row in rows[1:]: # Skip header
                    cols = row.find_all('td')
                    if len(cols) >= 4:
                        date = cols[0].text.strip()
                        place = cols[1].text.strip()
                        
                        # Deaths often have citations like "12[3]"
                        deaths_txt = cols[2].text.strip().split('[')[0]
                        # Try to force int
                        try: deaths = int(deaths_txt)
                        except: deaths = 0
                        
                        perpetrator = cols[3].text.strip()
                        
                        # Add Year to date for visualization
                        full_date = f"{date}, {year}"
                        
                        all_incidents.append({
                            "Date": full_date,
                            "Location": place,
                            "Deaths": deaths,
                            "Perpetrator": perpetrator,
                            "Year": year
                        })
                        
    except Exception as e:
        print(f"Error scanning {year}: {e}")

# Save
df = pd.DataFrame(all_incidents)
# Filter for significant events (Deaths > 0)
df = df[df['Deaths'] > 0]
df.to_csv("global_terror_log.csv", index=False)
print(f"--- SUCCESS: Logged {len(df)} Verified Terrorist Incidents ---")
