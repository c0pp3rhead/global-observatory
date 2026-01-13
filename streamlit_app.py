import streamlit as st
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Global Pulse Observatory",
    page_icon="🔭",
    layout="wide"
)

# --- 1. ROBUST URL RETRIEVAL ---
# Try the new method first, fall back to the old method if needed
try:
    # New Streamlit versions
    query_params = st.query_params
    article_requested = query_params.get("article", None)
except:
    # Older Streamlit versions
    query_params = st.experimental_get_query_params()
    # Old method returns a list ['filename.md'], so we grab the first item
    raw = query_params.get("article", [None])
    article_requested = raw[0]

# --- 2. FILE SYSTEM HELPER ---
def find_article_path(filename):
    """Recursively searches for the file in the research_articles directory"""
    target = filename.strip() # Remove any accidental whitespace
    for root, dirs, files in os.walk("research_articles"):
        if target in files:
            return os.path.join(root, target)
    return None

# --- 3. DEBUGGING SECTION (Temporary) ---
# This will show us exactly what the app sees.
# with st.expander("🛠 System Debug Info (Click to View)", expanded=False):
#    st.write(f"**URL Parameter Detected:** `{article_requested}`")
#    st.write(f"**Current Working Directory:** `{os.getcwd()}`")
#    st.write("**Search Test:** Searching for 'The_Potato_Paradox.md'...")
#    test_path = find_article_path("The_Potato_Paradox.md")
#    st.write(f"-> Found at: `{test_path}`")

# --- 4. NAVIGATION LOGIC ---

# SCENARIO A: Article Requested via URL
if article_requested:
    file_path = find_article_path(article_requested)
    
    if file_path:
        # success! Render the article
        
        # Back Button
        if st.button("← Back to Dashboard"):
            st.query_params.clear()
            st.rerun()
            
        # Render Content
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                content = f.read()
            st.markdown(content, unsafe_allow_html=True)
        else:
            st.error(f"File found at {file_path} but could not be opened.")
            
    else:
        # File not found in folders
        st.error(f"404 Error: The system could not locate the file `{article_requested}`.")
        st.warning("Please check that the file exists in the 'research_articles' folder.")
        if st.button("Return Home"):
            st.query_params.clear()
            st.rerun()

# SCENARIO B: Default Dashboard View
else:
    # Sidebar Setup
    st.sidebar.title("🏛 Fields of Study")
    st.sidebar.write("Select Discipline:")

    pillars = {
        "🌱 Exoplanetary Agriculture": "research_articles/1_Exoplanetary_Agriculture",
        "📉 Climate Finance": "research_articles/2_Climate_Finance",
        "☣️ Biosecurity & Illicit Economies": "research_articles/3_Biosecurity_Illicit_Economies"
    }

    selected_pillar = st.sidebar.radio(
        "Go to Pillar:", 
        list(pillars.keys()), 
        index=0
    )

    st.sidebar.markdown("---")
    st.sidebar.info("**Note:** Articles in the 'Biosecurity' section focus on economic impact and supply chain analysis.")

    # Main Content Area
    st.title("Cristian Morales")
    st.subheader("Research Portfolio: Economics, Systems & Security")
    st.markdown("_A repository of static analysis, data visualizations, and research notes._")
    st.markdown("---")

    # Render Pillar Content
    folder_path = pillars[selected_pillar]
    st.header(f"Research Focus: {selected_pillar}")
    
    # Load Index
    index_path = os.path.join(folder_path, "index.md")
    if os.path.exists(index_path):
        with open(index_path, "r") as f:
            index_content = f.read()
        st.markdown(index_content, unsafe_allow_html=True)
    else:
        # Fallback list
        files = sorted([f for f in os.listdir(folder_path) if f.endswith(".md")])
        for f in files:
            st.markdown(f"- [{f}](/?article={f})")

# --- FOOTER ---
st.markdown("---")
st.caption("Global Pulse Observatory | Live Research Platform")
