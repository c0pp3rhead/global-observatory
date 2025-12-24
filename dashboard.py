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
    "2. Bio-Radar (Time Travel)",
    "3. Security Monitor",
    "4. Agenda Setter (Decades)",
    "5. Underworld Atlas (Deep)",
    "6. Global Terror Log (Verified)",
    "7. Autism Diagnosis History"
]
selection = st.sidebar.radio("Select Module:", options)

# 1. COMMODITY-CLIMATE
if selection == "1. Commodity-Climate":
    st.title("🌧️ COMMODITY-CLIMATE MONITOR")
    try:
        df = pd.read_csv("coffee_weather_master.csv")
        st.line_chart(df.set_index('Date')[['Close_Price', 'Rolling_Rain_30d']])
    except: st.error("Data missing.")

# 2. BIO-RADAR (TIMELINE ADDED)
elif selection == "2. Bio-Radar (Time Travel)":
    st.title("🧬 THE BIO-RADAR")
    st.markdown("### ⏳ Historical Disease Tracker")
    try:
        df = pd.read_csv("health_unified.csv")
        
        # SLIDER
        min_year = int(df['Year'].min())
        max_year = int(df['Year'].max())
        selected_year = st.slider("Select Year:", min_year, max_year, max_year)
        
        # Filter Data
        df_year = df[df['Year'] == selected_year]
        
        metric = st.selectbox("Metric:", ["Suicide_Rate_100k", "AIDS_Prevalence_Pct"])
        
        fig = px.choropleth(df_year, locations="iso_code", color=metric, 
                            hover_name="Country", 
                            color_continuous_scale="Viridis",
                            title=f"Global Map ({selected_year})")
        fig.update_layout(template="plotly_dark", geo=dict(bgcolor="#0e1117"))
        st.plotly_chart(fig, use_container_width=True)
        
    except: st.error("Data missing. Run 'etl_health_unified.py'.")

# 3. SECURITY MONITOR (LEGEND FIX)
elif selection == "3. Security Monitor":
    st.title("🛡️ SECURITY MONITOR")
    try:
        df = pd.read_csv("security_events.csv")
        st.metric("Events (24h)", len(df))
        
        fig = px.scatter_geo(df, lat='Latitude', lon='Longitude', size='Article_Count',
                             color="Article_Count", # Adds color dimension
                             color_continuous_scale="Plasma",
                             title="Live GDELT Conflict Event Feed")
        
        # Explicit Legend Title
        fig.update_layout(template="plotly_dark", geo=dict(bgcolor="#0e1117"),
                          coloraxis_colorbar=dict(title="News Volatility<br>(Article Count)"))
        st.plotly_chart(fig, use_container_width=True)
    except: st.error("Data missing.")

# 4. AGENDA SETTER
elif selection == "4. Agenda Setter (Decades)":
    st.title("🗳️ THE AGENDA SETTER")
    try:
        df = pd.read_csv("trump_real_timeline.csv")
        fig = px.scatter(df, x="Year", y="Sentiment_Score", color="Category", hover_data=["Event"], 
                         color_discrete_map={"Positive":"#00ff00", "Negative":"#ff0000", "Neutral":"#888888"})
        fig.update_layout(template="plotly_dark", height=500)
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(df[['Year', 'Event', 'Category']], hide_index=True)
    except: st.error("Data missing.")

# 5. UNDERWORLD ATLAS
elif selection == "5. Underworld Atlas (Deep)":
    st.title("💀 THE UNDERWORLD ATLAS")
    try:
        df = pd.read_csv("underworld_rich_data.csv")
        st.metric("Groups Tracked", len(df))
        
        # Simplified Table (No URL column)
        st.dataframe(
            df[['Group Name', 'Membership', 'Est. Revenue', 'Founded']], 
            hide_index=True,
            use_container_width=True
        )
        
        search = st.text_input("🔍 Search Dossier")
        if search: df = df[df.apply(lambda row: search.lower() in str(row).lower(), axis=1)]
        
        for i, row in df.iterrows():
            with st.expander(f"{row['Group Name']}"):
                c1, c2 = st.columns(2)
                c1.markdown(f"**💰 Revenue:** {row['Est. Revenue']}")
                c1.markdown(f"**🔫 Activities:** {row['Criminal Activities']}")
                c2.markdown(f"**👥 Membership:** {row['Membership']}")
                c2.markdown(f"**📅 Founded:** {row['Founded']}")
                st.markdown(f"[Link to Source]({row['Wiki_Link']})")
    except: st.error("Data missing.")

# 6. GLOBAL TERROR LOG (MAP & SOURCES)
elif selection == "6. Global Terror Log (Verified)":
    st.title("💣 GLOBAL TERROR MONITOR")
    st.markdown("### 🚨 Impact Map: Deaths by Country")
    
    try:
        df = pd.read_csv("global_terror_log.csv")
        
        # 1. MAP: Aggregate by Country
        df_map = df.groupby('Country')['Deaths'].sum().reset_index()
        
        fig = px.choropleth(df_map, locations="Country", locationmode="country names",
                            color="Deaths",
                            hover_name="Country",
                            color_continuous_scale="Reds",
                            title="Intensity of Lethal Events (Heatmap)")
        fig.update_layout(template="plotly_dark", geo=dict(bgcolor="#0e1117"))
        st.plotly_chart(fig, use_container_width=True)
        
        # 2. SOURCE TABLE
        st.markdown("### 📋 Verified Incident Log")
        
        # Display with Clickable Source Link
        st.dataframe(
            df[['Date', 'Location', 'Deaths', 'Perpetrator', 'Source_Link']],
            column_config={
                "Source_Link": st.column_config.LinkColumn("Evidence Link")
            },
            hide_index=True,
            use_container_width=True
        )
        
    except: st.error("Data missing. Run 'etl_terror.py'.")

# 7. AUTISM DIAGNOSIS HISTORY
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
                                f"<p>{row['Context']}</p></div>", unsafe_allow_html=True)
    except: st.error("Data missing.")
