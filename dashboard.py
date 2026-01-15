import streamlit as st
import os
import streamlit.components.v1 as components

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Global Pulse Observatory",
    page_icon="🔭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. GOOGLE ANALYTICS INJECTION ---
# Replace 'G-MTQ30TPFCV' with your actual Measurement ID
GA_ID = "G-MTQ30TPFCV"
GA_JS = f"""
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
<script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', '{GA_ID}');
</script>
"""
# This inserts the code invisibly
components.html(GA_JS, height=0, width=0)

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

# --- SIDEBAR PROFILE ---
with st.sidebar:
    st.image("https://ui-avatars.com/api/?name=Cristián+Morales&background=0D8ABC&color=fff&size=128", width=100)
    st.markdown("### Cristián Morales")
    st.markdown("**Digital Marketing & Business Analytics**")
    st.caption("MBA | INCAE Business School") 
    st.caption("📍 San José, Costa Rica")
    
    # Social Links
    st.link_button("🔗 LinkedIn", "https://www.linkedin.com/in/cris-morales-ema2024/") 
    st.link_button("🐙 GitHub", "https://github.com/c0pp3rhead")
    
    # Resume Download Logic
    if os.path.exists("resume.pdf"):
        with open("resume.pdf", "rb") as pdf_file:
            st.download_button(
                label="📄 Download Resume",
                data=pdf_file,
                file_name="Cristian_Morales_Resume.pdf",
                mime="application/pdf"
            )
    
    st.markdown("---")

st.sidebar.title("🏛 Fields of Study")
pillars = {
    "🌱 Exoplanetary Agriculture": "research_articles/1_Exoplanetary_Agriculture",
    "📉 Climate Finance": "research_articles/2_Climate_Finance",
    "☣️ Biosecurity & Illicit Economies": "research_articles/3_Biosecurity_Illicit_Economies"
}

selected_pillar = st.sidebar.radio("Select Discipline:", list(pillars.keys()), index=0)
st.sidebar.markdown("---")
st.sidebar.info("Select a Discipline, then search for a research note.")

# --- MAIN PAGE ---
st.title("Cristian Morales")
st.subheader("Research Portfolio: Economics, Systems & Security")
st.markdown("---")
st.header(f"Research Focus: {selected_pillar}")

folder_path = pillars[selected_pillar]
files = get_file_list(folder_path)

if files:
    st.write(f"**Browse {len(files)} Research Notes:**")
    selected_file = st.selectbox("Select an article:", options=files, format_func=format_func)
    st.markdown("---")
    
    # RENDER CONTENT
    file_path = os.path.join(folder_path, selected_file)
    with open(file_path, "r") as f:
        content = f.read()
    
    # Filter out any old markdown image links to avoid duplicates/errors
    content_clean = "\n".join([line for line in content.split('\n') if "![Chart]" not in line])
    st.markdown(content_clean, unsafe_allow_html=True)

    # RENDER IMAGE MANUALLY (The Fix)
    img_name = selected_file.replace(".md", ".png")
    # Try exact match first, then lowercase
    paths_to_try = [
        os.path.join(folder_path, "images", img_name),
        os.path.join(folder_path, "images", img_name.lower())
    ]
    
    image_loaded = False
    for p in paths_to_try:
        if os.path.exists(p):
            st.image(p, caption=f"Figure 1: Data Analysis for {format_func(selected_file)}")
            image_loaded = True
            break
            
    if not image_loaded:
        st.caption("*(Chart generation pending)*")

else:
    st.error(f"No files found in {folder_path}.")
