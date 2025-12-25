import pandas as pd
import requests

print("--- Starting Bio-Radar ETL (Gap-Filling Mode) ---")

def get_wb_data_latest(indicator, col_name):
    # Fetch 10 years of data to ensure coverage
    url = f"http://api.worldbank.org/v2/country/all/indicator/{indicator}?format=json&per_page=10000&date=2014:2024"
    try:
        resp = requests.get(url).json()
        data = []
        if len(resp) > 1:
            for item in resp[1]:
                if item['value'] is not None:
                    data.append({
                        'iso_code': item['countryiso3code'],
                        'Country': item['country']['value'],
                        'Year': int(item['date']),
                        col_name: item['value']
                    })
        df = pd.DataFrame(data)
        if not df.empty:
            # SORT by Year (descending) and DROP duplicates to keep only the LATEST value
            df = df.sort_values('Year', ascending=False).drop_duplicates('iso_code')
        return df
    except Exception as e:
        print(f"Error fetching {col_name}: {e}")
        return pd.DataFrame()

# 1. Fetch Indicators (Latest Available)
print("Fetching General Mortality...")
df_death = get_wb_data_latest("SP.DYN.CDRT.IN", "General_Death_Rate_1k")

print("Fetching Suicide Rates...")
df_suicide = get_wb_data_latest("SH.STA.SUIC.P5", "Suicide_Rate_100k")

print("Fetching HIV/AIDS...")
df_hiv = get_wb_data_latest("SH.DYN.AIDS.ZS", "AIDS_Prevalence_Pct")

# 2. Merge All on ISO Code
print("Merging Datasets...")
# Start with a base of all countries found in the Death dataset
df_final = df_death[['iso_code', 'Country', 'General_Death_Rate_1k']].copy()

if not df_suicide.empty:
    df_final = pd.merge(df_final, df_suicide[['iso_code', 'Suicide_Rate_100k']], on='iso_code', how='left')
if not df_hiv.empty:
    df_final = pd.merge(df_final, df_hiv[['iso_code', 'AIDS_Prevalence_Pct']], on='iso_code', how='left')

# Fill NaNs with 0 for cleaner mapping (optional, or leave as NaN)
df_final = df_final.fillna(0)

df_final.to_csv("health_unified.csv", index=False)
print(f"--- SUCCESS: Bio-Radar Populated with {len(df_final)} Countries ---")
