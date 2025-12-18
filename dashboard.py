import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Global Observatory",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. CUSTOM CSS (High Contrast & Mobile Stability) ---
st.markdown("""
    <style>
    /* Force main background to dark */
    .stApp {
        background-color: #0e1117;
    }
    
    /* Force all headers to be white for legibility */
    h1, h2, h3, h4, h5, h6, .stMarkdown, p {
        font-family: 'Helvetica Neue', sans-serif !important;
        color: #fafafa !important;
    }
    
    /* Metric Cards High Contrast */
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
    
    /* Prevent Chart Overflow on Mobile */
    .js-plotly-plot {
        max-width: 100%;
    }
    
    /* Methodology Section Styling */
    .methodology {
        font-size: 0.9em;
        color: #a0a0a0 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HELPER FUNCTION: Mobile Chart Config ---
def get_chart_config():
    return {
        'displayModeBar': False,  # Hides the floating toolbar
        'scrollZoom': False,      # Prevents "infinite scroll" inside chart
        'staticPlot': False       # Keeps tooltips working
    }

# --- Common Chart Theme Colors (Magazine Style) ---
COLOR_PRIMARY = "#00d4ff" # Bright Blue
COLOR_SECONDARY = "#ff007f" # Magenta/Pink
COLOR_TERTIARY = "#f1c40f" # Gold/Yellow
COLOR_BACKGROUND = "#0e1117"
COLOR_GRID = "#2c3e50"

def apply_magazine_theme(fig):
    """Applies a professional, magazine-style dark theme to Plotly charts."""
    fig.update_layout(
        template="plotly_dark",
        plot_bgcolor=COLOR_BACKGROUND,
        paper_bgcolor=COLOR_BACKGROUND,
        font=dict(family="Helvetica Neue", color="#fafafa"),
        xaxis=dict(
            showgrid=True,
            gridcolor=COLOR_GRID,
            gridwidth=0.5,
            zeroline=False
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor=COLOR_GRID,
            gridwidth=0.5,
            zeroline=False
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            bgcolor="rgba(0,0,0,0)"
        ),
        margin=dict(l=10, r=10, t=50, b=10),
        height=450,
        dragmode=False
    )
    return fig

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

        # Visualization - UPDATED: Magazine Style Line Chart
        fig = go.Figure()
        
        # Line 1: Price (Primary Axis)
        fig.add_trace(go.Scatter(
            x=df_filtered['Date'], 
            y=df_filtered['Close_Price'], 
            name="Price ($)", 
            line=dict(color=COLOR_SECONDARY, width=2.5),
            mode='lines'
        ))
        
        # Line 2: Rainfall (Secondary Axis)
        fig.add_trace(go.Scatter(
            x=df_filtered['Date'], 
            y=df_filtered['Rolling_Rain_30d'], 
            name="Rain (mm)", 
            line=dict(color=COLOR_PRIMARY, width=2.5),
            yaxis='y2',
            mode='lines'
        ))
        
        fig = apply_magazine_theme(fig)
        fig.update_layout(
            title_text="Price vs. Rainfall Correlation",
            yaxis=dict(title=dict(text="Price ($)", font=dict(color=COLOR_SECONDARY)), tickfont=dict(color=COLOR_SECONDARY)),
            yaxis2=dict(
                title=dict(text="Rain (mm)", font=dict(color=COLOR_PRIMARY)), 
                tickfont=dict(color=COLOR_PRIMARY), 
                overlaying='y', 
                side='right',
                showgrid=False # Cleaner to have grid only for primary axis
            )
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
        
        # Visualization - UPDATED: Choropleth Map (Color-coded countries)
        fig_map = px.choropleth(
            df_year,
            locations="economy", # Use ISO-3 codes for accurate mapping
            color="Death_Rate",
            hover_name="Country",
            projection="natural earth",
            color_continuous_scale="Reds",
            title=f"Crude Death Rate (per 1,000) in {selected_year}"
        )
        
        fig_map.update_layout(
            template="plotly_dark",
            geo=dict(
                bgcolor=COLOR_BACKGROUND,
                landcolor='#2c3e50',
                oceancolor=COLOR_BACKGROUND,
                showlakes=False,
                coastlinecolor='#95a5a6',
                showframe=False
            ),
            margin=dict(l=0, r=0, t=40, b=0),
            height=500,
            dragmode=False,
            coloraxis_colorbar=dict(
                title="Deaths/1k",
                thicknessmode="pixels", thickness=15,
                lenmode="pixels", len=300,
                yanchor="middle", y=0.5,
                xanchor="left", x=0.02,
                bgcolor="rgba(0,0,0,0.5)"
            )
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

        # Visualization - UPDATED: Magazine Style Line Chart
        fig_energy = go.Figure()

        # Line 1: CO2 (Primary Axis)
        fig_energy.add_trace(go.Scatter(
            x=df_energy['Year'], 
            y=df_energy['Global_CO2_MillionTons'],
            name="CO2 Emissions",
            line=dict(color=COLOR_PRIMARY, width=2.5),
            mode='lines'
        ))

        # Line 2: Oil Price (Secondary Axis)
        fig_energy.add_trace(go.Scatter(
            x=df_energy['Year'], 
            y=df_energy['Avg_Oil_Price'],
            name="Oil Price ($)",
            yaxis='y2',
            line=dict(color=COLOR_TERTIARY, width=2.5),
            mode='lines'
        ))

        fig_energy = apply_magazine_theme(fig_energy)
        fig_energy.update_layout(
            title="Global Emissions vs. Energy Cost",
            xaxis=dict(title="Year"),
            yaxis=dict(title=dict(text="CO2 (Million Tons)", font=dict(color=COLOR_PRIMARY)), tickfont=dict(color=COLOR_PRIMARY)),
            yaxis2=dict(
                title=dict(text="Oil Price ($/bbl)", font=dict(color=COLOR_TERTIARY)), 
                overlaying='y', 
                side='right',
                tickfont=dict(color=COLOR_TERTIARY),
                showgrid=False
            )
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
        
        st.metric("Verified Events (Last 24h)", total_events)

        # Visualization - UPDATED: 2D Density Heatmap
        # Using px.density_mapbox for a clean, color-coded heatmap of event occurrences.
        fig_map = px.density_mapbox(
            df_sec, 
            lat='Latitude', 
            lon='Longitude', 
            z='Article_Count', # Color intensity based on number of reports
            radius=25,
            center=dict(lat=20, lon=0), 
            zoom=1,
            mapbox_style="carto-darkmatter",
            color_continuous_scale="plasma",
            title="Global Event Density Heatmap"
        )
        
        fig_map.update_layout(
            template="plotly_dark",
            margin=dict(l=0, r=0, t=40, b=0),
            height=500,
            dragmode=False,
            coloraxis_colorbar=dict(
                title="Report Count",
                thicknessmode="pixels", thickness=15,
                lenmode="pixels", len=300,
                yanchor="middle", y=0.5,
                xanchor="left", x=0.02,
                bgcolor="rgba(0,0,0,0.5)"
            )
        )

        st.plotly_chart(fig_map, use_container_width=True, config=get_chart_config())
        
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
        
        # Data Processing for Stacked Bar Chart
        # Convert Date to datetime and extract just the date part for grouping
        df_pol['Date'] = pd.to_datetime(df_pol['Date']).dt.date
        
        # Group by Date and Category, then count the occurrences
        df_grouped = df_pol.groupby(['Date', 'Category']).size().reset_index(name='Count')
        
        # Calculate overall sentiment metrics
        avg_sentiment = df_pol['Sentiment_Score'].mean()
        if avg_sentiment > 0.05:
            sent_status = "Positive 🟢"
        elif avg_sentiment < -0.05:
            sent_status = "Negative 🔴"
        else:
            sent_status = "Neutral ⚪"
            
        c1, c2 = st.columns(2)
        c1.metric("Overall Media Tone", sent_status)
        c2.metric("Total Articles Analyzed", len(df_pol))

        # Visualization - UPDATED: Stacked Bar Chart over Time
        fig_pol = px.bar(
            df_grouped,
            x="Date",
            y="Count",
            color="Category",
            title="Daily Sentiment Breakdown",
            color_discrete_map={"Positive": "#2ecc71", "Neutral": "#95a5a6", "Negative": "#e74c3c"},
            barmode='stack'
        )
        
        fig_pol = apply_magazine_theme(fig_pol)
        fig_pol.update_layout(
            xaxis=dict(title="Date"),
            yaxis=dict(title="Article Count"),
            legend=dict(title=None) # Remove legend title for cleaner look
        )
        
        st.plotly_chart(fig_pol, use_container_width=True, config=get_chart_config())
        
        st.markdown("### 📰 Recent Headlines")
        st.dataframe(df_pol[['Date', 'Title', 'Sentiment_Score']].head(10), hide_index=True)

    except FileNotFoundError:
        st.error("⚠️ Data missing.")


# --- NEW SECTION: METHODOLOGY & SOURCES ---
st.markdown("---")
with st.expander("📚 **Methodology, Sources & Statistical Techniques**"):
    st.markdown("""
    <div class="methodology">
    This dashboard aggregates and analyzes data from multiple global sources to provide real-time insights. Below is a summary of the data pipelines and techniques used for each module.

    #### **1. Commodity-Climate Monitor**
    * **Data Sources:** * **Financial Data:** Yahoo Finance API for Coffee Futures (KC=F) historical data.
        * **Weather Data:** Open-Meteo Historical Weather API for daily rainfall in Minas Gerais, Brazil (a key coffee-producing region).
    * **Techniques:** * **ETL Pipeline:** Automated script fetches, cleans, and merges daily price and weather data.
        * **Feature Engineering:** Calculation of a 30-day rolling sum of rainfall to model cumulative weather effects.
        * **Statistical Analysis:** Pearson Correlation Coefficient is calculated to quantify the linear relationship between coffee prices and recent rainfall.

    #### **2. The Bio-Radar (Global Health)**
    * **Data Source:** The World Bank Open Data API.
    * **Metric:** crude Death Rate (per 1,000 people) - Indicator Code `SP.DYN.CDRT.IN`.
    * **Techniques:** * **ETL Pipeline:** Script uses the `wbgapi` library to fetch historical data for all countries.
        * **Data Processing:** Data is pivoted from wide to long format and cleaned of aggregate region entries.
        * **Visualization:** A Choropleth map visualizes the geospatial distribution of mortality rates using ISO-3 country codes.

    #### **3. The Greenflation Monitor (Energy & CO2)**
    * **Data Sources:** * **Energy Prices:** Yahoo Finance API for Brent Crude Oil Prices (BZ=F).
        * **Emissions Data:** Our World in Data (OWID) GitHub repository for global CO2 emissions.
    * **Techniques:** * **ETL Pipeline:** Fetches daily oil prices, resamples them to yearly averages, and merges them with yearly global CO2 data.
        * **Analysis:** A dual-axis time-series chart visualizes the long-term trend and correlation between energy costs and global carbon output.

    #### **4. Security Monitor**
    * **Data Source:** The GDELT Project (Global Database of Events, Language, and Tone) Geo 2.0 API.
    * **Query:** Real-time ingestion of news events matching keywords related to drug interdictions (e.g., "seizure," "narcotics," "trafficking") over the last 24 hours.
    * **Techniques:** * **Real-time ETL:** A Python script queries the live API, parses the resulting GeoJSON data, and extracts location coordinates and article counts.
        * **Visualization:** A 2D Density Heatmap aggregates point data to highlight regional hotspots of reported security events.

    #### **5. The Agenda Setter (Political Sentiment)**
    * **Data Source:** Google News RSS Feeds focused on specific political queries.
    * **Techniques:** * **ETL Pipeline:** Script parses the RSS feed to extract the latest headlines.
        * **NLP & Sentiment Analysis:** The `TextBlob` library is used to perform Natural Language Processing on each headline, assigning a Polarity score (-1 to +1) to classify sentiment as Positive, Negative, or Neutral.
        * **Visualization:** A stacked bar chart aggregates sentiment categories by date to show the evolving media tone.

    *Note: This project is for informational and portfolio demonstration purposes. Data is sourced from public APIs and may have inherent latencies or inaccuracies.*
    </div>
    """, unsafe_allow_html=True)
