import streamlit as st
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Global Pulse Observatory",
    page_icon="🔭",
    layout="wide"
)

# --- 1. SETUP SIDEBAR ---
st.sidebar.title("🏛 Fields of Study")
st.sidebar.write("Select Discipline:")

# Define Pillars and Paths
pillars = {
    "🌱 Exoplanetary Agriculture": "research_articles/1_Exoplanetary_Agriculture",
    "📉 Climate Finance": "research_articles/2_Climate_Finance",
    "☣️ Biosecurity & Illicit Economies": "research_articles/3_Biosecurity_Illicit_Economies"
}

# Sidebar Selection
selected_pillar = st.sidebar.radio(
    "Go to Pillar:", 
    list(pillars.keys()), 
    label_visibility="collapsed"
)

# Sidebar Note
st.sidebar.markdown("---")
st.sidebar.info("**Note:** Articles in the 'Biosecurity' section focus on economic impact and supply chain analysis, not synthesis or instruction.")

# --- 2. NAVIGATION LOGIC ---
# We check the URL to see if the user clicked a link
query_params = st.query_params
article_requested = query_params.get("article", None)

# Helper to find file path across all folders
def find_article_path(filename):
    for root, dirs, files in os.walk("research_articles"):
        if filename in files:
            return os.path.join(root, filename)
    return None

# --- 3. RENDER CONTENT ---

# SCENARIO A: User wants to read a specific article (Deep Link)
if article_requested:
    file_path = find_article_path(article_requested)
    
    if file_path and os.path.exists(file_path):
        # 1. Add a "Back" button
        if st.button("← Back to Dashboard"):
            st.query_params.clear() # Clear URL to return to home
            st.rerun()
            
        # 2. Render Article
        with open(file_path, "r") as f:
            content = f.read()
        st.markdown(content, unsafe_allow_html=True)
        
    else:
        st.error(f"404: Article '{article_requested}' not found.")
        if st.button("Return Home"):
            st.query_params.clear()
            st.rerun()

# SCENARIO B: User is browsing a Pillar (List View)
else:
    # Title
    st.title("Cristian Morales")
    st.subheader("Research Portfolio: Economics, Systems & Security")
    st.markdown("_A repository of static analysis, data visualizations, and research notes._")
    st.markdown("---")

    # Dynamic Header based on selection
    if selected_pillar == "🌱 Exoplanetary Agriculture":
        st.header("Research Focus: 1 Exoplanetary Agriculture")
        st.markdown("This section explores the intersection of systems, economics, and security.")
        
        # Check if the categorized index exists (The one we generated)
        index_path = os.path.join(pillars[selected_pillar], "index.md")
        if os.path.exists(index_path):
            with open(index_path, "r") as f:
                index_content = f.read()
            st.markdown(index_content, unsafe_allow_html=True)
        else:
            # Fallback: List files if index is missing
            files = sorted([f for f in os.listdir(pillars[selected_pillar]) if f.endswith(".md") and f != "index.md"])
            for f in files:
                clean_name = f.replace("_", " ").replace(".md", "")
                st.markdown(f"- [{clean_name}](/?article={f})")

    elif selected_pillar == "📉 Climate Finance":
        st.header("Research Focus: 2 Climate Finance")
        st.markdown("This section explores the intersection of systems, economics, and security.")
        
        # List all files for Climate Finance
        folder = pillars[selected_pillar]
        files = sorted([f for f in os.listdir(folder) if f.endswith(".md") and f != "index.md"])
        for f in files:
            clean_name = f.replace("_", " ").replace(".md", "")
            st.markdown(f"- [{clean_name}](/?article={f})")

    elif selected_pillar == "☣️ Biosecurity & Illicit Economies":
        st.header("Research Focus: 3 Biosecurity & Illicit Economies")
        st.markdown("This section explores the intersection of systems, economics, and security.")
        
        # List all files for Biosecurity
        folder = pillars[selected_pillar]
        files = sorted([f for f in os.listdir(folder) if f.endswith(".md") and f != "index.md"])
        for f in files:
            clean_name = f.replace("_", " ").replace(".md", "")
            st.markdown(f"- [{clean_name}](/?article={f})")

# --- FOOTER ---
st.markdown("---")
st.caption("Global Pulse Observatory | Live Research Platform")
