import streamlit as st
import os
import random
import streamlit.components.v1 as components

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Biosystems Engineering Research | UCR",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- GOOGLE ANALYTICS (Keep this for your own stats) ---
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

def get_research_gaps(category):
    """Injects dynamic PhD commentary based on the research pillar."""
    if "Exoplanetary" in category:
        return """
        **🧪 Principal Investigator's Note:**
        * **Current State:** Most closed-loop life support systems (ECLSS) operate at TRL 4-6. We currently rely on resupply for Earth orbit missions.
        * **The Engineering Gap:** The primary hurdle is **nutrient recovery efficiency**. We need to move from 75% water recycling to 98%+ closed-loop mass balance. My research focuses on the fluid dynamics of nutrient delivery in variable gravity to bridge this gap.
        """
    elif "Finance" in category:
        return """
        **🧪 Principal Investigator's Note:**
        * **Current State:** Biosystems valuation is currently theoretical or based on voluntary carbon markets with high volatility.
        * **The Engineering Gap:** We lack **thermodynamic accounting standards** for biological assets. This paper explores the gap between physical exergy (useful energy) and monetary valuation. Making these engineered systems bankable requires rigorous Techno-Economic Analysis (TEA) verified by sensors, not just estimates.
        """
    else: # Security
        return """
        **🧪 Principal Investigator's Note:**
        * **Current State:** Biological manufacturing is becoming digitized, but industrial control systems (ICS) for bio-reactors are insecure by design.
        * **The Engineering Gap:** There is a critical lack of **cyber-physical attribution**. We can detect a failure, but we cannot distinguish between a sensor error, a mutation, or a cyber-attack. My work investigates 'digital signatures' in biological hardware to secure the bio-economy supply chain.
        """

# --- SIDEBAR PROFILE (ACADEMIC) ---
with st.sidebar:
    # Use a neutral or academic avatar if you have one, or keep the abstract one
    st.image("https://ui-avatars.com/api/?name=Cristián+Morales&background=0D8ABC&color=fff&size=128", width=100)
    
    st.markdown("### Cristián Morales")
    st.markdown("**PhD Candidate**")
    st.markdown("Biosystems Engineering")
    st.caption("🏛 University of Costa Rica (UCR)")
    
    st.markdown("---")
    
    # NAVIGATION
    st.sidebar.title("📚 Research Modules")
    pillars = {
        "🚀 Space Biosystems (TRL 3-5)": "research_articles/1_Exoplanetary_Agriculture",
        "🌍 Climate Systems Engineering": "research_articles/2_Climate_Finance",
        "☣️ Biosecurity & Cyber-Bio": "research_articles/3_Biosecurity_Illicit_Economies"
    }
    
    selected_pillar = st.sidebar.radio("Select Research Focus:", list(pillars.keys()), index=0)
    
    st.markdown("---")
    st.info("**Methodology:** This library utilizes Generative AI to simulate high-volume scenarios (n=2000). My PhD work focuses on validating the governing equations and bridging the engineering gaps identified in these simulations.")

# --- MAIN PAGE ---
st.title("Biosystems Engineering | Research Roadmap")
st.subheader("Simulating Complex Biological Systems for Resilience")
st.markdown(f"**Current Module:** {selected_pillar}")

folder_path = pillars[selected_pillar]
files = get_file_list(folder_path)

if files:
    # Search and Select
    search_term = st.text_input("🔍 Search database by keyword (e.g., 'Thermodynamics', 'Sensor', 'Algorithm')", "")
    
    if search_term:
        files = [f for f in files if search_term.lower() in f.lower()]
        
    st.write(f"**Found {len(files)} Research Scenarios:**")
    selected_file = st.selectbox("Select a simulation to review:", options=files, format_func=format_func)
    
    st.markdown("---")
    
    # RENDER CONTENT
    file_path = os.path.join(folder_path, selected_file)
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            content = f.read()
        
        # Clean out old images text if any
        content_clean = "\n".join([line for line in content.split('\n') if "![Chart]" not in line])
        st.markdown(content_clean, unsafe_allow_html=True)

        # DYNAMIC IMAGE LOADER
        img_name = selected_file.replace(".md", ".png")
        paths_to_try = [
            os.path.join(folder_path, "images", img_name),
            os.path.join(folder_path, "images", img_name.lower())
        ]
        
        image_loaded = False
        for p in paths_to_try:
            if os.path.exists(p):
                st.image(p, caption=f"Figure 1: Simulated Engineering Output for {format_func(selected_file)}")
                image_loaded = True
                break
        
        # --- INJECT PHD COMMENTARY ---
        st.markdown("---")
        st.success(get_research_gaps(selected_pillar))
        
    else:
        st.error("File not found.")

else:
    st.error(f"No research files found in {folder_path}.")
