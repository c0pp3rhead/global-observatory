import pandas as pd
import requests

print("--- Starting Bio-Radar Historical ETL ---")

def get_wb_data(indicator, col_name):
    # Fetching 15 years of data
    url = f"http://api.worldbank.org/v2/country/all/indicator/{indicator}?format=json&per_page=10000&date=2010:2023"
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
        return pd.DataFrame(data)
    except:
        return pd.DataFrame()

# 1. Fetch Datasets
print("Fetching Suicide Rates (Historical)...")
df_suicide = get_wb_data("SH.STA.SUIC.P5", "Suicide_Rate_100k")

print("Fetching HIV Prevalence (Historical)...")
df_hiv = get_wb_data("SH.DYN.AIDS.ZS", "AIDS_Prevalence_Pct")

# 2. Merge on Country + Year
print("Merging Historical Data...")
if not df_suicide.empty:
    df_final = df_suicide
    if not df_hiv.empty:
        df_final = pd.merge(df_final, df_hiv[['iso_code', 'Year', 'AIDS_Prevalence_Pct']], 
                            on=['iso_code', 'Year'], how='outer')
    
    # Fill Country names if lost during merge
    df_final['Country'] = df_final['Country'].fillna("Unknown")
    
    # Save
    df_final.to_csv("health_unified.csv", index=False)
    print("--- SUCCESS: Saved Historical Health Data ---")
    print(df_final.head())
else:
    print("Error: No data fetched.")
