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
    "5. Underworld Atlas (Deep)",
    "6. Global Terror Log",
    "7. Autism Diagnosis History"
]
selection = st.sidebar.radio("Select Module:", options)

# 1. COMMODITY
if selection == "1. Commodity-Climate":
    st.title("🌧️ COMMODITY-CLIMATE MONITOR")
    try:
        df = pd.read_csv("coffee_weather_master.csv")
        st.line_chart(df.set_index('Date')[['Close_Price', 'Rolling_Rain_30d']])
    except: st.error("Data missing.")

# 2. BIO-RADAR (FIXED MAPS)
elif selection == "2. Bio-Radar (Mortality)":
    st.title("🧬 THE BIO-RADAR")
    try:
        df = pd.read_csv("health_unified.csv")
        
        t1, t2, t3 = st.tabs(["General Death Count", "Suicide Rates (Latest)", "HIV/AIDS (Latest)"])
        
        with t1:
            st.markdown("### 💀 General Mortality (Crude Death Rate per 1k)")
            # Using 'Reds' for death
            fig = px.choropleth(df, locations="iso_code", color="General_Death_Rate_1k", hover_name="Country", color_continuous_scale="Reds")
            fig.update_layout(template="plotly_dark", geo=dict(bgcolor="#0e1117"))
            st.plotly_chart(fig, use_container_width=True)
            
        with t2:
            st.markdown("### 📉 Suicide Rate (per 100k)")
            # Using 'Viridis' for contrast
            fig = px.choropleth(df, locations="iso_code", color="Suicide_Rate_100k", hover_name="Country", color_continuous_scale="Viridis")
            fig.update_layout(template="plotly_dark", geo=dict(bgcolor="#0e1117"))
            st.plotly_chart(fig, use_container_width=True)

        with t3:
            st.markdown("### 🎗️ HIV/AIDS Prevalence (%)")
            # Using 'Plasma' for disease
            fig = px.choropleth(df, locations="iso_code", color="AIDS_Prevalence_Pct", hover_name="Country", color_continuous_scale="Plasma")
            fig.update_layout(template="plotly_dark", geo=dict(bgcolor="#0e1117"))
            st.plotly_chart(fig, use_container_width=True)
            
    except: st.error("Data missing. Run 'etl_health_unified.py'.")

# 3. SECURITY MONITOR
elif selection == "3. Security Monitor":
    st.title("🛡️ SECURITY MONITOR")
    st.markdown("##### 📡 Live Feed: Global Conflict & Protest Events")
    st.caption("Data represents real-time news volume intensity for conflict-related keywords in the last 24 hours.")
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
    try:
        df = pd.read_csv("trump_real_timeline.csv")
        fig = px.scatter(df, x="Year", y="Sentiment_Score", color="Category", hover_data=["Event"], 
                         color_discrete_map={"Positive":"#00ff00", "Negative":"#ff0000", "Neutral":"#888888"})
        fig.update_layout(template="plotly_dark", height=500)
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(df[['Year', 'Event', 'Category']], hide_index=True)
    except: st.error("Data missing.")

# 5. UNDERWORLD ATLAS (SORTED)
elif selection == "5. Underworld Atlas (Deep)":
    st.title("💀 THE UNDERWORLD ATLAS")
    try:
        df = pd.read_csv("underworld_rich_data.csv")
        st.metric("Groups Tracked", len(df))
        
        # --- CRITICAL FIX: SORT BY KNOWN DATA ---
        # Create a helper column to push "Unknown" to the bottom
        df['HasData'] = df['Membership'].apply(lambda x: 0 if str(x).lower() == 'unknown' else 1)
        df_sorted = df.sort_values('HasData', ascending=False).drop('HasData', axis=1)
        
        # Main Table
        st.dataframe(
            df_sorted[['Group Name', 'Membership', 'Est. Revenue', 'Founded']], 
            hide_index=True, use_container_width=True
        )
        
        search = st.text_input("🔍 Search Dossier")
        if search: df_sorted = df_sorted[df_sorted.apply(lambda row: search.lower() in str(row).lower(), axis=1)]
        
        for i, row in df_sorted.iterrows():
            with st.expander(f"{row['Group Name']}"):
                c1, c2 = st.columns(2)
                c1.markdown(f"**💰 Revenue:** {row['Est. Revenue']}")
                c1.markdown(f"**🔫 Activities:** {row['Criminal Activities']}")
                c2.markdown(f"**👥 Membership:** {row['Membership']}")
                c2.markdown(f"**📅 Founded:** {row['Founded']}")
                st.markdown(f"[Source Link]({row['Wiki_Link']})")
    except: st.error("Data missing.")

# 6. GLOBAL TERROR LOG (WIKIPEDIA STYLE)
elif selection == "6. Global Terror Log":
    st.title("💣 GLOBAL TERROR MONITOR")
    
    try:
        df = pd.read_csv("global_terror_log.csv")
        
        # --- 1. METRICS ROW ---
        c1, c2, c3 = st.columns(3)
        c1.metric("Total Incidents", len(df))
        c2.metric("Total Deaths", df['Deaths'].sum())
        c3.metric("Countries Affected", df['Country'].nunique())
        
        st.divider()

        # --- 2. TIMELINE CHART (Mirroring Wiki Style) ---
        st.markdown("### 📊 Attack Frequency Over Time")
        # Convert date to datetime object for sorting
        df['Date_Obj'] = pd.to_datetime(df['Date'], errors='coerce')
        # Group by Month-Year
        df_timeline = df.groupby(df['Date_Obj'].dt.to_period("M")).size().reset_index(name='Incidents')
        df_timeline['Date_Str'] = df_timeline['Date_Obj'].astype(str)
        
        fig_time = px.bar(df_timeline, x='Date_Str', y='Incidents', 
                          labels={'Date_Str': 'Month', 'Incidents': 'Attacks'},
                          color='Incidents', color_continuous_scale='Reds')
        fig_time.update_layout(template="plotly_dark", height=350, xaxis_title=None)
        st.plotly_chart(fig_time, use_container_width=True)

        # --- 3. IMPACT MAP ---
        st.markdown("### 🚨 Impact Map: Deaths by Country")
        df_map = df.groupby('Country')['Deaths'].sum().reset_index()
        
        fig_map = px.choropleth(df_map, locations="Country", locationmode="country names",
                            color="Deaths", hover_name="Country", 
                            color_continuous_scale="Reds",
                            range_color=(0, df_map['Deaths'].max())) # Fix scale
        fig_map.update_layout(template="plotly_dark", geo=dict(bgcolor="#0e1117", showlakes=False))
        st.plotly_chart(fig_map, use_container_width=True)
        
        # --- 4. DATA TABLE ---
        st.markdown("### 📋 Verified Incident Log")
        st.dataframe(
            df[['Date', 'Location', 'Deaths', 'Source_Link']],
            column_config={"Source_Link": st.column_config.LinkColumn("Source")},
            hide_index=True, use_container_width=True
        )

    except Exception as e:
        st.error(f"Data Error: {e}")

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
                        st.markdown(f"<p style='text-align: right; font-size:0.8em; color:#888'>Cases: {row.get('Est_US_Cases', '')}</p>", unsafe_allow_html=True)
                with c2:
                    st.markdown(f"<div style='border-left: 4px solid {color}; padding-left: 15px; margin-bottom: 20px;'>"
                                f"<h4 style='margin:0'>{row['Authority']}</h4>"
                                f"<h5 style='margin:0; color: #00d4ff'>{row['Definition']}</h5>"
                                f"<p style='margin-top:5px'>{row['Context']}</p>"
                                f"<p style='font-size:0.85em; background-color:#1f2937; padding:10px; border-radius:5px'><b>Symptoms:</b><br>{row.get('Symptoms', '').replace(chr(10), '<br>')}</p>"
                                f"</div>", unsafe_allow_html=True)
    except: st.error("Data missing.")
