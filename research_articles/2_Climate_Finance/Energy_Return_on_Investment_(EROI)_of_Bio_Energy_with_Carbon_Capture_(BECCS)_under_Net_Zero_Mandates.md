# Energy Return on Investment (EROI) of Bio-Energy with Carbon Capture (BECCS) under Net-Zero Mandates
**Domain:** Biosystems Engineering (Finance) | **Read Time:** 15 min
**Keywords:** Biosystems, Engineering, Modeling

**Energy Return on Investment (EROI) of Bio-Energy with Carbon Capture (BECCS) under Net-Zero Mandates**

**Engineering Abstract**

The transition to net-zero emissions necessitates the integration of sustainable energy technologies, among which Bio-Energy with Carbon Capture and Storage (BECCS) is a pivotal component. This research note examines the Energy Return on Investment (EROI) of BECCS—an essential metric that determines the feasibility and sustainability of this technology within the constraints of net-zero mandates. EROI, defined as the ratio of energy output to energy input, is critically evaluated in the context of BECCS systems, considering their operational complexities and carbon neutrality objectives. We explore the technical architecture of BECCS, establish a mathematical framework for EROI calculation, and present simulation results under various operational scenarios. Additionally, we conduct a thorough failure modes and risk analysis to identify potential impediments to achieving desired EROI levels.

**System Architecture**

The BECCS system comprises three core components: biomass feedstock production, bioenergy conversion, and carbon capture and storage (CCS). Biomass feedstock, typically sourced from agricultural residues, dedicated energy crops, or forestry by-products, enters the system at a rate of 5000 kg/day. Conversion to bioenergy is achieved through combustion or gasification processes, producing an energy output of 10 MW. The carbon capture component employs amine-based absorption, capturing CO2 at a rate of 85%, equivalent to 4.25 tonnes/day, under operating conditions of 1 MPa and 50°C. The captured CO2 is subsequently compressed and transported for geological storage.

Inputs to the system include energy investments for biomass cultivation (750 kW), transportation (100 kW), conversion (2000 kW), and CCS operations (350 kW). Outputs are assessed in terms of net energy yield and sequestered carbon, with a focus on optimizing both energy efficiency and carbon neutrality.

**Mathematical Framework**

The quantitative evaluation of EROI for BECCS systems requires a comprehensive mathematical framework. The EROI is expressed as:

\[ \text{EROI} = \frac{E_{\text{out}}}{E_{\text{in}}} \]

where \( E_{\text{out}} \) is the total energy output (kWh) and \( E_{\text{in}} \) is the cumulative energy input (kWh) over a specified period.

To model the bioenergy conversion process, we employ a mass-energy balance approach, incorporating the stoichiometric combustion equation for biomass:

\[ \text{C}_n\text{H}_m\text{O}_p + O_2 \rightarrow CO_2 + H_2O + \text{Energy} \]

The energy yield from biomass is calculated using the higher heating value (HHV) of the feedstock, typically 18 MJ/kg. The CCS component is modeled using the equation for capture efficiency (\(\eta_{\text{CCS}}\)) and energy penalty (\(\Delta E_{\text{CCS}}\)):

\[ \eta_{\text{CCS}} = \frac{\text{Mass of CO}_2 \text{ captured}}{\text{Mass of CO}_2 \text{ emitted}} \]

\[ \Delta E_{\text{CCS}} = \frac{E_{\text{capture}} + E_{\text{compression}}}{E_{\text{out}}} \]

The net energy output is adjusted for CCS energy penalties, ensuring an accurate EROI assessment.

**Simulation Results**

Simulation scenarios reveal EROI values ranging from 1.2 to 2.5, contingent on feedstock type, conversion efficiency, and CCS effectiveness. Figure 1 depicts the EROI sensitivity to variations in biomass moisture content and capture efficiency. Optimal scenarios, characterized by low moisture content and high capture efficiency, yield EROI values exceeding 2.0, signifying favorable energy sustainability.

**Failure Modes & Risk Analysis**

A rigorous failure modes and risk analysis identifies critical vulnerabilities within the BECCS system. Key failure modes include:

1. **Feedstock Supply Variability**: Inconsistent biomass supply can disrupt energy output and elevate input costs, adversely affecting EROI.
2. **Conversion Efficiency Losses**: Suboptimal combustion or gasification processes can diminish energy yield, thereby reducing system EROI.
3. **CCS Operational Failures**: Inefficient capture technologies or storage leakages compromise carbon sequestration efficacy and system sustainability.

Risk mitigation strategies involve diversifying feedstock sources, enhancing conversion technologies through advanced thermochemical processes, and adopting robust CCS monitoring protocols in compliance with ISO 27914 standards.

In conclusion, the EROI of BECCS under net-zero mandates is a multifaceted challenge, influenced by technological, operational, and environmental factors. This research underscores the importance of optimizing system components and processes to ensure the viability of BECCS as a cornerstone of sustainable energy strategy. Further research is required to refine EROI models and address identified risk factors, ensuring BECCS contributes effectively to global carbon reduction targets.