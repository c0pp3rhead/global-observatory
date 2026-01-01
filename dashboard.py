import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

st.set_page_config(page_title="Global Observatory", page_icon="🌍", layout="wide")
st.markdown("""<style>.stApp { background-color: #0e1117; } h1, h2, h3, h4, p { font-family: 'Helvetica Neue', sans-serif !important; color: #fafafa !important; } .stMetric { background-color: #1f2937; border-left: 5px solid #FF4B4B; } div[data-testid="stMetricValue"] { color: #fafafa !important; }</style>""", unsafe_allow_html=True)

# --- SIDEBAR: MODE SWITCHER ---
st.sidebar.title("📡 MODE SELECTION")
app_mode = st.sidebar.radio("Choose Interface:", ["🔍 Live Observatory (Tools)", "📚 Research Archives (Articles)"])
st.sidebar.divider()

# =========================================================
# MODE 1: THE LIVE OBSERVATORY (Your Existing Tools)
# =========================================================
if app_mode == "🔍 Live Observatory (Tools)":
    st.sidebar.subheader("Live Modules")
    options = [
        "1. Commodity-Climate",
        "2. Bio-Radar (Mortality)",
        "3. Security Monitor",
        "4. Agenda Setter",
        "5. Underworld Asset Tracker",
        "6. Global Terror Log",
        "7. Autism Diagnosis History"
    ]
    selection = st.sidebar.radio("Select Tool:", options)

    # 1. COMMODITY
    if selection == "1. Commodity-Climate":
        st.title("🌧️ COMMODITY-CLIMATE MONITOR")
        st.caption("ℹ️ **Legend:** Data correlates daily coffee market prices (USD) with rolling 30-day rainfall averages.")
        try:
            df = pd.read_csv("coffee_weather_master.csv")
            st.line_chart(df.set_index('Date')[['Close_Price', 'Rolling_Rain_30d']])
        except: st.error("Data missing.")

    # 2. BIO-RADAR
    elif selection == "2. Bio-Radar (Mortality)":
        st.title("🧬 THE BIO-RADAR")
        try:
            df = pd.read_csv("health_unified.csv")
            t1, t2, t3 = st.tabs(["General Death Count", "Suicide Rates", "HIV/AIDS"])
            with t1:
                st.markdown("### 💀 General Mortality")
                fig = px.choropleth(df, locations="iso_code", color="General_Death_Rate_1k", hover_name="Country", color_continuous_scale="Reds")
                fig.update_layout(template="plotly_dark", geo=dict(bgcolor="#0e1117"))
                st.plotly_chart(fig, use_container_width=True)
            with t2:
                st.markdown("### 📉 Suicide Rate")
                fig = px.choropleth(df, locations="iso_code", color="Suicide_Rate_100k", hover_name="Country", color_continuous_scale="Viridis")
                fig.update_layout(template="plotly_dark", geo=dict(bgcolor="#0e1117"))
                st.plotly_chart(fig, use_container_width=True)
            with t3:
                st.markdown("### 🎗️ HIV/AIDS Prevalence")
                fig = px.choropleth(df, locations="iso_code", color="AIDS_Prevalence_Pct", hover_name="Country", color_continuous_scale="Plasma")
                fig.update_layout(template="plotly_dark", geo=dict(bgcolor="#0e1117"))
                st.plotly_chart(fig, use_container_width=True)
        except: st.error("Data missing.")

    # 3. SECURITY MONITOR
    elif selection == "3. Security Monitor":
        st.title("🛡️ SECURITY MONITOR")
        try:
            df = pd.read_csv("security_events.csv")
            st.metric("Active Events", len(df))
            fig = px.scatter_geo(df, lat='Latitude', lon='Longitude', size='Article_Count',
                                 color="Article_Count", color_continuous_scale="Plasma")
            fig.update_layout(template="plotly_dark", geo=dict(bgcolor="#0e1117"), coloraxis_colorbar=dict(title="News Intensity"))
            st.plotly_chart(fig, use_container_width=True)
        except: st.error("Data missing.")

    # 4. AGENDA SETTER
    elif selection == "4. Agenda Setter":
        st.title("🗳️ THE AGENDA SETTER")
        st.caption("ℹ️ **Legend:** Data represents the sentiment polarity of historical events involving Donald Trump.")
        try:
            df = pd.read_csv("trump_real_timeline.csv")
            fig = px.scatter(df, x="Year", y="Sentiment_Score", color="Category", hover_data=["Event"], 
                             color_discrete_map={"Positive":"#00ff00", "Negative":"#ff0000", "Neutral":"#888888"})
            fig.update_layout(template="plotly_dark", height=500)
            st.plotly_chart(fig, use_container_width=True)
        except: st.error("Data missing.")

    # 5. UNDERWORLD
    elif selection == "5. Underworld Asset Tracker":
        st.title("💀 UNDERWORLD ASSET TRACKER")
        st.caption("ℹ️ **Legend:** Tracks verified seizures (Drugs, Money, Weapons) linked to criminal groups.")
        try:
            df = pd.read_csv("seizure_log.csv")
            col1, col2 = st.columns(2)
            col1.metric("Seizure Events", len(df))
            col2.metric("Groups Impacted", df['Group'].nunique())
            search = st.text_input("🔍 Search Logs")
            if search: df = df[df.apply(lambda row: search.lower() in str(row).lower(), axis=1)]
            st.dataframe(df[['Year', 'Group', 'Seized Assets', 'Source_Link']], hide_index=True, use_container_width=True)
        except: st.error("Data missing.")

    # 6. TERROR LOG
    elif selection == "6. Global Terror Log":
        st.title("💣 GLOBAL TERROR MONITOR")
        st.caption("ℹ️ **Legend:** Verified terrorist incidents 2023-2024.")
        try:
            df = pd.read_csv("global_terror_log.csv")
            c1, c2 = st.columns(2)
            c1.metric("Total Incidents", len(df))
            c2.metric("Total Deaths", df['Deaths'].sum())
            st.divider()
            
            # Map
            st.markdown("### 🚨 Impact Map: Deaths by Country")
            df_map = df.groupby('Country')['Deaths'].sum().reset_index()
            fig_map = px.choropleth(df_map, locations="Country", locationmode="country names", color="Deaths", color_continuous_scale="Reds")
            fig_map.update_layout(template="plotly_dark", geo=dict(bgcolor="#0e1117", showlakes=False))
            st.plotly_chart(fig_map, use_container_width=True)
            
            # Deadliest
            st.markdown("### ⚰️ Deadliest Attacks")
            st.dataframe(df.sort_values('Deaths', ascending=False).head(10)[['Date','Location','Deaths']], hide_index=True, use_container_width=True)
        except: st.error("Data missing.")

    # 7. AUTISM TIMELINE
    elif selection == "7. Autism Diagnosis History":
        st.title("🧩 DIAGNOSIS TIMELINE")
        try:
            df = pd.read_csv("autism_diagnosis_timeline.csv")
            for i, row in df.iterrows():
                color = "#95a5a6" if row['Year'] < 1980 else "#f1c40f" if row['Year'] < 2000 else "#e74c3c"
                with st.container():
                    st.markdown(f"<h3 style='color:{color}'>{row['Year']} - {row['Authority']}</h3>", unsafe_allow_html=True)
                    st.markdown(f"**{row['Definition']}**: {row['Context']}")
                    st.markdown(f"<p style='font-size:0.9em; background:#1f2937; padding:10px;'>{row.get('Symptoms','')}</p>", unsafe_allow_html=True)
        except: st.error("Data missing.")

# =========================================================
# MODE 2: RESEARCH ARCHIVES (The PhD Platform)
# =========================================================
elif app_mode == "📚 Research Archives (Articles)":
    st.title("📚 RESEARCH ARCHIVES")
    st.markdown("### Academic Repository & Analysis")
    st.markdown("Select a research pillar to view archived notes, screenshots, and static analysis.")
    
    # 1. Select Pillar
    base_path = "research_articles"
    try:
        pillars = sorted([f for f in os.listdir(base_path) if not f.startswith('.')])
        selected_pillar = st.sidebar.selectbox("Select Research Pillar:", pillars)
        
        # 2. Select Article
        pillar_path = os.path.join(base_path, selected_pillar)
        articles = [f for f in os.listdir(pillar_path) if f.endswith('.md')]
        
        if articles:
            selected_article = st.sidebar.radio("Select Article:", articles)
            
            # 3. Display Article
            st.divider()
            with open(os.path.join(pillar_path, selected_article), "r") as f:
                content = f.read()
                st.markdown(content, unsafe_allow_html=True)
        else:
            st.info("No articles published in this pillar yet.")
            
    except FileNotFoundError:
        st.error("Archive directory not found. Please run 'setup_research.py'.")
