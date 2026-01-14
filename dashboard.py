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
    if not os.path.exists(folder_path):
        return []
    files = [f for f in os.listdir(folder_path) if f.endswith(".md") and f != "index.md"]
    files.sort()
    return files

def format_func(filename):
    return filename.replace("_", " ").replace(".md", "")

# --- SIDEBAR ---
st.sidebar.title("🏛 Fields of Study")

pillars = {
    "🌱 Exoplanetary Agriculture": "research_articles/1_Exoplanetary_Agriculture",
    "📉 Climate Finance": "research_articles/2_Climate_Finance",
    "☣️ Biosecurity & Illicit Economies": "research_articles/3_Biosecurity_Illicit_Economies"
}

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

st.header(f"Research Focus: {selected_pillar}")

folder_path = pillars[selected_pillar]
files = get_file_list(folder_path)

if files:
    st.write(f"**Browse {len(files)} Research Notes:**")
    
    selected_file = st.selectbox(
        "Select an article to read:",
        options=files,
        format_func=format_func,
        index=0
    )
    
    st.markdown("---")
    
    file_path = os.path.join(folder_path, selected_file)
    with open(file_path, "r") as f:
        content = f.read()
    
    st.markdown(content, unsafe_allow_html=True)

else:
    st.error(f"No files found in {folder_path}. Please check your directories.")

st.markdown("---")
st.caption("Global Pulse Observatory | Live Research Platform")
