import streamlit as st
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Global Pulse Observatory",
    page_icon="🔭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 1. HELPER FUNCTIONS ---
def find_article_path(filename):
    """Recursively search for the article in all folders"""
    target = filename.strip()
    for root, dirs, files in os.walk("research_articles"):
        if target in files:
            return os.path.join(root, target)
    return None

def reset_app():
    """Clears URL and resets state"""
    st.query_params.clear()

# --- 2. URL CHECK (THE ROUTER) ---
# We check this BEFORE drawing the sidebar to prioritize the link
query_params = st.query_params
article_requested = query_params.get("article", None)

# --- 3. SIDEBAR SETUP ---
st.sidebar.title("🏛 Fields of Study")

pillars = {
    "🌱 Exoplanetary Agriculture": "research_articles/1_Exoplanetary_Agriculture",
    "📉 Climate Finance": "research_articles/2_Climate_Finance",
    "☣️ Biosecurity & Illicit Economies": "research_articles/3_Biosecurity_Illicit_Economies"
}

# The Pillar Selector
# Note: We use a callback to clear the URL if the user switches pillars
selected_pillar = st.sidebar.radio(
    "Select Discipline:", 
    list(pillars.keys()), 
    index=0,
    on_change=reset_app # CRITICAL: Clicking sidebar clears the article view
)

st.sidebar.markdown("---")
st.sidebar.info("**Note:** Articles in the 'Biosecurity' section focus on economic impact and supply chain analysis.")

# --- 4. MAIN CONTENT AREA ---

# SCENARIO A: VIEWING AN ARTICLE
if article_requested:
    file_path = find_article_path(article_requested)
    
    if file_path and os.path.exists(file_path):
        # 1. Navigation Bar
        if st.button("← Back to Index"):
            reset_app()
            st.rerun()
            
        # 2. Render Article
        with open(file_path, "r") as f:
            content = f.read()
        st.markdown(content, unsafe_allow_html=True)
        
    else:
        st.error(f"404 Not Found: '{article_requested}'")
        if st.button("Return Home"):
            reset_app()
            st.rerun()

# SCENARIO B: PILLAR INDEX
else:
    # Header
    st.title("Cristian Morales")
    st.subheader("Research Portfolio: Economics, Systems & Security")
    st.markdown("_A repository of static analysis, data visualizations, and research notes._")
    st.markdown("---")

    # Render Pillar Header
    st.header(f"Research Focus: {selected_pillar}")
    
    # Load the specific Index
    folder_path = pillars[selected_pillar]
    index_path = os.path.join(folder_path, "index.md")
    
    if os.path.exists(index_path):
        with open(index_path, "r") as f:
            index_content = f.read()
        st.markdown(index_content, unsafe_allow_html=True)
        
    else:
        # Fallback if index.md is missing (Safety Net)
        st.write("### Research Notes")
        files = sorted([f for f in os.listdir(folder_path) if f.endswith(".md")])
        for f in files:
            # Create the exact same link format
            st.markdown(f"- [{f}](/?article={f})")
