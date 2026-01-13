import streamlit as st
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Global Pulse Observatory",
    page_icon="🔭",
    layout="wide"
)

# --- 1. HELPER FUNCTIONS ---
def get_all_articles():
    """Scans all folders and returns a dict of {filename: full_path}"""
    article_map = {}
    for root, dirs, files in os.walk("research_articles"):
        for file in files:
            if file.endswith(".md") and file != "index.md":
                article_map[file] = os.path.join(root, file)
    return article_map

def load_markdown(path):
    """Safely reads a markdown file"""
    if os.path.exists(path):
        with open(path, "r") as f:
            return f.read()
    return None

# --- 2. URL PARAMETER HANDLING (THE FIX) ---
# We grab the query params immediately
query_params = st.query_params
article_requested = query_params.get("article", None)

# If 'article_requested' is a list (rare edge case), take the first item
if isinstance(article_requested, list):
    article_requested = article_requested[0]

# --- 3. SIDEBAR SETUP ---
st.sidebar.title("🏛 Fields of Study")
st.sidebar.write("Select Discipline:")

pillars = {
    "🌱 Exoplanetary Agriculture": "research_articles/1_Exoplanetary_Agriculture",
    "📉 Climate Finance": "research_articles/2_Climate_Finance",
    "☣️ Biosecurity & Illicit Economies": "research_articles/3_Biosecurity_Illicit_Economies"
}

# We only show the radio button if we are NOT viewing an article
# OR we allow it to act as a "Home" button
selected_pillar = st.sidebar.radio(
    "Go to Pillar:", 
    list(pillars.keys()), 
    index=0
)

st.sidebar.markdown("---")
st.sidebar.info("**Note:** Articles in the 'Biosecurity' section focus on economic impact and supply chain analysis.")

# --- 4. MAIN LOGIC FLOW ---

# PRIORITY 1: VIEWING AN ARTICLE (URL TRIGGER)
if article_requested:
    # Scan for the file
    article_map = get_all_articles()
    
    if article_requested in article_map:
        file_path = article_map[article_requested]
        
        # Add a prominent BACK button
        if st.button("← Back to Research Pillars"):
            st.query_params.clear() # Wipe the URL
            st.rerun() # Reload the app in "Pillar Mode"

        # Render the Article
        content = load_markdown(file_path)
        if content:
            st.markdown(content, unsafe_allow_html=True)
        else:
            st.error("Error loading article content.")
    else:
        st.error(f"404: The article '{article_requested}' could not be found.")
        if st.button("Return to Home"):
            st.query_params.clear()
            st.rerun()

# PRIORITY 2: BROWSING A PILLAR (DEFAULT)
else:
    # Header
    st.title("Cristian Morales")
    st.subheader("Research Portfolio: Economics, Systems & Security")
    st.markdown("_A repository of static analysis, data visualizations, and research notes._")
    st.markdown("---")

    # Determine which folder to show based on Sidebar
    folder_path = pillars[selected_pillar]
    
    # Render the Pillar Header
    st.header(f"Research Focus: {selected_pillar}")
    
    # 1. Try to load the curated 'index.md' (The nice list you generated)
    index_path = os.path.join(folder_path, "index.md")
    
    if os.path.exists(index_path):
        index_content = load_markdown(index_path)
        # We need to ensure the index.md links are rendered correctly by Streamlit
        st.markdown(index_content, unsafe_allow_html=True)
    
    # 2. Fallback: If no index.md exists, list files automatically
    else:
        files = sorted([f for f in os.listdir(folder_path) if f.endswith(".md")])
        for f in files:
            # Clean up the name for display
            clean_name = f.replace("_", " ").replace(".md", "")
            # Create the link that triggers Priority 1
            st.markdown(f"- [{clean_name}](/?article={f})")

# --- FOOTER ---
st.markdown("---")
st.caption("Global Pulse Observatory | Live Research Platform")
