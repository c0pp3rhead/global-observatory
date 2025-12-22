import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# --- CONFIG ---
st.set_page_config(page_title="Global Observatory", page_icon="🌍", layout="wide")

# --- CSS (High Contrast & Magazine Style) ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    h1, h2, h3, h4, h5, h6, .stMarkdown, p, label { font-family: 'Helvetica Neue', sans-serif !important; color: #fafafa !important; }
    .stMetric { background-color: #1f2937; padding: 15px; border-radius: 5px; border-left: 5px solid #FF4B4B; }
    div[data-testid="stMetricValue"] { color: #fafafa !important; }
    div[data-testid="stMetricLabel"] { color: #d1d5db !important; }
    </style>
    """, unsafe_allow_html=True)

# --- HELPER ---
def get_chart_config(): return {'displayModeBar': False, 'scrollZoom': False, 'staticPlot': False}
COLOR_BG = "#0e1117"

# --- SIDEBAR ---
st.sidebar.title("📡 NAVIGATION")
options = [
    "1. Commodity-Climate Monitor",
    "2. Bio-Radar (Global Health)",
    "3. Greenflation (Energy vs CO2)",
    "4. Security Monitor (Live)",
    "5. Agenda Setter (Trump Analysis)",
    "6. Underworld Atlas"
]
selection = st.sidebar.radio("Select Module:", options)
st.sidebar.markdown("---")
st.sidebar.info("📡 Data Streams Active")

# ==========================================
# 1. COMMODITY-CLIMATE (Coffee)
# ==========================================
if selection == "1. Commodity-Climate Monitor":
    st.title("🌧️ COMMODITY-CLIMATE MONITOR")
    st.markdown("### 📉 Coffee Futures vs. Brazil Rainfall")
    try:
        df = pd.read_csv("coffee_weather_master.csv")
        df['Date'] = pd.to_datetime(df['Date'])
        # Simple Line Chart
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['Date'], y=df['Close_Price'], name="Price ($)", line=dict(color="#ff007f", width=2)))
        fig.add_trace(go.Scatter(x=df['Date'], y=df['Rolling_Rain_30d'], name="Rain (mm)", line=dict(color="#00d4ff", width=2), yaxis='y2'))
        fig.update_layout(template="plotly_dark", height=450, yaxis2=dict(overlaying='y', side='right'))
        st.plotly_chart(fig, use_container_width=True, config=get_chart_config())
    except: st.error("Data missing.")

# ==========================================
# 2. BIO-RADAR (Consolidated Health)
# ==========================================
elif selection == "2. Bio-Radar (Global Health)":
    st.title("🧬 THE BIO-RADAR")
    st.markdown("### 🗺️ Global Mortality & Crisis Metrics")
    st.markdown("---")
    
    try:
        df = pd.read_csv("health_unified.csv")
        
        # SELECTOR
        metric = st.selectbox("Select Metric:", 
             ["General_Death_Rate_1k", "COVID_Deaths_per_M", "AIDS_Prevalence_Pct", "Suicide_Rate_100k"])
        
        labels = {
            "General_Death_Rate_1k": "Death Rate (per 1k)",
            "COVID_Deaths_per_M": "COVID Deaths (per Million)",
            "AIDS_Prevalence_Pct": "HIV/AIDS Prevalence (%)",
            "Suicide_Rate_100k": "Suicide Rate (per 100k)"
        }
        
        # Map
        fig = px.choropleth(
            df, locations="iso_code", color=metric,
            hover_name="Country", projection="natural earth",
            color_continuous_scale="Reds" if "COVID" in metric else "Viridis",
            title=f"Global Heatmap: {labels[metric]}"
        )
        fig.update_layout(template="plotly_dark", geo=dict(bgcolor=COLOR_BG, showframe=False), margin=dict(l=0,r=0,t=40,b=0), height=500)
        st.plotly_chart(fig, use_container_width=True, config=get_chart_config())
        
        # Stats
        st.markdown("#### 🚩 Top 5 Highest Rates")
        top5 = df.sort_values(metric, ascending=False).head(5)
        st.table(top5[['Country', metric]])
        
    except FileNotFoundError: st.error("⚠️ Health Data missing. Run 'etl_health_unified.py'.")

# ==========================================
# 3. GREENFLATION (Oil vs CO2)
# ==========================================
elif selection == "3. Greenflation (Energy vs CO2)":
    st.title("⚡ THE GREENFLATION MONITOR")
    st.markdown("### 🛢️ Oil Prices vs. Emissions")
    try:
        df = pd.read_csv("energy_oil_co2.csv")
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['Year'], y=df['Global_CO2_MillionTons'], name="CO2", line=dict(color="#00d4ff")))
        fig.add_trace(go.Scatter(x=df['Year'], y=df['Avg_Oil_Price'], name="Oil ($)", yaxis='y2', line=dict(color="#f1c40f")))
        fig.update_layout(template="plotly_dark", height=450, yaxis2=dict(overlaying='y', side='right'))
        st.plotly_chart(fig, use_container_width=True, config=get_chart_config())
    except: st.error("Data missing.")

# ==========================================
# 4. SECURITY MONITOR (Live GDELT)
# ==========================================
elif selection == "4. Security Monitor (Live)":
    st.title("🛡️ SECURITY MONITOR")
    st.markdown("### 🚨 Live Feed: Drug Interdictions")
    try:
        df = pd.read_csv("security_events.csv")
        st.metric("Events (24h)", len(df))
        fig = px.scatter_geo(df, lat='Latitude', lon='Longitude', size='Article_Count', projection="natural earth", color="Article_Count")
        fig.update_layout(template="plotly_dark", geo=dict(bgcolor=COLOR_BG), margin=dict(l=0,r=0,t=0,b=0), height=500)
        st.plotly_chart(fig, use_container_width=True, config=get_chart_config())
    except: st.error("Data missing.")

# ==========================================
# 5. AGENDA SETTER (Real Trump Data)
# ==========================================
elif selection == "5. Agenda Setter (Trump Analysis)":
    st.title("🗳️ THE AGENDA SETTER")
    st.markdown("### 🧠 Media Tone: Donald Trump (Lifetime Analysis)")
    st.warning("ℹ️ Data Source: Verified Wikipedia Timelines & Historical Records (Non-Simulated)")
    
    try:
        df = pd.read_csv("trump_real_timeline.csv")
        
        # Stats
        pos = len(df[df['Category']=='Positive'])
        neg = len(df[df['Category']=='Negative'])
        col1, col2 = st.columns(2)
        col1.metric("Positive Events", pos)
        col2.metric("Negative Events", neg)
        
        st.markdown("### 📜 Verified Event Log")
        st.dataframe(df[['Event', 'Category']], hide_index=True)
        
    except FileNotFoundError: st.error("⚠️ Real Data missing. Run 'etl_trump_deep.py'.")

# ==========================================
# 6. UNDERWORLD ATLAS
# ==========================================
elif selection == "6. Underworld Atlas":
    st.title("💀 THE UNDERWORLD ATLAS")
    st.markdown("### 🕸️ Transnational Criminal Organizations")
    
    try:
        df = pd.read_csv("underworld_atlas.csv")
        
        # REGION FILTER
        regions = ["All"] + sorted(df['Region'].unique().tolist())
        sel_region = st.selectbox("🌍 Filter by Region:", regions)
        
        if sel_region != "All":
            df_view = df[df['Region'] == sel_region]
        else:
            df_view = df
            
        st.metric("Groups Tracked", len(df_view))
        
        st.dataframe(df_view[['Group Name', 'Region', 'Status', 'Wiki_Link']], 
                     column_config={"Wiki_Link": st.column_config.LinkColumn("Full Dossier")},
                     hide_index=True)
        
    except FileNotFoundError: st.error("⚠️ Atlas Data missing. Run 'etl_underworld.py'.")
