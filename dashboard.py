import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Global Observatory", page_icon="🌍", layout="wide")

# --- CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    h1, h2, h3, h4, p { font-family: 'Helvetica Neue', sans-serif !important; color: #fafafa !important; }
    .stMetric { background-color: #1f2937; border-left: 5px solid #FF4B4B; }
    div[data-testid="stMetricValue"] { color: #fafafa !important; }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.title("📡 NAVIGATION")
options = [
    "1. Commodity-Climate",
    "2. Bio-Radar",
    "3. Greenflation",
    "4. Security Monitor",
    "5. Agenda Setter (Decades)",
    "6. Underworld Atlas (Deep)",
    "7. Global Terror Log",
    "8. Autism Diagnosis History"
]
selection = st.sidebar.radio("Select Module:", options)

# 1. COMMODITY-CLIMATE
if selection == "1. Commodity-Climate":
    st.title("🌧️ COMMODITY-CLIMATE MONITOR")
    try:
        df = pd.read_csv("coffee_weather_master.csv")
        st.line_chart(df.set_index('Date')[['Close_Price', 'Rolling_Rain_30d']])
    except: st.error("Data missing.")

# 2. BIO-RADAR
elif selection == "2. Bio-Radar":
    st.title("🧬 THE BIO-RADAR")
    try:
        df = pd.read_csv("health_unified.csv")
        metric = st.selectbox("Metric:", ["COVID_Deaths_per_M", "Suicide_Rate_100k", "AIDS_Prevalence_Pct"])
        fig = px.choropleth(df, locations="iso_code", color=metric, hover_name="Country", color_continuous_scale="Viridis")
        fig.update_layout(template="plotly_dark", geo=dict(bgcolor="#0e1117"))
        st.plotly_chart(fig, use_container_width=True)
    except: st.error("Data missing.")

# 3. GREENFLATION
elif selection == "3. Greenflation":
    st.title("⚡ THE GREENFLATION MONITOR")
    try:
        df = pd.read_csv("energy_oil_co2.csv")
        st.line_chart(df.set_index('Year')[['Avg_Oil_Price', 'Global_CO2_MillionTons']])
    except: st.error("Data missing.")

# 4. SECURITY MONITOR
elif selection == "4. Security Monitor":
    st.title("🛡️ SECURITY MONITOR")
    try:
        df = pd.read_csv("security_events.csv")
        st.metric("Events (24h)", len(df))
        fig = px.scatter_geo(df, lat='Latitude', lon='Longitude', size='Article_Count')
        fig.update_layout(template="plotly_dark", geo=dict(bgcolor="#0e1117"))
        st.plotly_chart(fig, use_container_width=True)
    except: st.error("Data missing.")

# 5. AGENDA SETTER (DECADES)
elif selection == "5. Agenda Setter (Decades)":
    st.title("🗳️ THE AGENDA SETTER")
    st.markdown("### 🧠 40-Year Sentiment Analysis: Donald Trump")
    try:
        df = pd.read_csv("trump_real_timeline.csv")
        fig = px.scatter(df, x="Year", y="Sentiment_Score", color="Category", hover_data=["Event"], 
                         color_discrete_map={"Positive":"#00ff00", "Negative":"#ff0000", "Neutral":"#888888"})
        fig.update_layout(template="plotly_dark", height=500)
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(df[['Year', 'Event', 'Category']], hide_index=True)
    except: st.error("Data missing.")

# 6. UNDERWORLD ATLAS (DEEP)
elif selection == "6. Underworld Atlas (Deep)":
    st.title("💀 THE UNDERWORLD ATLAS")
    st.markdown("### 🕸️ Detailed Dossiers: Revenue & Activity")
    try:
        df = pd.read_csv("underworld_rich_data.csv")
        search = st.text_input("🔍 Search Dossier (e.g., 'Drug', 'Extortion')")
        if search: df = df[df.apply(lambda row: search.lower() in str(row).lower(), axis=1)]
        for i, row in df.iterrows():
            with st.expander(f"{row['Group Name']}"):
                c1, c2 = st.columns(2)
                c1.markdown(f"**💰 Revenue:** {row['Est. Revenue']}")
                c1.markdown(f"**🔫 Activities:** {row['Criminal Activities']}")
                c2.markdown(f"**👥 Membership:** {row['Membership']}")
                c2.markdown(f"**📅 Founded:** {row['Founded']}")
                st.markdown(f"[View Wikipedia Entry]({row['Wiki_Link']})")
    except: st.error("Data missing.")

# 7. GLOBAL TERROR LOG
elif selection == "7. Global Terror Log":
    st.title("💣 GLOBAL TERROR MONITOR")
    try:
        df = pd.read_csv("global_terror_log.csv")
        c1, c2 = st.columns(2)
        c1.metric("Total Incidents", len(df))
        c2.metric("Total Casualties", df['Deaths'].sum())
        st.bar_chart(df['Location'].value_counts().head(10))
        st.dataframe(df[['Date', 'Location', 'Deaths', 'Perpetrator']], hide_index=True)
    except: st.error("Data missing. Run 'etl_terror.py'.")

# 8. AUTISM DIAGNOSIS HISTORY
elif selection == "8. Autism Diagnosis History":
    st.title("🧩 DIAGNOSIS TIMELINE")
    st.markdown("### 📜 Evolution of Diagnosis (1911 - 2025)")
    try:
        df = pd.read_csv("autism_diagnosis_timeline.csv")
        for i, row in df.iterrows():
            color = "#95a5a6" if row['Year'] < 1980 else "#f1c40f" if row['Year'] < 2000 else "#e74c3c"
            with st.container():
                c1, c2 = st.columns([1, 4])
                c1.markdown(f"<h2 style='text-align: right; color: {color}'>{row['Year']}</h2>", unsafe_allow_html=True)
                c2.markdown(f"<div style='border-left: 4px solid {color}; padding-left: 15px; margin-bottom: 20px;'>"
                            f"<h4 style='margin:0'>{row['Authority']}</h4>"
                            f"<h5 style='margin:0; color: #00d4ff'>{row['Definition']}</h5>"
                            f"<p>{row['Context']}</p></div>", unsafe_allow_html=True)
    except: st.error("Data missing.")
