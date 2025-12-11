import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Global Pulse: Commodity Monitor",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    h1, h2, h3 {
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 800;
        color: #f0f2f6;
    }
    .stMetric {
        background-color: #1f2937;
        padding: 15px;
        border-radius: 5px;
        border-left: 5px solid #FF4B4B;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DATA LOADING ---
@st.cache_data
def load_data():
    df = pd.read_csv("coffee_weather_master.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.dropna()
    df = df.sort_values('Date')
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("❌ Data file not found. Please run 'etl_weather.py' first.")
    st.stop()

# --- 3. DASHBOARD HEADER ---
st.title("🌍 THE GLOBAL OBSERVATORY")
st.markdown("### LIVE FEED: Commodity Weather Impact / [BRAZIL: MINAS GERAIS]")
st.markdown("---")

# --- 4. METRICS ROW ---
latest = df.iloc[-1]
prev = df.iloc[-2]

col1, col2, col3, col4 = st.columns(4)

with col1:
    price_diff = latest['Close_Price'] - prev['Close_Price']
    st.metric("Coffee Futures (KC=F)", f"${latest['Close_Price']:.2f}", f"{price_diff:.2f}")

with col2:
    rain_diff = latest['Rolling_Rain_30d'] - prev['Rolling_Rain_30d']
    st.metric("30-Day Rainfall (mm)", f"{latest['Rolling_Rain_30d']:.1f} mm", f"{rain_diff:.1f} mm")

with col3:
    drought_status = "CRITICAL" if latest['Rolling_Rain_30d'] < 50 else "STABLE"
    st.metric("Drought Risk Level", drought_status, delta_color="off")

with col4:
    correlation = df['Close_Price'].corr(df['Rolling_Rain_30d'])
    st.metric("Price-Weather Correlation", f"{correlation:.2f}")

# --- 5. MAIN VISUALIZATION (Dual Axis) ---
st.markdown("### 📊 Market vs. Climate Analysis")

min_date = df['Date'].min()
max_date = df['Date'].max()
start_date, end_date = st.slider(
    "Select Date Range",
    min_value=min_date.date(),
    max_value=max_date.date(),
    value=(datetime(2020, 1, 1).date(), max_date.date())
)

mask = (df['Date'].dt.date >= start_date) & (df['Date'].dt.date <= end_date)
df_filtered = df.loc[mask]

fig = go.Figure()

# Trace 1: Rainfall (Bar Chart)
fig.add_trace(go.Bar(
    x=df_filtered['Date'],
    y=df_filtered['Rolling_Rain_30d'],
    name="30-Day Rainfall (mm)",
    marker_color='rgba(52, 152, 219, 0.5)',
    yaxis='y2'
))

# Trace 2: Coffee Price (Line Chart)
fig.add_trace(go.Scatter(
    x=df_filtered['Date'],
    y=df_filtered['Close_Price'],
    name="Coffee Price ($)",
    line=dict(color='#FF4B4B', width=2)
))

# Layout Updates - UPDATED FOR PLOTLY 6.0 COMPATIBILITY
fig.update_layout(
    template="plotly_dark",
    height=600,
    title_text="Correlation: Rainfall vs. Market Price",
    yaxis=dict(
        title=dict(text="Coffee Price ($)", font=dict(color="#FF4B4B")),
        tickfont=dict(color="#FF4B4B")
    ),
    yaxis2=dict(
        title=dict(text="30-Day Rainfall (mm)", font=dict(color="#3498db")),
        tickfont=dict(color="#3498db"),
        overlaying='y',
        side='right'
    ),
    legend=dict(x=0, y=1.1, orientation="h")
)

st.plotly_chart(fig, use_container_width=True)

# --- 6. ANALYST NOTES ---
st.markdown("### 📝 Analyst Briefing")
st.info(f"""
**Observation for {end_date}:**
When the blue bars (Rainfall) drop significantly for sustained periods (Drought), the red line (Price) often reacts with a lag. 
The current correlation coefficient of **{correlation:.2f}** suggests a { "strong" if abs(correlation) > 0.5 else "moderate"} inverse relationship.
""")
