import streamlit as st
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Global Pulse Observatory",
    page_icon="🔭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 1. ROUTER LOGIC (THE SUPREME AUTHORITY) ---
# Check URL immediately. If present, this overrides everything else.
query_params = st.query_params
article_requested = query_params.get("article", None)

# Helper: Find file recursively
def find_article_path(filename):
    target = filename.strip()
    for root, dirs, files in os.walk("research_articles"):
        if target in files:
            return os.path.join(root, target)
    return None

# Helper: Clear URL to go home
def go_home():
    st.query_params.clear()

# --- 2. SIDEBAR (ALWAYS VISIBLE) ---
st.sidebar.title("🏛 Fields of Study")

pillars = {
    "🌱 Exoplanetary Agriculture": "research_articles/1_Exoplanetary_Agriculture",
    "📉 Climate Finance": "research_articles/2_Climate_Finance",
    "☣️ Biosecurity & Illicit Economies": "research_articles/3_Biosecurity_Illicit_Economies"
}

# We use a session state to track the pilllar so it doesn't reset weirdly
if "pillar" not in st.session_state:
    st.session_state.pillar = list(pillars.keys())[0]

# The Radio Button
selected_pillar = st.sidebar.radio(
    "Select Discipline:", 
    list(pillars.keys()), 
    key="pillar_selector",
    on_change=go_home # CRITICAL: If they touch the sidebar, we clear the article view
)

st.sidebar.markdown("---")
st.sidebar.info("**Note:** Articles in the 'Biosecurity' section focus on economic impact and supply chain analysis.")

# --- 3. MAIN CONTENT CONTROLLER ---

if article_requested:
    # --- MODE A: READER VIEW ---
    # The URL has an article, so we IGNORE the sidebar selection entirely.
    
    file_path = find_article_path(article_requested)
    
    if file_path and os.path.exists(file_path):
        # Back Button
        if st.button("← Back to Research Index"):
            go_home()
            st.rerun()
            
        # Render Markdown
        with open(file_path, "r") as f:
            content = f.read()
        st.markdown(content, unsafe_allow_html=True)
        
    else:
        st.error(f"404 Not Found: '{article_requested}'")
        if st.button("Return Home"):
            go_home()
            st.rerun()

else:
    # --- MODE B: INDEX VIEW ---
    # No URL detected, so we obey the Sidebar.
    
    st.title("Cristian Morales")
    st.subheader("Research Portfolio: Economics, Systems & Security")
    st.markdown("---")

    # 1. Header
    st.header(f"Research Focus: {selected_pillar}")
    
    # 2. Load the Pillar Folder
    folder_path = pillars[selected_pillar]
    index_path = os.path.join(folder_path, "index.md")
    
    # 3. Render the Index
    if os.path.exists(index_path):
        # Use the nice curated list (100 links)
        with open(index_path, "r") as f:
            index_content = f.read()
        st.markdown(index_content, unsafe_allow_html=True)
    else:
        # Fallback (Auto-generate list if index.md is missing)
        st.write("### Available Research Notes")
        files = sorted([f for f in os.listdir(folder_path) if f.endswith(".md")])
        for f in files:
            # Create the exact same link format
            st.markdown(f"- [{f}](/?article={f})")

# --- FOOTER ---
st.markdown("---")
st.caption("Global Pulse Observatory | Live Research Platform")
