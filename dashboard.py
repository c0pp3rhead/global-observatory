import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import pydeck as pdk
from datetime import datetime

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Global Observatory",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. CUSTOM CSS (Dark Mode) ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    h1, h2, h3 { font-family: 'Helvetica Neue', sans-serif; font-weight: 800; color: #f0f2f6; }
    .stMetric { background-color: #1f2937; padding: 15px; border-radius: 5px; border-left: 5px solid #FF4B4B; }
    hr { border-color: #2c3e50; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
st.sidebar.title("📡 NAVIGATION")
st.sidebar.markdown("Select a module to view live data:")

options = [
    "1. Weather & Economy",
    "2. Global Health (Bio-Radar)",
    "3. Energy & CO2",
    "4. Terrorism & Security",
    "5. Political Sentiment"
]

selection = st.sidebar.radio("", options)

st.sidebar.markdown("---")
st.sidebar.info("**Status:**\n\n🟢 Systems Online\n\n📡 Data Streams Active")

# --- 4. MAIN CONTENT AREA ---

# ==========================================
# MODULE 1: WEATHER & ECONOMY (Active)
# ==========================================
if selection == "1. Weather & Economy":
    st.title("🌧️ COMMODITY-CLIMATE MONITOR")
    st.markdown("### 📉 Analysis: Coffee Futures vs. Brazil Rainfall")
    st.markdown("This module correlates real-time financial markets with historical weather patterns in Minas Gerais, Brazil.")
    st.markdown("---")

    try:
        df = pd.read_csv("coffee_weather_master.csv")
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.dropna().sort_values('Date')
        
        # Date Filter
        min_date = df['Date'].min()
        max_date = df['Date'].max()
        col1, col2 = st.columns([3, 1])
        with col1:
            start_date, end_date = st.slider(
                "Time Window",
                min_value=min_date.date(),
                max_value=max_date.date(),
                value=(datetime(2015, 1, 1).date(), max_date.date())
            )

        # Filter Logic
        mask = (df['Date'].dt.date >= start_date) & (df['Date'].dt.date <= end_date)
        df_filtered = df.loc[mask]
        
        # Metrics
        latest = df_filtered.iloc[-1]
        if len(df_filtered) > 1:
            prev = df_filtered.iloc[-2]
            price_change = latest['Close_Price'] - prev['Close_Price']
            rain_change = latest['Rolling_Rain_30d'] - prev['Rolling_Rain_30d']
        else:
            price_change, rain_change = 0, 0

        m1, m2, m3 = st.columns(3)
        m1.metric("Coffee Futures (KC=F)", f"${latest['Close_Price']:.2f}", f"{price_change:.2f}")
        m2.metric("30-Day Rain (Minas Gerais)", f"{latest['Rolling_Rain_30d']:.1f} mm", f"{rain_change:.1f} mm")
        
        # Correlation
        corr = df_filtered['Close_Price'].corr(df_filtered['Rolling_Rain_30d'])
        m3.metric("Correlation Coefficient", f"{corr:.2f}")

        # Visualization
        fig = go.Figure()
        fig.add_trace(go.Bar(x=df_filtered['Date'], y=df_filtered['Rolling_Rain_30d'], name="Rainfall (mm)", marker_color='rgba(52, 152, 219, 0.5)', yaxis='y2'))
        fig.add_trace(go.Scatter(x=df_filtered['Date'], y=df_filtered['Close_Price'], name="Price ($)", line=dict(color='#FF4B4B')))
        
        fig.update_layout(
            template="plotly_dark", 
            height=500,
            title_text="Impact of Drought on Coffee Prices",
            yaxis=dict(title=dict(text="Price ($)", font=dict(color="#FF4B4B")), tickfont=dict(color="#FF4B4B")),
            yaxis2=dict(title=dict(text="Rain (mm)", font=dict(color="#3498db")), tickfont=dict(color="#3498db"), overlaying='y', side='right'),
            legend=dict(x=0, y=1.1, orientation="h")
        )
        st.plotly_chart(fig, use_container_width=True)

    except FileNotFoundError:
        st.error("⚠️ Data missing. Please run 'etl_weather.py' locally.")

# ==========================================
# MODULE 2: GLOBAL HEALTH (Active)
# ==========================================
elif selection == "2. Global Health (Bio-Radar)":
    st.title("🧬 THE BIO-RADAR")
    st.markdown("### 🗺️ Visualization: Global Mortality Trends")
    st.markdown("An interactive geospatial analysis of Crude Death Rates (per 1,000 people) sourced from the World Bank.")
    st.markdown("---")

    try:
        df_health = pd.read_csv("health_death_rates.csv")
        
        # Slider for Year
        min_year = int(df_health['Year'].min())
        max_year = int(df_health['Year'].max())
        
        col1, col2 = st.columns([3, 1])
        with col1:
            selected_year = st.slider("Select Year to Observe", min_year, max_year, 2021)
        
        # Filter Data
        df_year = df_health[df_health['Year'] == selected_year]
        
        # MAP VISUALIZATION
        fig_map = px.scatter_geo(
            df_year,
            locations="Country",
            locationmode="country names",
            size="Death_Rate",
            hover_name="Country",
            projection="natural earth",
            color="Death_Rate",
            color_continuous_scale="Reds",
            size_max=40,
            title=f"Global Death Rates in {selected_year}"
        )
        
        fig_map.update_layout(
            template="plotly_dark",
            geo=dict(bgcolor='#0e1117', landcolor='#2c3e50', oceancolor='#0e1117', showlakes=False, coastlinecolor='#95a5a6'),
            margin=dict(l=0, r=0, t=50, b=0),
            height=600
        )
        
        st.plotly_chart(fig_map, use_container_width=True)
        
        with st.expander("📂 View Top 10 Mortality Rates"):
            st.table(df_year.sort_values("Death_Rate", ascending=False).head(10)[['Country', 'Death_Rate']])

    except FileNotFoundError:
        st.error("⚠️ Data missing. Please run 'etl_health.py' locally.")

# ==========================================
# MODULE 3: ENERGY & CO2 (Active)
# ==========================================
elif selection == "3. Energy & CO2":
    st.title("⚡ THE GREENFLATION MONITOR")
    st.markdown("### 🛢️ Macro Analysis: Oil Prices vs. Global Emissions")
    st.markdown("Does expensive energy force the world to reduce emissions? This tool correlates **Brent Crude Oil Prices** with **Global CO2 Output**.")
    st.markdown("---")

    try:
        df_energy = pd.read_csv("energy_oil_co2.csv")
        
        # Metrics
        latest_energy = df_energy.iloc[-1]
        prev_energy = df_energy.iloc[-2]
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Avg Oil Price (Yearly)", f"${latest_energy['Avg_Oil_Price']:.2f}")
        with c2:
            co2_delta = latest_energy['Global_CO2_MillionTons'] - prev_energy['Global_CO2_MillionTons']
            st.metric("Global CO2 (Million Tons)", f"{latest_energy['Global_CO2_MillionTons']:,.0f}", f"{co2_delta:,.0f}")
        with c3:
            corr_energy = df_energy['Avg_Oil_Price'].corr(df_energy['Global_CO2_MillionTons'])
            st.metric("Price-Emission Correlation", f"{corr_energy:.2f}")

        # Dual Axis Chart
        fig_energy = go.Figure()

        fig_energy.add_trace(go.Scatter(
            x=df_energy['Year'], 
            y=df_energy['Global_CO2_MillionTons'],
            name="Global CO2 Emissions",
            fill='tozeroy',
            mode='none',
            fillcolor='rgba(231, 76, 60, 0.3)'
        ))

        fig_energy.add_trace(go.Scatter(
            x=df_energy['Year'], 
            y=df_energy['Avg_Oil_Price'],
            name="Oil Price ($/Barrel)",
            yaxis='y2',
            line=dict(color='#f1c40f', width=3)
        ))

        # FIXED FOR PLOTLY 6.0 (Nested font dictionaries)
        fig_energy.update_layout(
            template="plotly_dark",
            title="Correlation: Cost of Energy vs. Carbon Output",
            height=500,
            xaxis=dict(title="Year"),
            yaxis=dict(title="Global CO2 (Million Tons)", showgrid=False),
            yaxis2=dict(
                title=dict(text="Oil Price ($)", font=dict(color="#f1c40f")), 
                overlaying='y', 
                side='right',
                tickfont=dict(color="#f1c40f")
            ),
            legend=dict(x=0, y=1.1, orientation="h")
        )

        st.plotly_chart(fig_energy, use_container_width=True)
        st.info("💡 **Analyst Note:** A positive correlation suggests that emissions continue to rise regardless of energy price volatility, indicating inelastic demand for fossil fuels.")

    except FileNotFoundError:
        st.error("⚠️ Data missing. Please run 'etl_energy.py' locally.")

# ==========================================
# MODULE 4: SECURITY (Active)
# ==========================================
elif selection == "4. Terrorism & Security":
    st.title("🛡️ GLOBAL SECURITY MONITOR")
    st.markdown("### 🚨 Live Feed: Counternarcotics Operations (Last 24h)")
    st.markdown("Real-time extraction of 'Seizure' and 'Trafficking' events from the GDELT Global News Stream.")
    st.markdown("---")

    try:
        df_sec = pd.read_csv("security_events.csv")
        
        # Metrics
        total_events = len(df_sec)
        if not df_sec.empty:
            top_hotspot = df_sec.sort_values('Article_Count', ascending=False).iloc[0]['Location']
        else:
            top_hotspot = "None"
        
        m1, m2 = st.columns(2)
        m1.metric("Verified Events (24h)", total_events)
        m2.metric("Top Reporting Hotspot", top_hotspot)

        # PYDECK MAP (Hexagon Layer)
        layer = pdk.Layer(
            "HexagonLayer",
            df_sec,
            get_position=["Longitude", "Latitude"],
            auto_highlight=True,
            elevation_scale=50,
            pickable=True,
            elevation_range=[0, 3000],
            extruded=True,                 
            coverage=1
        )

        view_state = pdk.ViewState(
            longitude=-75.0, # Centered on Americas
            latitude=10.0,
            zoom=2,
            min_zoom=1,
            max_zoom=15,
            pitch=40.5,
            bearing=-27.36
        )

        st.pydeck_chart(pdk.Deck(
            map_style='mapbox://styles/mapbox/dark-v10',
            initial_view_state=view_state,
            layers=[layer],
            tooltip={"text": "Event Density: {elevationValue}"}
        ))
        
        st.markdown("### 📰 Live Wire: Latest Reports")
        st.dataframe(
            df_sec[['Location', 'Article_Count', 'Source_URL']],
            column_config={"Source_URL": st.column_config.LinkColumn("News Source")},
            hide_index=True
        )

    except FileNotFoundError:
        st.error("⚠️ Data missing. Please run 'etl_security.py' locally.")

# ==========================================
# MODULE 5: POLITICS (Active)
# ==========================================
elif selection == "5. Political Sentiment":
    st.title("🗳️ THE AGENDA SETTER")
    st.markdown("### 🧠 NLP Analysis: Media Sentiment on 'Donald Trump'")
    st.markdown("We use Natural Language Processing (TextBlob) to scan real-time headlines and score them for **Positivity** vs. **Negativity**.")
    st.markdown("---")

    try:
        df_pol = pd.read_csv("politics_sentiment.csv")
        
        # Metrics
        avg_sentiment = df_pol['Sentiment_Score'].mean()
        # Convert score to emoji/text
        if avg_sentiment > 0.05:
            sent_status = "Positive 🟢"
        elif avg_sentiment < -0.05:
            sent_status = "Negative 🔴"
        else:
            sent_status = "Neutral ⚪"
            
        article_count = len(df_pol)
        
        c1, c2 = st.columns(2)
        c1.metric("Current Media Tone", sent_status, f"{avg_sentiment:.3f} Polarity")
        c2.metric("Articles Analyzed (Live)", article_count)

        # SCATTER PLOT (The "Discource Map")
        # X = Subjectivity (Fact vs Opinion)
        # Y = Polarity (Happy vs Angry)
        
        fig_pol = px.scatter(
            df_pol,
            x="Subjectivity_Score",
            y="Sentiment_Score",
            color="Category",
            hover_data=["Title", "Source"],
            color_discrete_map={"Positive": "#2ecc71", "Negative": "#e74c3c", "Neutral": "#95a5a6"},
            title="Media Landscape: Fact vs. Opinion & Tone"
        )
        
        # Add 'Crosshairs' to divide the quadrants
        fig_pol.add_hline(y=0, line_width=1, line_dash="dash", line_color="white")
        fig_pol.add_vline(x=0.5, line_width=1, line_dash="dash", line_color="white")
        
        fig_pol.update_layout(
            template="plotly_dark",
            height=600,
            xaxis=dict(title="Subjectivity (0=Fact, 1=Opinion)", range=[-0.1, 1.1]),
            yaxis=dict(title="Sentiment (Negative ↔ Positive)", range=[-1.1, 1.1]),
            legend=dict(orientation="h", y=1.1)
        )
        
        st.plotly_chart(fig_pol, use_container_width=True)
        
        # Data Table
        st.markdown("### 📰 Ranked Headlines")
        # Filter buttons
        filter_opt = st.radio("Show:", ["All", "Positive Only", "Negative Only"], horizontal=True)
        
        if filter_opt == "Positive Only":
            df_show = df_pol[df_pol['Category'] == "Positive"]
        elif filter_opt == "Negative Only":
            df_show = df_pol[df_pol['Category'] == "Negative"]
        else:
            df_show = df_pol
            
        st.dataframe(
            df_show[['Date', 'Title', 'Source', 'Sentiment_Score']],
            hide_index=True
        )

    except FileNotFoundError:
        st.error("⚠️ Data missing. Please run 'etl_politics.py' locally.")
