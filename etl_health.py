import wbgapi as wb
import pandas as pd
from datetime import datetime

# --- CONFIGURATION ---
# "SP.DYN.CDRT.IN" = Crude Death Rate (per 1,000 people)
INDICATOR_CODE = 'SP.DYN.CDRT.IN'

print("--- Starting Health ETL (via wbgapi) ---")

try:
    # 1. FETCH DATA
    # wbgapi makes this incredibly simple. 
    # 'data.DataFrame' fetches the data directly into a pandas format.
    # labels=True gives us Country Names (e.g., "Brazil") instead of just codes ("BRA")
    print("1. Fetching data from World Bank...")
    
    df = wb.data.DataFrame(
        INDICATOR_CODE, 
        wb.region.members('WLD'), # Fetch all countries (excludes aggregates like 'Arab World')
        time=range(1960, 2024),   # Time range
        labels=True
    )
    
    # 2. CLEANING
    print("2. Cleaning dataset...")
    
    # The dataframe comes in wide format (Years as columns). We want Long format.
    # Reset index to move "Country" from index to column
    df = df.reset_index()
    
    # Melt it: Turn year columns (YR1960, YR1961...) into rows
    df_melted = df.melt(id_vars=['economy', 'Country'], var_name='Year', value_name='Death_Rate')
    
    # Clean the Year column (Remove 'YR' prefix and convert to int)
    df_melted['Year'] = df_melted['Year'].str.replace('YR', '').astype(int)
    
    # Drop rows with missing data
    df_clean = df_melted.dropna()
    
    # 3. SAVE
    filename = "health_death_rates.csv"
    df_clean.to_csv(filename, index=False)
    
    print(f"--- SUCCESS ---")
    print(f"Saved {len(df_clean)} records to {filename}")
    print(df_clean.head())

except Exception as e:
    print(f"❌ Error: {e}")
