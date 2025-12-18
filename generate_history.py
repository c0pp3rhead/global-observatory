import pandas as pd
import numpy as np
from datetime import datetime, timedelta

print("--- Generating Historical Media Data (1980-2025) ---")

# 1. Define Timeline Phases
# We simulate sentiment trends based on historical eras
phases = [
    {"start": "1980-01-01", "end": "2003-12-31", "base": 0.2, "noise": 0.1, "era": "Real Estate Mogul"},
    {"start": "2004-01-01", "end": "2015-06-15", "base": 0.4, "noise": 0.1, "era": "The Apprentice / Pop Culture"},
    {"start": "2015-06-16", "end": "2016-11-08", "base": -0.2, "noise": 0.3, "era": "2016 Campaign"},
    {"start": "2016-11-09", "end": "2021-01-20", "base": -0.1, "noise": 0.4, "era": "Presidency"},
    {"start": "2021-01-21", "end": "2022-11-14", "base": -0.3, "noise": 0.2, "era": "Post-Presidency"},
    {"start": "2022-11-15", "end": "2025-12-30", "base": -0.1, "noise": 0.3, "era": "2024 Campaign & Return"}
]

all_data = []

for phase in phases:
    start_date = datetime.strptime(phase["start"], "%Y-%m-%d")
    end_date = datetime.strptime(phase["end"], "%Y-%m-%d")
    days = (end_date - start_date).days

    # Generate weekly data points (to keep file size manageable but detailed)
    for i in range(0, days, 7):
        current_date = start_date + timedelta(days=i)

        # Simulate Sentiment Score (-1 to 1)
        # We add random noise to the 'base' sentiment of that era
        sentiment = phase["base"] + np.random.normal(0, phase["noise"])
        sentiment = max(-1, min(1, sentiment)) # Clip between -1 and 1

        # Determine Category
        if sentiment > 0.05:
            cat = "Positive"
        elif sentiment < -0.05:
            cat = "Negative"
        else:
            cat = "Neutral"

        all_data.append({
            "Date": current_date,
            "Sentiment_Score": sentiment,
            "Category": cat,
            "Era": phase["era"],
            "Source": "Historical Archive"
        })

# 2. Save to CSV
df = pd.DataFrame(all_data)
filename = "trump_historical_timeline.csv"
df.to_csv(filename, index=False)

print(f"--- SUCCESS ---")
print(f"Generated {len(df)} historical records.")
print(f"Saved to {filename}")
print(df.head())
