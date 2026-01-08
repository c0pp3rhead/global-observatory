import streamlit as st
import os
from PIL import Image

# --- CONFIGURATION ---
st.set_page_config(page_title="Cristian Morales | Research", page_icon="🏛️", layout="wide")

# --- ACADEMIC STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #fdfdfd; color: #111; }
    .sidebar .sidebar-content { background-color: #f4f4f4; }
    h1 { font-family: 'Times New Roman', serif; color: #2c3e50; border-bottom: 2px solid #b33939; padding-bottom: 10px; }
    h2, h3 { font-family: 'Times New Roman', serif; color: #2c3e50; }
    p, li { font-family: 'Georgia', serif; font-size: 18px; line-height: 1.6; color: #333; }
    .caption { font-size: 14px; color: #666; font-style: italic; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
with st.container():
    st.title("Cristian Morales")
    st.markdown("### Research Portfolio: Economics, Systems & Security")
    st.markdown("*A repository of static analysis, data visualizations, and research notes.*")
    st.divider()

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("🏛️ Fields of Study")

# Map User Friendly Names to Folder Names
topic_map = {
    "🌱 Exoplanetary Agriculture": "1_Exoplanetary_Agriculture",
    "📉 Climate Finance": "2_Climate_Finance",
    "☣️ Biosecurity & Illicit Economies": "3_Biosecurity_Illicit_Economies"
}

selected_label = st.sidebar.radio("Select Discipline:", list(topic_map.keys()))
selected_folder = topic_map[selected_label]

st.sidebar.divider()
st.sidebar.info(
    "**Note:** Articles in the 'Biosecurity' section focus on economic impact and supply chain analysis, not synthesis or instruction."
)

# --- MAIN CONTENT RENDERER ---
base_path = os.path.join("research_articles", selected_folder)

try:
    # Get articles
    files = sorted([f for f in os.listdir(base_path) if f.endswith(".md")])
    
    if not files:
        st.warning("No articles archived in this section yet.")
    else:
        # Article Selector
        st.sidebar.subheader("📄 Publications")
        selected_article = st.sidebar.radio("Read:", files)
        
        # Display Logic
        article_path = os.path.join(base_path, selected_article)
        
        with open(article_path, "r") as f:
            content = f.read()
            
            # Render content line by line to catch [IMAGE] tags
            lines = content.split('\n')
            for line in lines:
                if "[IMAGE:" in line and "]" in line:
                    # Clean: [IMAGE: my_plot.png] -> my_plot.png
                    img_name = line.split("[IMAGE:")[1].split("]")[0].strip()
                    img_path = os.path.join(base_path, "images", img_name)
                    
                    if os.path.exists(img_path):
                        image = Image.open(img_path)
                        st.image(image, caption=f"Figure: {img_name}", use_column_width=True)
                    else:
                        st.warning(f"Image placeholder found, but file '{img_name}' is missing.")
                else:
                    st.markdown(line, unsafe_allow_html=True)

except FileNotFoundError:
    st.error("Research directory missing. Please run the setup script.")
