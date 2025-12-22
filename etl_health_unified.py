import pandas as pd
import requests
import io

print("--- Starting Unified Health ETL (Bio-Radar) ---")

# Helper to safely fetch data
def fetch_csv_safe(url):
    try:
        # Use requests with a timeout (more robust than pandas direct read)
        s = requests.get(url, timeout=10).content
        return pd.read_csv(io.StringIO(s.decode('utf-8')))
    except Exception as e:
        print(f"   > Failed to fetch {url}: {e}")
        return pd.DataFrame()

# 1. COVID-19 (Source: Our World in Data)
print("1. Fetching COVID-19 Data (OWID)...")
df_covid = fetch_csv_safe("https://covid.ourworldindata.org/data/owid-covid-data.csv")

if not df_covid.empty:
    df_covid = df_covid[['iso_code', 'location', 'date', 'total_deaths_per_million']]
    # Get latest snapshot per country
    df_covid = df_covid.sort_values('date').groupby('iso_code').tail(1)
    df_covid = df_covid.rename(columns={'total_deaths_per_million': 'COVID_Deaths_per_M', 'location': 'Country'})
    print(f"   > Loaded COVID stats for {len(df_covid)} locations.")
else:
    print("   > ⚠️ Warning: COVID data unavailable. Proceeding with backup sources.")

# 2. WORLD BANK INDICATORS
def get_wb_data(indicator, col_name, year):
    print(f"   > Fetching {col_name}...")
    url = f"http://api.worldbank.org/v2/country/all/indicator/{indicator}?format=json&per_page=300&date={year}"
    try:
        resp = requests.get(url, timeout=10).json()
        data = []
        if len(resp) > 1:
            for item in resp[1]:
                if item['value'] is not None:
                    data.append({'iso_code': item['countryiso3code'], col_name: item['value'], 'Country_WB': item['country']['value']})
        return pd.DataFrame(data)
    except:
        return pd.DataFrame()

# Fetch datasets
df_suicide = get_wb_data("SH.STA.SUIC.P5", "Suicide_Rate_100k", 2019)
df_aids = get_wb_data("SH.DYN.AIDS.ZS", "AIDS_Prevalence_Pct", 2021)
df_death = get_wb_data("SP.DYN.CDRT.IN", "General_Death_Rate_1k", 2021)

# 3. MERGE EVERYTHING
print("3. Merging Datasets...")

# Establish a "Base" dataframe. Prefer COVID data, fallback to World Bank if COVID failed.
if not df_covid.empty:
    base_df = df_covid[['iso_code', 'Country', 'COVID_Deaths_per_M']]
elif not df_suicide.empty:
    base_df = df_suicide[['iso_code', 'Country_WB']].rename(columns={'Country_WB': 'Country'})
    base_df['COVID_Deaths_per_M'] = 0 # Fill missing
else:
    # If everything fails, create empty structure
    base_df = pd.DataFrame(columns=['iso_code', 'Country'])

# Merge
if not base_df.empty:
    df_final = pd.merge(base_df, df_suicide[['iso_code', 'Suicide_Rate_100k']], on='iso_code', how='left')
    df_final = pd.merge(df_final, df_aids[['iso_code', 'AIDS_Prevalence_Pct']], on='iso_code', how='left')
    df_final = pd.merge(df_final, df_death[['iso_code', 'General_Death_Rate_1k']], on='iso_code', how='left')
    
    # Save
    df_final.to_csv("health_unified.csv", index=False)
    print("--- SUCCESS: Saved 'health_unified.csv' ---")
    print(df_final.head())
else:
    print("❌ Critical Error: No data sources available.")
