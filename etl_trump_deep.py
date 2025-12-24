import requests
import pandas as pd
from bs4 import BeautifulSoup
from textblob import TextBlob
import re

print("--- Starting Deep Trump Timeline Scraper (1970s-2025) ---")

# We target specific Wikipedia Timelines to cover his ENTIRE life
URLS = [
    # The Business Years (1970s-2015)
    "https://en.wikipedia.org/wiki/Timeline_of_Donald_Trump%27s_business_career",
    # The Presidency (Sample Years)
    "https://en.wikipedia.org/wiki/Timeline_of_the_Donald_Trump_presidency_(2017_Q1)",
    "https://en.wikipedia.org/wiki/Timeline_of_the_Donald_Trump_presidency_(2020_Q1)",
    # Post-Presidency / Legal
    "https://en.wikipedia.org/wiki/Indictments_against_Donald_Trump" 
]

events = []

for url in URLS:
    print(f"Scraping: {url}...")
    try:
        res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(res.text, 'html.parser')
        
        # Scrape the main content list items
        content = soup.find('div', {'class': 'mw-parser-output'})
        if content:
            for item in content.find_all('li'):
                text = item.get_text(strip=True)
                
                # Filter for Year-like patterns (e.g., "1987:", "In 2004,")
                # This ensures we get dated events
                if re.search(r'\b(19|20)\d{2}\b', text) and len(text) > 50:
                    
                    # Attempt to extract the year for sorting
                    year_match = re.search(r'\b(19|20)\d{2}\b', text)
                    year = year_match.group(0) if year_match else "Unknown"
                    
                    # Clean citations [12]
                    clean_text = re.sub(r'\[.*?\]', '', text)
                    
                    events.append({
                        "Year": year,
                        "Event": clean_text[:200] + "...", # Truncate for display
                        "Full_Text": clean_text
                    })
    except Exception as e:
        print(f"Error scraping {url}: {e}")

# NLP Analysis
print(f"Analyzing Sentiment for {len(events)} historical events...")
for ev in events:
    blob = TextBlob(ev['Full_Text'])
    score = blob.sentiment.polarity
    ev['Sentiment_Score'] = score
    
    # Categorize
    if score > 0.05: ev['Category'] = "Positive"
    elif score < -0.05: ev['Category'] = "Negative"
    else: ev['Category'] = "Neutral"

# Save
df = pd.DataFrame(events)
# Sort by Year
df = df.sort_values('Year')
df.to_csv("trump_real_timeline.csv", index=False)
print(f"--- SUCCESS: Saved {len(df)} events from 1970s-Present ---")
