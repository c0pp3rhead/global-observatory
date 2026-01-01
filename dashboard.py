import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Global Observatory", page_icon="🌍", layout="wide")
st.markdown("""<style>.stApp { background-color: #0e1117; } h1, h2, h3, h4, p { font-family: 'Helvetica Neue', sans-serif !important; color: #fafafa !important; } .stMetric { background-color: #1f2937; border-left: 5px solid #FF4B4B; } div[data-testid="stMetricValue"] { color: #fafafa !important; }</style>""", unsafe_allow_html=True)

st.sidebar.title("📡 NAVIGATION")
options = [
    "1. Commodity-Climate",
    "2. Bio-Radar (Mortality)",
    "3. Security Monitor",
    "4. Agenda Setter",
    "5. Underworld Asset Tracker",
    "6. Global Terror Log",
    "7. Autism Diagnosis History"
]
selection = st.sidebar.radio("Select Module:", options)

# 1. COMMODITY
if selection == "1. Commodity-Climate":
    st.title("🌧️ COMMODITY-CLIMATE MONITOR")
    st.caption("ℹ️ **Legend:** Data correlates daily coffee market prices (USD) with rolling 30-day rainfall averages in key production regions, highlighting climate impact on soft commodities.")
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
            st.markdown("### 💀 General Mortality (Crude Death Rate per 1k)")
            fig = px.choropleth(df, locations="iso_code", color="General_Death_Rate_1k", hover_name="Country", color_continuous_scale="Reds")
            fig.update_layout(template="plotly_dark", geo=dict(bgcolor="#0e1117"))
            st.plotly_chart(fig, use_container_width=True)
        with t2:
            st.markdown("### 📉 Suicide Rate (per 100k)")
            fig = px.choropleth(df, locations="iso_code", color="Suicide_Rate_100k", hover_name="Country", color_continuous_scale="Viridis")
            fig.update_layout(template="plotly_dark", geo=dict(bgcolor="#0e1117"))
            st.plotly_chart(fig, use_container_width=True)
        with t3:
            st.markdown("### 🎗️ HIV/AIDS Prevalence (%)")
            fig = px.choropleth(df, locations="iso_code", color="AIDS_Prevalence_Pct", hover_name="Country", color_continuous_scale="Plasma")
            fig.update_layout(template="plotly_dark", geo=dict(bgcolor="#0e1117"))
            st.plotly_chart(fig, use_container_width=True)
    except: st.error("Data missing. Run 'etl_health_unified.py'.")

# 3. SECURITY MONITOR
elif selection == "3. Security Monitor":
    st.title("🛡️ SECURITY MONITOR")
    st.markdown("##### 📡 Live Feed: Global Conflict & Protest Events")
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
    st.caption("ℹ️ **Legend:** Data represents the sentiment polarity (Positive/Negative) of historical events and publications involving Donald Trump over the last 40 years, tracked via NLP analysis.")
    try:
        df = pd.read_csv("trump_real_timeline.csv")
        fig = px.scatter(df, x="Year", y="Sentiment_Score", color="Category", hover_data=["Event"], 
                         color_discrete_map={"Positive":"#00ff00", "Negative":"#ff0000", "Neutral":"#888888"})
        fig.update_layout(template="plotly_dark", height=500)
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(df[['Year', 'Event', 'Category']], hide_index=True)
    except: st.error("Data missing.")

# 5. UNDERWORLD ASSET TRACKER
elif selection == "5. Underworld Asset Tracker":
    st.title("💀 UNDERWORLD ASSET TRACKER")
    st.markdown("### 💰 Confiscated Wealth & Contraband")
    st.caption("ℹ️ **Legend:** This ledger tracks specific verified seizures (Drugs, Money, Weapons) linked to criminal groups.")
    
    try:
        df = pd.read_csv("seizure_log.csv")
        
        col1, col2 = st.columns(2)
        col1.metric("Seizure Events Logged", len(df))
        col2.metric("Groups Impacted", df['Group'].nunique())
        
        search = st.text_input("🔍 Search Logs (e.g., 'Cocaine', 'Sinaloa', '2023')")
        if search: df = df[df.apply(lambda row: search.lower() in str(row).lower(), axis=1)]

        st.dataframe(
            df[['Year', 'Group', 'Seized Assets', 'Source_Link']],
            column_config={
                "Source_Link": st.column_config.LinkColumn("Source"),
                "Seized Assets": st.column_config.TextColumn("Confiscated Items", width="medium"),
            }, hide_index=True, use_container_width=True
        )
        
        st.markdown("### 📂 Event Details")
        for i, row in df.iterrows():
            with st.expander(f"{row['Year']} - {row['Group']}: {row['Seized Assets']}"):
                st.write(f"**Context:** \"{row['Full Description']}...\"")
                st.markdown(f"[Verify Source]({row['Source_Link']})")
    except: st.error("Data missing. Run 'etl_seizures.py'.")

# 6. GLOBAL TERROR LOG
elif selection == "6. Global Terror Log":
    st.title("💣 GLOBAL TERROR MONITOR")
    st.caption("ℹ️ **Legend:** Visualizing verified terrorist incidents from 2023-2024. Map intensity reflects total deaths per country.")
    
    try:
        df = pd.read_csv("global_terror_log.csv")
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Total Incidents", len(df))
        c2.metric("Total Deaths", df['Deaths'].sum())
        c3.metric("Countries Affected", df['Country'].nunique())
        st.divider()

        # 1. MAP
        st.markdown("### 🚨 Impact Map: Deaths by Country")
        df_map = df.groupby('Country')['Deaths'].sum().reset_index()
        fig_map = px.choropleth(df_map, locations="Country", locationmode="country names",
                            color="Deaths", hover_name="Country", color_continuous_scale="Reds")
        fig_map.update_layout(template="plotly_dark", geo=dict(bgcolor="#0e1117", showlakes=False))
        st.plotly_chart(fig_map, use_container_width=True)

        # 2. DEADLIEST ATTACKS TABLE
        st.markdown("### ⚰️ Deadliest Attacks (Specific Locations)")
        df_sorted = df.sort_values('Deaths', ascending=False).head(10)
        st.dataframe(
            df_sorted[['Date', 'Location', 'Deaths', 'Perpetrator']],
            hide_index=True, use_container_width=True
        )
        
        # 3. FULL LOG
        with st.expander("View Full Incident Log"):
            st.dataframe(df[['Date', 'Location', 'Deaths', 'Source_Link']], column_config={"Source_Link": st.column_config.LinkColumn("Source")}, hide_index=True)

    except: st.error("Data missing.")

# 7. AUTISM DIAGNOSIS
elif selection == "7. Autism Diagnosis History":
    st.title("🧩 DIAGNOSIS TIMELINE")
    try:
        df = pd.read_csv("autism_diagnosis_timeline.csv")
        for i, row in df.iterrows():
            color = "#95a5a6" if row['Year'] < 1980 else "#f1c40f" if row['Year'] < 2000 else "#e74c3c"
            with st.container():
                c1, c2 = st.columns([1, 3])
                with c1:
                    st.markdown(f"<h2 style='text-align: right; color: {color}'>{row['Year']}</h2>", unsafe_allow_html=True)
                    if 'Prevalence' in row:
                        st.markdown(f"<p style='text-align: right; font-weight:bold'>{row['Prevalence']}</p>", unsafe_allow_html=True)
                with c2:
                    st.markdown(f"<div style='border-left: 4px solid {color}; padding-left: 15px; margin-bottom: 20px;'>"
                                f"<h4 style='margin:0'>{row['Authority']}</h4>"
                                f"<h5 style='margin:0; color: #00d4ff'>{row['Definition']}</h5>"
                                f"<p>{row['Context']}</p><p style='font-size:0.85em; background-color:#1f2937; padding:10px; border-radius:5px'>{row.get('Symptoms', '')}</p></div>", unsafe_allow_html=True)
    except: st.error("Data missing.")