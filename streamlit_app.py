import streamlit as st
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Global Pulse Observatory",
    page_icon="🔭",
    layout="wide"
)

# --- 1. SIDEBAR CONFIGURATION (CLEAN) ---
st.sidebar.title("🏛 Fields of Study")
st.sidebar.write("Select Discipline:")

pillars = {
    "🌱 Exoplanetary Agriculture": "research_articles/1_Exoplanetary_Agriculture",
    "📉 Climate Finance": "research_articles/2_Climate_Finance",
    "☣️ Biosecurity & Illicit Economies": "research_articles/3_Biosecurity_Illicit_Economies"
}

# The only interactive element in the sidebar
selected_pillar = st.sidebar.radio(
    "Discipline Selector", 
    list(pillars.keys()), 
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.info("**Note:** Articles in the 'Biosecurity' section focus on economic impact and supply chain analysis, not synthesis or instruction.")

# --- 2. URL LOGIC (THE ROUTER) ---
# We check the URL to see if the user clicked a specific article link
query_params = st.query_params
article_requested = query_params.get("article", None)

# Handle edge case where param returns as a list
if isinstance(article_requested, list):
    article_requested = article_requested[0]

# Helper to find file path
def find_article_path(filename):
    for root, dirs, files in os.walk("research_articles"):
        if filename in files:
            return os.path.join(root, filename)
    return None

# --- 3. MAIN CONTENT RENDERER ---

# SCENARIO A: VIEWING AN ARTICLE
if article_requested:
    file_path = find_article_path(article_requested)
    
    if file_path and os.path.exists(file_path):
        # Navigation Bar
        col1, col2 = st.columns([1, 5])
        with col1:
            if st.button("← Back to Index"):
                st.query_params.clear()
                st.rerun()
        
        # Render Article
        with open(file_path, "r") as f:
            content = f.read()
        st.markdown(content, unsafe_allow_html=True)
        
    else:
        st.error(f"404: Article '{article_requested}' not found.")
        if st.button("Return Home"):
            st.query_params.clear()
            st.rerun()

# SCENARIO B: PILLAR INDEX (DEFAULT VIEW)
else:
    # Title Header
    st.title("Cristian Morales")
    st.subheader("Research Portfolio: Economics, Systems & Security")
    st.markdown("_A repository of static analysis, data visualizations, and research notes._")
    st.markdown("---")

    # Load the specific folder for the selected pillar
    folder_path = pillars[selected_pillar]
    st.header(f"Research Focus: {selected_pillar}")

    # Check for a curated 'index.md' (We created this for Pillar 1)
    index_path = os.path.join(folder_path, "index.md")
    
    if os.path.exists(index_path):
        # Render the curated index
        with open(index_path, "r") as f:
            index_content = f.read()
        st.markdown(index_content, unsafe_allow_html=True)
        
    else:
        # AUTOMATIC FALLBACK for Pillar 2 & 3 (No index.md yet)
        # We generate the link list dynamically so they aren't empty
        st.markdown("### Available Research Notes")
        files = sorted([f for f in os.listdir(folder_path) if f.endswith(".md")])
        
        for f in files:
            # Create a Deep Link for every file
            clean_name = f.replace("_", " ").replace(".md", "")
            # This format triggers Scenario A when clicked
            st.markdown(f"- [{clean_name}](/?article={f})")

# --- FOOTER ---
st.markdown("---")
st.caption("Global Pulse Observatory | Live Research Platform")
