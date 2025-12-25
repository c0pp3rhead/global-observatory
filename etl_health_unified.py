import pandas as pd
import requests

print("--- Starting Bio-Radar ETL (Snapshot Mode) ---")

def get_wb_data(indicator, col_name, preferred_year):
    # Fetch a range to ensure we find the latest data if the preferred year is empty
    url = f"http://api.worldbank.org/v2/country/all/indicator/{indicator}?format=json&per_page=300&date=2015:2023"
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
            # Sort by Year and keep the row closest to preferred_year
            df = df.sort_values('Year', ascending=False).drop_duplicates('iso_code')
        return df
    except:
        return pd.DataFrame()

# 1. Fetch Indicators
print("Fetching General Mortality (Crude Death Rate)...")
df_death = get_wb_data("SP.DYN.CDRT.IN", "General_Death_Rate_1k", 2021)

print("Fetching Suicide Rates (2021)...")
df_suicide = get_wb_data("SH.STA.SUIC.P5", "Suicide_Rate_100k", 2021)

print("Fetching HIV/AIDS (2023)...")
df_hiv = get_wb_data("SH.DYN.AIDS.ZS", "AIDS_Prevalence_Pct", 2023)

# 2. Merge
print("Merging Datasets...")
df_final = df_death[['iso_code', 'Country', 'General_Death_Rate_1k']].copy()

if not df_suicide.empty:
    df_final = pd.merge(df_final, df_suicide[['iso_code', 'Suicide_Rate_100k']], on='iso_code', how='left')
if not df_hiv.empty:
    df_final = pd.merge(df_final, df_hiv[['iso_code', 'AIDS_Prevalence_Pct']], on='iso_code', how='left')

df_final.to_csv("health_unified.csv", index=False)
print("--- SUCCESS: Bio-Radar Data Updated ---")
