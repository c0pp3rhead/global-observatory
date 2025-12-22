import pandas as pd
import requests
import io

print("--- Starting Unified Health ETL (Bio-Radar) ---")

# 1. COVID-19 (Source: Our World in Data)
print("1. Fetching COVID-19 Data (OWID)...")
try:
    url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
    # Fetch only necessary columns to save memory
    df_covid = pd.read_csv(url, usecols=['iso_code', 'location', 'date', 'total_deaths_per_million'])
    # Get latest snapshot per country
    df_covid = df_covid.sort_values('date').groupby('iso_code').tail(1)
    df_covid = df_covid.rename(columns={'total_deaths_per_million': 'COVID_Deaths_per_M', 'location': 'Country'})
except Exception as e:
    print(f"   > Error fetching COVID: {e}")
    df_covid = pd.DataFrame()

# 2. WORLD BANK INDICATORS
def get_wb_data(indicator, col_name, year):
    print(f"   > Fetching {col_name}...")
    url = f"http://api.worldbank.org/v2/country/all/indicator/{indicator}?format=json&per_page=300&date={year}"
    try:
        resp = requests.get(url).json()
        data = []
        if len(resp) > 1:
            for item in resp[1]:
                if item['value'] is not None:
                    data.append({'iso_code': item['countryiso3code'], col_name: item['value']})
        return pd.DataFrame(data)
    except:
        return pd.DataFrame()

# Fetch datasets (Using 2019/2021 as standard recent years)
df_suicide = get_wb_data("SH.STA.SUIC.P5", "Suicide_Rate_100k", 2019)
df_aids = get_wb_data("SH.DYN.AIDS.ZS", "AIDS_Prevalence_Pct", 2021)
df_death = get_wb_data("SP.DYN.CDRT.IN", "General_Death_Rate_1k", 2021)

# 3. MERGE EVERYTHING
print("3. Merging Datasets...")
if not df_covid.empty:
    df_final = df_covid[['iso_code', 'Country', 'COVID_Deaths_per_M']].copy()
    df_final = pd.merge(df_final, df_suicide, on='iso_code', how='left')
    df_final = pd.merge(df_final, df_aids, on='iso_code', how='left')
    df_final = pd.merge(df_final, df_death, on='iso_code', how='left')

    # Save
    df_final.to_csv("health_unified.csv", index=False)
    print("--- SUCCESS: Saved 'health_unified.csv' ---")
    print(df_final.head())
else:
    print("❌ Critical Error: Could not fetch base country data.")
