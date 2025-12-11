import yfinance as yf
import pandas as pd
import requests
from datetime import datetime

# --- CONFIGURATION ---
# We use the 2000-Present window we agreed on
START_DATE = "2000-01-01"
TODAY = datetime.today().strftime('%Y-%m-%d')

# Coordinates for Varginha, Minas Gerais (Heart of Brazilian Coffee)
LAT = -21.55
LON = -45.43

print(f"--- Starting ETL Process: {START_DATE} to {TODAY} ---")

# 1. FETCH FINANCIAL DATA (Target Variable)
print("1. Fetching Coffee Futures (KC=F)...")
ticker = yf.Ticker("KC=F")
coffee = ticker.history(start=START_DATE, end=TODAY)

# Clean up: We only want the Closing price and the Date
coffee = coffee[['Close']].reset_index()
# Rename columns to be standard
coffee.columns = ['Date', 'Close_Price']
# Ensure Date format is standard (remove timezone info if present)
coffee['Date'] = pd.to_datetime(coffee['Date']).dt.date

print(f"   > Retrieved {len(coffee)} trading days of price data.")

# 2. FETCH WEATHER DATA (Predictor Variable)
print("2. Fetching Historical Weather from Open-Meteo...")
url = "https://archive-api.open-meteo.com/v1/archive"
params = {
    "latitude": LAT,
    "longitude": LON,
    "start_date": START_DATE,
    "end_date": TODAY,
    "daily": ["temperature_2m_max", "precipitation_sum"],
    "timezone": "America/Sao_Paulo"
}

response = requests.get(url, params=params)
weather_json = response.json()

# Convert JSON to Pandas DataFrame
daily_data = weather_json['daily']
df_weather = pd.DataFrame({
    'Date': daily_data['time'],
    'Max_Temp_C': daily_data['temperature_2m_max'],
    'Rainfall_mm': daily_data['precipitation_sum']
})
df_weather['Date'] = pd.to_datetime(df_weather['Date']).dt.date
print(f"   > Retrieved {len(df_weather)} days of weather data.")

# 3. TRANSFORM & MERGE
print("3. Merging datasets...")
# Inner join: We only keep days where we have BOTH price and weather
df_master = pd.merge(coffee, df_weather, on='Date', how='inner')

# Feature Engineering: Add a 30-day Rolling Rainfall average
# (Because one day of rain doesn't grow coffee; sustained rain does)
df_master['Rolling_Rain_30d'] = df_master['Rainfall_mm'].rolling(window=30).sum()

# 4. LOAD (Save to CSV)
filename = "coffee_weather_master.csv"
df_master.to_csv(filename, index=False)

print(f"--- SUCCESS ---")
print(f"Data saved to /Users/cristianmorales/Documents/GlobalPulse/{filename}")
print("First 5 rows of your new dataset:")
print(df_master.head())
