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

# --- SIDEBAR ---
st.sidebar.title("🏛 Fields of Study")

pillars = {
    "🌱 Exoplanetary Agriculture": "research_articles/1_Exoplanetary_Agriculture",
    "📉 Climate Finance": "research_articles/2_Climate_Finance",
    "☣️ Biosecurity & Illicit Economies": "research_articles/3_Biosecurity_Illicit_Economies"
}

# 1. Pillar Selector
selected_pillar = st.sidebar.radio(
    "Select Discipline:", 
    list(pillars.keys()), 
    index=0
)

st.sidebar.markdown("---")
st.sidebar.info("Select a Discipline above, then search for an article in the main window.")

# --- MAIN PAGE ---
st.title("Cristian Morales")
st.subheader("Research Portfolio: Economics, Systems & Security")
st.markdown("---")

# 1. Context Header
st.header(f"Research Focus: {selected_pillar}")

# 2. The Search Engine (This replaces the broken links)
folder_path = pillars[selected_pillar]
files = get_file_list(folder_path)

if files:
    st.write(f"**Browse {len(files)} Research Notes:**")
    
    # THE SEARCH WIDGET
    # This box allows typing (e.g., 'Potato') or scrolling.
    selected_file = st.selectbox(
        "Select an article to read:",
        options=files,
        format_func=format_func,
        index=0
    )
    
    st.markdown("---")
    
    # 3. Render Content (Instant Load)
    file_path = os.path.join(folder_path, selected_file)
    with open(file_path, "r") as f:
        content = f.read()
    
    st.markdown(content, unsafe_allow_html=True)

else:
    st.error(f"No files found in {folder_path}. Please check your directories.")

# --- FOOTER ---
st.markdown("---")
st.caption("Global Pulse Observatory | Live Research Platform")
