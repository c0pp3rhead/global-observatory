import streamlit as st
import os

# --- CONFIGURATION ---
st.set_page_config(
    page_title="Global Pulse Observatory",
    page_icon="🔭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- HELPER FUNCTIONS ---
def find_article_path(filename):
    """Finds the file path across all 3 pillars"""
    target = filename.strip()
    for root, dirs, files in os.walk("research_articles"):
        if target in files:
            return os.path.join(root, target)
    return None

def go_home():
    """Reset URL"""
    st.query_params.clear()

# --- SIDEBAR (CLEAN - NO FILES) ---
st.sidebar.title("🏛 Fields of Study")

pillars = {
    "🌱 Exoplanetary Agriculture": "research_articles/1_Exoplanetary_Agriculture",
    "📉 Climate Finance": "research_articles/2_Climate_Finance",
    "☣️ Biosecurity & Illicit Economies": "research_articles/3_Biosecurity_Illicit_Economies"
}

# Session state ensures the selection sticks
if "pillar" not in st.session_state:
    st.session_state.pillar = list(pillars.keys())[0]

selected_pillar = st.sidebar.radio(
    "Select Discipline:", 
    list(pillars.keys()), 
    index=0,
    on_change=go_home 
)

st.sidebar.markdown("---")
# Only the note appears here. No file lists.
st.sidebar.info("**Note:** Articles in the 'Biosecurity' section focus on economic impact and supply chain analysis.")

# --- MAIN CONTENT ---

# 1. Check URL for Deep Link
query_params = st.query_params
article_requested = query_params.get("article", None)

if article_requested:
    # --- VIEWING ARTICLE ---
    file_path = find_article_path(article_requested)
    
    if file_path and os.path.exists(file_path):
        if st.button("← Back to Research Index"):
            go_home()
            st.rerun()
            
        with open(file_path, "r") as f:
            content = f.read()
        
        # Render Article
        st.markdown(content, unsafe_allow_html=True)
    else:
        st.error(f"404 Not Found: {article_requested}")
        if st.button("Return Home"):
            go_home()
            st.rerun()

else:
    # --- VIEWING INDEX ---
    st.title("Cristian Morales")
    st.subheader("Research Portfolio: Economics, Systems & Security")
    st.markdown("_A repository of static analysis, data visualizations, and research notes._")
    st.markdown("---")

    # Dynamic Header
    st.header(f"Research Focus: {selected_pillar}")
    if selected_pillar == "🌱 Exoplanetary Agriculture":
        st.markdown("This section explores the intersection of systems, economics, and security.")
    elif selected_pillar == "📉 Climate Finance":
        st.markdown("This section explores the intersection of systems, economics, and security.")
    elif selected_pillar == "☣️ Biosecurity & Illicit Economies":
        st.markdown("This section explores the intersection of systems, economics, and security.")
    
    # Load the Index File (The list of 100 links)
    folder_path = pillars[selected_pillar]
    index_path = os.path.join(folder_path, "index.md")
    
    if os.path.exists(index_path):
        with open(index_path, "r") as f:
            index_content = f.read()
        st.markdown(index_content, unsafe_allow_html=True)
    else:
        st.warning("Index file not found. Please regenerate the index.")
