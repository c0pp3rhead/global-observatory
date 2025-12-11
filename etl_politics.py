import feedparser
import pandas as pd
from textblob import TextBlob
from datetime import datetime
import time

print("--- Starting Politics ETL: Sentiment Analysis ---")

# --- CONFIGURATION ---
# We use Google News RSS (Stable, Free, No API Key needed)
# Query: Donald Trump + high-impact policy words
RSS_URL = "https://news.google.com/rss/search?q=Donald+Trump+OR+Trump+Policy&hl=en-US&gl=US&ceid=US:en"

print(f"1. Fetching News Feed from: {RSS_URL}...")

try:
    # 1. PARSE FEED
    feed = feedparser.parse(RSS_URL)
    print(f"   > Retrieved {len(feed.entries)} headlines.")
    
    news_data = []
    
    for entry in feed.entries:
        title = entry.title
        pub_date = entry.published
        link = entry.link
        
        # 2. NLP ANALYSIS (The "AI" part)
        # TextBlob calculates sentiment:
        # Polarity: -1 (Negative) to +1 (Positive)
        # Subjectivity: 0 (Fact) to 1 (Opinion)
        blob = TextBlob(title)
        sentiment = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        
        # Categorize the sentiment for the dashboard
        if sentiment > 0.1:
            category = "Positive"
        elif sentiment < -0.1:
            category = "Negative"
        else:
            category = "Neutral"
            
        news_data.append({
            'Date': pub_date,
            'Title': title,
            'Sentiment_Score': sentiment,
            'Subjectivity_Score': subjectivity,
            'Category': category,
            'Source': entry.source.get('title', 'Google News'),
            'Link': link
        })
    
    # 3. SAVE DATA
    df = pd.DataFrame(news_data)
    
    # Convert Date to datetime object for sorting
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date', ascending=False)
    
    filename = "politics_sentiment.csv"
    df.to_csv(filename, index=False)
    
    print(f"--- SUCCESS ---")
    print(f"Analyzed {len(df)} articles.")
    print(f"Avg Sentiment: {df['Sentiment_Score'].mean():.3f}")
    print(df[['Title', 'Category']].head(3))

except Exception as e:
    print(f"❌ Error: {e}")
