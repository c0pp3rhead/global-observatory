import pandas as pd
import yfinance as yf
from datetime import datetime

print("--- Starting Energy ETL: Oil Prices vs. CO2 ---")

# --- 1. GET FINANCIAL DATA (Brent Crude Oil) ---
print("1. Fetching Oil Prices (Brent Crude)...")
# Ticker: BZ=F (Global Oil Benchmark)
oil_ticker = yf.Ticker("BZ=F")
df_oil = oil_ticker.history(period="max")

# Clean and Resample to YEARLY averages
# (Since CO2 data is usually reported yearly, we need to match that granularity)
df_oil = df_oil[['Close']].reset_index()
df_oil['Year'] = df_oil['Date'].dt.year
df_oil_yearly = df_oil.groupby('Year')['Close'].mean().reset_index()
df_oil_yearly.columns = ['Year', 'Avg_Oil_Price']

print(f"   > Retrieved Oil data from {df_oil_yearly['Year'].min()} to {df_oil_yearly['Year'].max()}")

# --- 2. GET CLIMATE DATA (Our World in Data) ---
print("2. Fetching Global CO2 Emissions (OWID)...")
# Direct URL to the raw CSV on GitHub (Best practice for portfolio repeatability)
url = "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"

# Load directly into Pandas
df_co2 = pd.read_csv(url)

# Filter for "World" only (We want global impact)
df_world_co2 = df_co2[df_co2['country'] == 'World'].copy()
df_world_co2 = df_world_co2[['year', 'co2']] # Keep only Year and Total CO2
df_world_co2.columns = ['Year', 'Global_CO2_MillionTons']

print(f"   > Retrieved CO2 data from {df_world_co2['Year'].min()} to {df_world_co2['Year'].max()}")

# --- 3. MERGE DATASETS ---
print("3. Merging datasets...")
# Inner join on 'Year'
df_master = pd.merge(df_oil_yearly, df_world_co2, on='Year', how='inner')

# Calculate "Carbon Intensity of Economy" (Optional, but looks smart)
# For now, we just keep the raw values.

# --- 4. SAVE ---
filename = "energy_oil_co2.csv"
df_master.to_csv(filename, index=False)

print(f"--- SUCCESS ---")
print(f"Data saved to {filename}")
print(df_master.tail())
