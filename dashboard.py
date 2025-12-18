import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, date

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Global Observatory",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    h1, h2, h3, h4, h5, h6, .stMarkdown, p { font-family: 'Helvetica Neue', sans-serif !important; color: #fafafa !important; }
    div[data-testid="stMetricValue"] { color: #fafafa !important; }
    div[data-testid="stMetricLabel"] { color: #d1d5db !important; }
    .stMetric { background-color: #1f2937; padding: 15px; border-radius: 5px; border-left: 5px solid #FF4B4B; }
    .js-plotly-plot { max-width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# --- HELPER CONFIGS ---
def get_chart_config():
    return {'displayModeBar': False, 'scrollZoom': False, 'staticPlot': False}

COLOR_PRIMARY = "#00d4ff"
COLOR_SECONDARY = "#ff007f"
COLOR_TERTIARY = "#f1c40f"
COLOR_BACKGROUND = "#0e1117"
COLOR_GRID = "#2c3e50"

def apply_magazine_theme(fig):
    fig.update_layout(
        template="plotly_dark",
        plot_bgcolor=COLOR_BACKGROUND,
        paper_bgcolor=COLOR_BACKGROUND,
        font=dict(family="Helvetica Neue", color="#fafafa"),
        xaxis=dict(showgrid=True, gridcolor=COLOR_GRID, gridwidth=0.5, zeroline=False),
        yaxis=dict(showgrid=True, gridcolor=COLOR_GRID, gridwidth=0.5, zeroline=False),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, bgcolor="rgba(0,0,0,0)"),
        margin=dict(l=10, r=10, t=50, b=10),
        height=450,
        dragmode=False
    )
    return fig

# --- 3. SIDEBAR NAVIGATION ---
st.sidebar.title("📡 NAVIGATION")
options = ["1. Weather & Economy", "2. Global Health (Bio-Radar)", "3. Energy & CO2", "4. Terrorism & Security", "5. Political Sentiment"]
selection = st.sidebar.radio("Select Module:", options)
st.sidebar.markdown("---")
st.sidebar.info("**Status:**\n\n🟢 Systems Online\n\n📡 Data Streams Active")

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
        min_date, max_date = df['Date'].min(), df['Date'].max()
        col1, col2 = st.columns([3, 1])
        with col1:
            start, end = st.slider("Time Window", min_value=min_date.date(), max_value=max_date.date(), value=(datetime(2015,1,1).date(), max_date.date()))
        df_filtered = df[(df['Date'].dt.date >= start) & (df['Date'].dt.date <= end)]
        
        latest = df_filtered.iloc[-1]
        m1, m2, m3 = st.columns(3)
        m1.metric("Coffee Futures", f"${latest['Close_Price']:.2f}")
        m2.metric("30-Day Rain", f"{latest['Rolling_Rain_30d']:.1f} mm")
        m3.metric("Correlation", f"{df_filtered['Close_Price'].corr(df_filtered['Rolling_Rain_30d']):.2f}")

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df_filtered['Date'], y=df_filtered['Close_Price'], name="Price ($)", line=dict(color=COLOR_SECONDARY, width=2.5)))
        fig.add_trace(go.Scatter(x=df_filtered['Date'], y=df_filtered['Rolling_Rain_30d'], name="Rain (mm)", line=dict(color=COLOR_PRIMARY, width=2.5), yaxis='y2'))
        fig = apply_magazine_theme(fig)
        fig.update_layout(yaxis2=dict(title="Rain (mm)", overlaying='y', side='right', showgrid=False))
        st.plotly_chart(fig, use_container_width=True, config=get_chart_config())
    except: st.error("⚠️ Data missing.")

# ==========================================
# MODULE 2: GLOBAL HEALTH
# ==========================================
elif selection == "2. Global Health (Bio-Radar)":
    st.title("🧬 THE BIO-RADAR")
    st.markdown("### 🗺️ Global Mortality Trends")
    st.markdown("---")
    try:
        df_health = pd.read_csv("health_death_rates.csv")
        year = st.slider("Select Year", int(df_health['Year'].min()), int(df_health['Year'].max()), 2021)
        df_year = df_health[df_health['Year'] == year]
        
        fig_map = px.choropleth(df_year, locations="economy", color="Death_Rate", hover_name="Country", projection="natural earth", color_continuous_scale="Reds", title=f"Death Rate (per 1,000) - {year}")
        fig_map.update_layout(template="plotly_dark", geo=dict(bgcolor=COLOR_BACKGROUND, showframe=False), margin=dict(l=0,r=0,t=40,b=0), height=500)
        st.plotly_chart(fig_map, use_container_width=True, config=get_chart_config())
    except: st.error("⚠️ Data missing.")

# ==========================================
# MODULE 3: ENERGY & CO2
# ==========================================
elif selection == "3. Energy & CO2":
    st.title("⚡ THE GREENFLATION MONITOR")
    st.markdown("### 🛢️ Oil Prices vs. Emissions")
    st.markdown("---")
    try:
        df_en = pd.read_csv("energy_oil_co2.csv")
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df_en['Year'], y=df_en['Global_CO2_MillionTons'], name="CO2", line=dict(color=COLOR_PRIMARY, width=2.5)))
        fig.add_trace(go.Scatter(x=df_en['Year'], y=df_en['Avg_Oil_Price'], name="Oil ($)", yaxis='y2', line=dict(color=COLOR_TERTIARY, width=2.5)))
        fig = apply_magazine_theme(fig)
        fig.update_layout(yaxis2=dict(title="Oil ($)", overlaying='y', side='right', showgrid=False))
        st.plotly_chart(fig, use_container_width=True, config=get_chart_config())
    except: st.error("⚠️ Data missing.")

# ==========================================
# MODULE 4: SECURITY (FIXED MAP)
# ==========================================
elif selection == "4. Terrorism & Security":
    st.title("🛡️ SECURITY MONITOR")
    st.markdown("### 🚨 Live Feed: Drug Interdictions (24h)")
    st.markdown("---")
    try:
        df_sec = pd.read_csv("security_events.csv")
        st.metric("Verified Events", len(df_sec))

        # FIX: Switched to 'scatter_geo' with Natural Earth projection.
        # This prevents the "repeating world" bug and looks cleaner.
        fig_map = px.scatter_geo(
            df_sec,
            lat='Latitude',
            lon='Longitude',
            size='Article_Count', # Bubble size based on reports
            color='Article_Count',
            hover_name="Location",
            projection="natural earth", # The Professional Projection
            color_continuous_scale="Plasma",
            title="Global Security Hotspots",
            size_max=25
        )
        
        fig_map.update_layout(
            template="plotly_dark",
            geo=dict(
                bgcolor=COLOR_BACKGROUND,
                landcolor='#1f2937', # Darker land
                oceancolor=COLOR_BACKGROUND,
                showlakes=False,
                coastlinecolor='#374151',
                showcountries=True,
                countrycolor='#374151'
            ),
            margin=dict(l=0, r=0, t=40, b=0),
            height=500
        )

        st.plotly_chart(fig_map, use_container_width=True, config=get_chart_config())
        
        st.markdown("### 📰 Latest Reports")
        st.dataframe(df_sec[['Location', 'Article_Count', 'Source_URL']], hide_index=True)
    except: st.error("⚠️ Data missing.")

# ==========================================
# MODULE 5: POLITICS (LIFETIME UPDATE)
# ==========================================
elif selection == "5. Political Sentiment":
    st.title("🗳️ THE AGENDA SETTER")
    st.markdown("### 🧠 Media Tone: Donald Trump (Lifetime Analysis)")
    st.markdown("Tracking media sentiment polarity across 40+ years of public life.")
    st.markdown("---")

    try:
        # Load Historical Data
        df_hist = pd.read_csv("trump_historical_timeline.csv")
        df_hist['Date'] = pd.to_datetime(df_hist['Date'])
        
        # 1. Date Range Filter
        min_date = df_hist['Date'].min().date()
        max_date = df_hist['Date'].max().date()
        
        col1, col2 = st.columns([3,1])
        with col1:
            start_d, end_d = st.slider(
                "Select Era", 
                min_value=min_date, 
                max_value=max_date, 
                value=(date(2015, 1, 1), max_date),
                format="YYYY-MM"
            )
            
        # Filter Data
        mask = (df_hist['Date'].dt.date >= start_d) & (df_hist['Date'].dt.date <= end_d)
        df_filtered = df_hist.loc[mask]
        
        # Metrics
        avg_sent = df_filtered['Sentiment_Score'].mean()
        status = "Positive 🟢" if avg_sent > 0.05 else "Negative 🔴" if avg_sent < -0.05 else "Neutral ⚪"
        st.metric("Avg Tone (Selected Period)", status, f"{avg_sent:.3f}")

        # Visualization: Area Chart (Evolution of Tone)
        # We calculate a rolling average to smooth the noise
        df_filtered['Rolling_Sentiment'] = df_filtered['Sentiment_Score'].rolling(4).mean()
        
        fig_pol = go.Figure()
        
        # Add Era Shading (Background)
        fig_pol.add_trace(go.Scatter(
            x=df_filtered['Date'], 
            y=df_filtered['Rolling_Sentiment'],
            mode='lines',
            name='Sentiment Trend',
            fill='tozeroy', # Area chart
            line=dict(color=COLOR_PRIMARY, width=2)
        ))
        
        fig_pol = apply_magazine_theme(fig_pol)
        fig_pol.update_layout(
            title="Media Sentiment Evolution",
            yaxis=dict(title="Sentiment Polarity (-1 to +1)", range=[-1, 1]),
            xaxis=dict(title="Timeline")
        )
        
        st.plotly_chart(fig_pol, use_container_width=True, config=get_chart_config())
        
        with st.expander("📚 View Era Breakdown"):
             st.dataframe(df_filtered.groupby('Era')['Sentiment_Score'].mean().reset_index().sort_values('Sentiment_Score'), hide_index=True)

    except FileNotFoundError:
        st.error("⚠️ Historical Data missing. Please run 'generate_history.py'.")

# --- METHODOLOGY ---
st.markdown("---")
with st.expander("📚 Methodology & Sources"):
    st.markdown("Data sources: World Bank, GDELT Project, Open-Meteo, Yahoo Finance. Historical sentiment data is simulated for demonstration.")
