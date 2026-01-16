import streamlit as st
import os
import streamlit.components.v1 as components

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Biosystems Engineering Research | UCR",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- GOOGLE ANALYTICS ---
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

# --- DYNAMIC COMMENTARY (The Student's Perspective) ---
def get_research_gaps(category):
    """Injects dynamic analysis of the current engineering landscape."""
    if "Exoplanetary" in category:
        return """
        **🔭 Research Roadmap (Future Focus):**
        * **Status Quo:** Current Environmental Control and Life Support Systems (ECLSS) on the ISS operate at ~90% water recovery but struggle with solid waste loop closure.
        * **The Challenge:** To make these simulations a reality, we need >99% closed-loop mass balance and significantly higher thermodynamic efficiency.
        * **My Objective:** As I progress in my engineering studies, I aim to investigate the fluid dynamics and biological control systems required to bridge this gap, using these AI simulations as a theoretical baseline.
        """
    elif "Finance" in category:
        return """
        **🔭 Research Roadmap (Future Focus):**
        * **Status Quo:** Climate finance currently lacks rigorous hardware-to-value verification standards, relying heavily on estimates rather than sensor data.
        * **The Challenge:** We need 'Thermodynamic Accounting'—valuing assets based on physical exergy (useful work) rather than speculative carbon markets.
        * **My Objective:** I am building this database to identify how engineered biosystems can be instrumented to provide real-time valuation data, a key area I plan to explore during my degree.
        """
    else: # Security
        return """
        **🔭 Research Roadmap (Future Focus):**
        * **Status Quo:** Biological manufacturing infrastructure (bioreactors) currently lacks cyber-attribution features, making it vulnerable to supply chain interdiction.
        * **The Challenge:** Distinguishing between natural mutation and adversarial attack in real-time is currently impossible with standard sensors.
        * **My Objective:** These simulations highlight the urgent need for 'Digital Signatures' in biological hardware. I intend to study the intersection of cybersecurity and biological control systems to address this vulnerability.
        """

# --- SIDEBAR PROFILE (THE UNDERGRADUATE RESEARCHER) ---
with st.sidebar:
    # Academic/Neutral Avatar
    st.image("https://ui-avatars.com/api/?name=Cristián+Morales&background=0D8ABC&color=fff&size=128", width=100)
    
    st.markdown("### Cristián Morales")
    st.markdown("**Biosystems Engineering Student**")
    st.markdown("*Undergraduate Researcher*")
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
    st.info("**About this Lab:** I am using Generative AI to map the frontier of Biosystems Engineering. This library represents 2,000 theoretical scenarios I plan to investigate and validate throughout my academic career.")

# --- MAIN PAGE ---
st.title("Biosystems Engineering | Research Roadmap")
st.subheader("Simulating Complex Biological Systems for Resilience")
st.markdown(f"**Current Module:** {selected_pillar}")

folder_path = pillars[selected_pillar]
files = get_file_list(folder_path)

if files:
    # Search Feature
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
        
        # Clean out old markdown images text if any exists to prevent duplicates
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
        
        if not image_loaded:
            st.caption("*(Theoretical model - Visualization pending)*")
        
        # --- INJECT STUDENT ROADMAP COMMENTARY ---
        st.markdown("---")
        st.success(get_research_gaps(selected_pillar))
        
    else:
        st.error("File not found.")

else:
    st.error(f"No research files found in {folder_path}.")
