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

# --- 2. CUSTOM CSS (FIX: High Contrast & Mobile Stability) ---
st.markdown("""
    <style>
    /* Force main background to dark */
    .stApp {
        background-color: #0e1117;
    }
    
    /* FIX: Force all headers to be white for legibility */
    h1, h2, h3, h4, h5, h6, .stMarkdown, p {
        font-family: 'Helvetica Neue', sans-serif !important;
        color: #fafafa !important;
    }
    
    /* FIX: Metric Cards High Contrast */
    div[data-testid="stMetricValue"] {
        color: #fafafa !important;
    }
    div[data-testid="stMetricLabel"] {
        color: #d1d5db !important; /* Light gray for labels */
    }
    
    /* Metric Card Background */
    .stMetric {
        background-color: #1f2937;
        padding: 15px;
        border-radius: 5px;
        border-left: 5px solid #FF4B4B;
    }
    
    /* FIX: Prevent Chart Overflow on Mobile */
    .js-plotly-plot {
        max-width: 100%;
    }
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

# --- HELPER FUNCTION: Mobile Chart Config ---
# FIX: Disables zooming/panning on mobile so you can scroll the page easily
def get_chart_config():
    return {
        'displayModeBar': False,  # Hides the floating toolbar
        'scrollZoom': False,      # FIX: Prevents "infinite scroll" inside chart
        'staticPlot': False       # Keeps tooltips working
    }

# --- 4. MAIN CONTENT AREA ---

# ==========================================
# MODULE 1: WEATHER & ECONOMY
# ==========================================
if selection == "1. Weather & Economy":
    st.title("🌧️ COMMODITY-CLIMATE MONITOR")
    st.markdown("### 📉 Analysis: Coffee Futures vs. Brazil Rainfall")
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
        m1.metric("Coffee Futures", f"${latest['Close_Price']:.2f}", f"{price_change:.2f}")
        m2.metric("30-Day Rain", f"{latest['Rolling_Rain_30d']:.1f} mm", f"{rain_change:.1f}")
        
        corr = df_filtered['Close_Price'].corr(df_filtered['Rolling_Rain_30d'])
        m3.metric("Correlation", f"{corr:.2f}")

        # Visualization
        fig = go.Figure()
        fig.add_trace(go.Bar(x=df_filtered['Date'], y=df_filtered['Rolling_Rain_30d'], name="Rain", marker_color='rgba(52, 152, 219, 0.5)', yaxis='y2'))
        fig.add_trace(go.Scatter(x=df_filtered['Date'], y=df_filtered['Close_Price'], name="Price", line=dict(color='#FF4B4B')))
        
        fig.update_layout(
            template="plotly_dark", 
            height=450, # FIX: Fixed height to prevent layout shift
            margin=dict(l=10, r=10, t=40, b=10), # FIX: Tighter margins for mobile
            yaxis=dict(title=dict(text="Price ($)", font=dict(color="#FF4B4B")), tickfont=dict(color="#FF4B4B")),
            yaxis2=dict(title=dict(text="Rain (mm)", font=dict(color="#3498db")), tickfont=dict(color="#3498db"), overlaying='y', side='right'),
            legend=dict(x=0, y=1.1, orientation="h"),
            dragmode=False # FIX: Disables drag-to-zoom
        )
        st.plotly_chart(fig, use_container_width=True, config=get_chart_config())

    except FileNotFoundError:
        st.error("⚠️ Data missing.")

# ==========================================
# MODULE 2: GLOBAL HEALTH
# ==========================================
elif selection == "2. Global Health (Bio-Radar)":
    st.title("🧬 THE BIO-RADAR")
    st.markdown("### 🗺️ Visualization: Global Mortality Trends")
    st.markdown("---")

    try:
        df_health = pd.read_csv("health_death_rates.csv")
        min_year = int(df_health['Year'].min())
        max_year = int(df_health['Year'].max())
        
        selected_year = st.slider("Select Year", min_year, max_year, 2021)
        df_year = df_health[df_health['Year'] == selected_year]
        
        fig_map = px.scatter_geo(
            df_year,
            locations="Country",
            locationmode="country names",
            size="Death_Rate",
            hover_name="Country",
            projection="natural earth",
            color="Death_Rate",
            color_continuous_scale="Reds",
            size_max=35,
            title=f"Global Death Rates in {selected_year}"
        )
        
        fig_map.update_layout(
            template="plotly_dark",
            geo=dict(bgcolor='#0e1117', landcolor='#2c3e50', oceancolor='#0e1117', showlakes=False, coastlinecolor='#95a5a6'),
            margin=dict(l=0, r=0, t=30, b=0),
            height=500,
            dragmode=False # FIX: Better map stability
        )
        
        st.plotly_chart(fig_map, use_container_width=True, config=get_chart_config())
        
        with st.expander("📂 View Top 10 Mortality Rates"):
            st.table(df_year.sort_values("Death_Rate", ascending=False).head(10)[['Country', 'Death_Rate']])

    except FileNotFoundError:
        st.error("⚠️ Data missing.")

# ==========================================
# MODULE 3: ENERGY & CO2
# ==========================================
elif selection == "3. Energy & CO2":
    st.title("⚡ THE GREENFLATION MONITOR")
    st.markdown("### 🛢️ Macro: Oil Prices vs. Emissions")
    st.markdown("---")

    try:
        df_energy = pd.read_csv("energy_oil_co2.csv")
        latest_energy = df_energy.iloc[-1]
        
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Avg Oil Price", f"${latest_energy['Avg_Oil_Price']:.2f}")
        with c2:
            st.metric("Global CO2 (M Tons)", f"{latest_energy['Global_CO2_MillionTons']:,.0f}")

        fig_energy = go.Figure()

        fig_energy.add_trace(go.Scatter(
            x=df_energy['Year'], 
            y=df_energy['Global_CO2_MillionTons'],
            name="CO2",
            fill='tozeroy',
            mode='none',
            fillcolor='rgba(231, 76, 60, 0.3)'
        ))

        fig_energy.add_trace(go.Scatter(
            x=df_energy['Year'], 
            y=df_energy['Avg_Oil_Price'],
            name="Oil ($)",
            yaxis='y2',
            line=dict(color='#f1c40f', width=3)
        ))

        fig_energy.update_layout(
            template="plotly_dark",
            height=450, # FIX: Fixed height
            margin=dict(l=10, r=10, t=40, b=10),
            xaxis=dict(title="Year"),
            yaxis=dict(title="CO2", showgrid=False),
            yaxis2=dict(
                title=dict(text="Oil ($)", font=dict(color="#f1c40f")), 
                overlaying='y', 
                side='right',
                tickfont=dict(color="#f1c40f")
            ),
            legend=dict(x=0, y=1.1, orientation="h"),
            dragmode=False # FIX: Disable Zoom
        )

        st.plotly_chart(fig_energy, use_container_width=True, config=get_chart_config())

    except FileNotFoundError:
        st.error("⚠️ Data missing.")

# ==========================================
# MODULE 4: SECURITY
# ==========================================
elif selection == "4. Terrorism & Security":
    st.title("🛡️ SECURITY MONITOR")
    st.markdown("### 🚨 Live Feed: Drug Interdictions")
    st.markdown("---")

    try:
        df_sec = pd.read_csv("security_events.csv")
        total_events = len(df_sec)
        
        st.metric("Verified Events (24h)", total_events)

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
            longitude=-75.0, 
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
            tooltip={"text": "Density: {elevationValue}"}
        ))
        
        st.markdown("### 📰 Latest Reports")
        st.dataframe(
            df_sec[['Location', 'Article_Count', 'Source_URL']],
            column_config={"Source_URL": st.column_config.LinkColumn("Source")},
            hide_index=True
        )

    except FileNotFoundError:
        st.error("⚠️ Data missing.")

# ==========================================
# MODULE 5: POLITICS
# ==========================================
elif selection == "5. Political Sentiment":
    st.title("🗳️ THE AGENDA SETTER")
    st.markdown("### 🧠 NLP Analysis: 'Donald Trump'")
    st.markdown("---")

    try:
        df_pol = pd.read_csv("politics_sentiment.csv")
        avg_sentiment = df_pol['Sentiment_Score'].mean()
        
        if avg_sentiment > 0.05:
            sent_status = "Positive 🟢"
        elif avg_sentiment < -0.05:
            sent_status = "Negative 🔴"
        else:
            sent_status = "Neutral ⚪"
            
        c1, c2 = st.columns(2)
        c1.metric("Media Tone", sent_status)
        c2.metric("Articles", len(df_pol))

        fig_pol = px.scatter(
            df_pol,
            x="Subjectivity_Score",
            y="Sentiment_Score",
            color="Category",
            color_discrete_map={"Positive": "#2ecc71", "Negative": "#e74c3c", "Neutral": "#95a5a6"},
            title="Fact vs. Opinion & Tone"
        )
        
        fig_pol.add_hline(y=0, line_width=1, line_dash="dash", line_color="white")
        fig_pol.add_vline(x=0.5, line_width=1, line_dash="dash", line_color="white")
        
        fig_pol.update_layout(
            template="plotly_dark",
            height=500,
            margin=dict(l=10, r=10, t=40, b=10),
            xaxis=dict(title="Subjectivity", range=[-0.1, 1.1]),
            yaxis=dict(title="Sentiment", range=[-1.1, 1.1]),
            legend=dict(orientation="h", y=1.1),
            dragmode=False # FIX: Disable Zoom
        )
        
        st.plotly_chart(fig_pol, use_container_width=True, config=get_chart_config())
        
        st.markdown("### 📰 Headlines")
        st.dataframe(df_pol[['Title', 'Sentiment_Score']], hide_index=True)

    except FileNotFoundError:
        st.error("⚠️ Data missing.")
