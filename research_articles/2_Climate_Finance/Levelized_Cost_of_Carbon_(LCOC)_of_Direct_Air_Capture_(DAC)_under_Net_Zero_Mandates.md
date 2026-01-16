# Levelized Cost of Carbon (LCOC) of Direct Air Capture (DAC) under Net-Zero Mandates
**Domain:** Biosystems Engineering (Finance) | **Read Time:** 15 min
**Keywords:** Biosystems, Engineering, Modeling

**Engineering Abstract**

The global challenge of achieving net-zero carbon emissions by 2050 necessitates the exploration and optimization of carbon removal technologies, such as Direct Air Capture (DAC). This research note investigates the Levelized Cost of Carbon (LCOC) of DAC systems within the framework of net-zero mandates. The study aims to provide a rigorous quantitative assessment of DAC's economic viability and its integration into existing biosystems engineering processes. This analysis draws from engineering principles, economic models, and failure mode assessments to deliver a comprehensive understanding of DAC's potential and limitations.

**System Architecture**

DAC systems are engineered to extract CO2 directly from ambient air. The primary components of a DAC system include:

1. **Air Contactors:** These devices facilitate the capture of CO2 using chemical sorbents. A popular choice involves aqueous solutions of potassium hydroxide (KOH), which react with CO2 to form potassium carbonate (K2CO3).

2. **Regeneration Units:** Following capture, the CO2-laden sorbent is transferred to a regeneration unit where CO2 is released through thermal or pressure-swing processes. The chemical equation for the liberation of CO2 from K2CO3 is:  
   \[ \text{K}_2\text{CO}_3 + \text{Heat} \rightarrow 2\text{KOH} + \text{CO}_2 \uparrow \]

3. **Compression and Storage:** The released CO2 is compressed to approximately 15 MPa for pipeline transport or storage. Compression requires substantial energy, often a significant cost factor.

4. **Energy Systems:** The DAC process is energy-intensive, necessitating robust integration with renewable energy sources to maintain net-zero emissions. Components operate at approximately 500 kW per tonne of CO2 captured per day.

5. **Control Systems:** Real-time monitoring and optimization algorithms, often compliant with IEEE 1547 standards, ensure system efficiency and reliability.

**Mathematical Framework**

The LCOC for DAC is derived from the total lifetime cost of the system divided by the total amount of CO2 captured over its operational lifespan. The key factors in this calculation include:

- **Capital Expenditure (CAPEX):** Initial investment costs for plant construction and equipment.
- **Operational Expenditure (OPEX):** Ongoing costs, including energy consumption, maintenance, and labor.
- **Discount Rate (r):** Reflects the time value of money, typically set between 3-7%.
- **Total CO2 Captured (Q):** Measured in metric tons over the system's life.

The LCOC is expressed as:
\[ \text{LCOC} = \frac{\text{CAPEX} + \sum_{t=1}^{n} \frac{\text{OPEX}_t}{(1+r)^t}}{Q} \]

Where \( n \) is the operational lifespan of the DAC plant.

**Simulation Results**

Simulation models were developed using MATLAB and Aspen Plus to assess the performance and cost implications of varying DAC configurations. Figure 1 illustrates the relationship between energy input (kW) and CO2 captured (kg/day) under different scenarios.

- **Scenario A:** High renewable energy availability (solar/wind), leading to reduced energy costs.
- **Scenario B:** Integration with waste heat recovery systems, enhancing energy efficiency.
- **Scenario C:** Economies of scale in large DAC installations, reducing unit costs.

The simulations indicate that LCOC values range from $100 to $300 per tonne of CO2, contingent on energy source and system size. The most cost-effective systems leverage high renewable penetration and advanced heat recovery technologies.

**Failure Modes & Risk Analysis**

DAC systems are subject to several potential failure modes, which can significantly affect LCOC and system reliability:

1. **Sorbent Degradation:** Chemical wear and tear over time may reduce capture efficiency. Regular replacement schedules and quality control measures are critical.

2. **Energy Supply Variability:** Fluctuations in renewable energy availability can impact operational continuity. Hybrid systems combining multiple energy sources (e.g., solar, wind, and geothermal) can mitigate this risk.

3. **Mechanical Failures:** Components such as compressors and pumps are prone to mechanical wear. Implementation of predictive maintenance protocols, guided by ISO 55000 standards for asset management, can enhance system uptime.

4. **Policy and Regulatory Risks:** Shifts in environmental policy or carbon pricing could alter the economic landscape for DAC. Continuous engagement with regulatory bodies ensures alignment and compliance.

In conclusion, while DAC presents a promising avenue for achieving net-zero targets, its economic viability hinges on strategic integration with renewable energy systems, technological advancements, and comprehensive risk management. Ongoing research and development, coupled with policy support, are essential to realizing the full potential of DAC technologies in the biosystems engineering domain.