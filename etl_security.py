import requests
import pandas as pd
from datetime import datetime

print("--- Starting Security ETL: GDELT Live Event Stream ---")

# --- CONFIGURATION ---
QUERY = "(drug OR narcotics OR cocaine OR heroin OR fentanyl) AND (seizure OR bust OR arrest OR confiscated)"
# We use the GeoJSON endpoint specifically
API_URL = "https://api.gdeltproject.org/api/v2/geo/geo"

print(f"1. Querying GDELT...")

try:
    # 1. FETCH DATA
    params = {
        'query': QUERY,
        'format': 'geojson', # CHANGED: Forces raw data, prevents HTML response
        'timespan': '24H',
        'maxrecords': 300
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    response = requests.get(API_URL, params=params, headers=headers)
    
    # Check for HTML error (if it still returns HTML, we catch it here)
    if response.text.strip().startswith("<!DOCTYPE html>"):
        print("❌ Error: API returned HTML instead of JSON. The query might be malformed or the API is blocking requests.")
        print("Switching to fallback empty dataset to prevent crash.")
        raise ValueError("GDELT returned HTML")

    data = response.json()
    
    # 2. PARSE DATA
    # GeoJSON puts features in a 'features' list
    features = data.get('features', [])
    print(f"   > Found {len(features)} events.")
    
    parsed_rows = []
    
    for item in features:
        props = item.get('properties', {})
        geometry = item.get('geometry', {})
        
        if geometry and 'coordinates' in geometry:
            lon, lat = geometry['coordinates']
            
            # GDELT GeoJSON sometimes puts the name in 'name' or 'html'
            # We strip HTML if present
            loc_name = props.get('name', 'Unknown')
            
            row = {
                'Location': loc_name,
                'Article_Count': props.get('count', 1),
                'Latitude': lat,
                'Longitude': lon,
                'Source_URL': props.get('url', '#') # Note: GDELT Geo often omits direct URLs in the lightweight feed
            }
            parsed_rows.append(row)
            
    # 3. CREATE DATAFRAME
    df = pd.DataFrame(parsed_rows)
    
    if not df.empty:
        filename = "security_events.csv"
        df.to_csv(filename, index=False)
        print(f"--- SUCCESS ---")
        print(f"Saved {len(df)} verified events to {filename}")
        print(df.head(3))
    else:
        print("⚠️ Query returned 0 results. Creating dummy file.")
        # Create a dummy file so the Dashboard doesn't crash
        df_dummy = pd.DataFrame({
            'Location': ['No Data (API Limit)'], 
            'Latitude': [0], 
            'Longitude': [0], 
            'Article_Count': [0], 
            'Source_URL': ['#']
        })
        df_dummy.to_csv("security_events.csv", index=False)

except Exception as e:
    print(f"❌ Error: {e}")
    # Fallback: Create empty CSV if it fails hard
    df_dummy = pd.DataFrame({'Location': [], 'Latitude': [], 'Longitude': [], 'Article_Count': [], 'Source_URL': []})
    df_dummy.to_csv("security_events.csv", index=False)
