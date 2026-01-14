import streamlit as st
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Global Pulse Observatory",
    page_icon="🔭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- HELPER FUNCTIONS ---
def get_file_list(folder_path):
    """Scans the folder and returns a sorted list of clean titles"""
    if not os.path.exists(folder_path):
        return []
    
    files = [f for f in os.listdir(folder_path) if f.endswith(".md") and f != "index.md"]
    files.sort()
    return files

def format_func(filename):
    """Removes underscores and extensions for the dropdown display"""
    return filename.replace("_", " ").replace(".md", "")

# --- SIDEBAR: DISCIPLINE SELECTOR ---
st.sidebar.title("🏛 Fields of Study")

pillars = {
    "🌱 Exoplanetary Agriculture": "research_articles/1_Exoplanetary_Agriculture",
    "📉 Climate Finance": "research_articles/2_Climate_Finance",
    "☣️ Biosecurity & Illicit Economies": "research_articles/3_Biosecurity_Illicit_Economies"
}

# 1. Select Pillar
selected_pillar = st.sidebar.radio(
    "Select Discipline:", 
    list(pillars.keys()), 
    index=0
)

st.sidebar.markdown("---")
st.sidebar.info("**Note:** Articles in the 'Biosecurity' section focus on economic impact and supply chain analysis.")

# --- MAIN PAGE: THE READER ---

# 1. Header
st.title("Cristian Morales")
st.subheader("Research Portfolio: Economics, Systems & Security")
st.markdown("---")

# 2. Context
st.header(f"Research Focus: {selected_pillar}")
if selected_pillar == "🌱 Exoplanetary Agriculture":
    st.caption("Engineering Life Support for Hostile Environments")
elif selected_pillar == "📉 Climate Finance":
    st.caption("Pricing Environmental Risk in Global Markets")
elif selected_pillar == "☣️ Biosecurity & Illicit Economies":
    st.caption("Tracking the Shadow Vectors of Globalization")

# 3. The Search Engine (The Solution)
folder_path = pillars[selected_pillar]
files = get_file_list(folder_path)

if files:
    # This creates a searchable dropdown.
    # The user types "Potato" and it finds it instantly.
    selected_file = st.selectbox(
        "🔍 Search or Select Research Note (100+ Available):",
        options=files,
        format_func=format_func, # Makes "The_Potato_Paradox.md" look like "The Potato Paradox"
        index=0
    )
    
    st.markdown("---")
    
    # 4. Render Content
    file_path = os.path.join(folder_path, selected_file)
    with open(file_path, "r") as f:
        content = f.read()
    
    # Render the article
    st.markdown(content, unsafe_allow_html=True)

else:
    st.error(f"No research notes found in {folder_path}. Please run the generators.")

# --- FOOTER ---
st.markdown("---")
st.caption("Global Pulse Observatory | Live Research Platform")
