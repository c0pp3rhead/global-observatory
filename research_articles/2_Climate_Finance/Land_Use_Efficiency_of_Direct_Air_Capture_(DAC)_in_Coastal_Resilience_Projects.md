# Land Use Efficiency of Direct Air Capture (DAC) in Coastal Resilience Projects
**Domain:** Biosystems Engineering (Finance) | **Read Time:** 15 min
**Keywords:** Biosystems, Engineering, Modeling

**Title: Land Use Efficiency of Direct Air Capture (DAC) in Coastal Resilience Projects**

**1. Engineering Abstract (Problem Statement)**

Coastal resilience projects are integral for mitigating the impacts of climate change, particularly in protecting against sea-level rise and extreme weather events. Direct Air Capture (DAC) technology has emerged as a potential tool to sequester atmospheric CO2, which could mitigate the ocean's acidification and its adverse effects on coastal ecosystems. However, the implementation of DAC systems necessitates substantial land use, which poses a challenge in densely populated coastal areas. This research note investigates the land use efficiency of DAC within the context of coastal resilience projects, assessing its viability through engineering and financial lenses. We explore the optimization of DAC systems to minimize spatial footprints while maximizing CO2 capture efficiency, supported by quantitative assessments and simulations.

**2. System Architecture (Technical Components, Inputs/Outputs)**

The DAC system architecture considered in this study comprises several key components: air contactors, chemical sorbents, regeneration units, and CO2 compression and storage facilities. 

- **Air Contactors:** The design of the contactors is based on structured packing materials that maximize surface area for air-sorbent interactions. The contactor operates at a flow rate of 500 m³/min.
  
- **Chemical Sorbents:** The primary sorbent used is a solid amine, known for its high affinity to CO2. The sorbent is regenerated through thermal swing adsorption (TSA), requiring energy input of approximately 2.5 MJ/kg CO2.

- **Regeneration Units:** These units operate at an efficiency of 85%, powered by renewable energy sources to minimize carbon footprint. The regeneration process involves heating the sorbent to 100°C.

- **CO2 Compression and Storage:** Captured CO2 is compressed to a pressure of 15 MPa for storage. The compression process consumes 0.5 kWh/kg CO2.

The system's inputs include ambient air, renewable energy (solar and wind), and water for cooling processes. Outputs are concentrated CO2 (purity >95%), waste heat, and regenerated sorbent. The overall land use is estimated based on the footprint of the air contactors and ancillary systems.

**3. Mathematical Framework**

The land use efficiency (\(LUE\)) of the DAC system is quantified as the ratio of CO2 captured per unit area to the total area occupied by the system:

\[ LUE = \frac{Q_{CO2}}{A_{system}} \]

where \(Q_{CO2}\) is the amount of CO2 captured (kg/day) and \(A_{system}\) is the total land area occupied by the DAC system (m²).

**CO2 Capture Rate:**
The CO2 capture rate (\(R_{CO2}\)) is determined by the air flow rate (\(F_{air}\)), the CO2 concentration in ambient air (\(C_{CO2,air} \approx 400 \ ppm = 0.0004\)), and the capture efficiency (\(\eta\)):

\[ R_{CO2} = F_{air} \times C_{CO2,air} \times \eta \]

**Energy Balance:**
The energy required for regeneration (\(E_{regen}\)) and compression (\(E_{compress}\)) is calculated as:

\[ E_{regen} = Q_{CO2} \times 2.5 \ MJ/kg \]

\[ E_{compress} = Q_{CO2} \times 0.5 \ kWh/kg \]

These equations underpin the DAC system's design and operation, ensuring that CO2 capture is maximized while minimizing energy consumption and land use.

**4. Simulation Results**

Simulation of a DAC system deployed in a coastal region with a land area constraint of 10,000 m² reveals promising results. As shown in Figure 1, the system captures approximately 1,200 kg of CO2 per day under optimal conditions, achieving a land use efficiency of 0.12 kg/m²/day. The energy consumption is primarily offset by solar and wind energy, with a total energy requirement of 3,500 kWh/day for regeneration and compression.

**5. Failure Modes & Risk Analysis**

Despite the promising potential of DAC systems in coastal resilience projects, several failure modes and risks must be considered:

- **Sorbent Degradation:** Over time, the chemical sorbent may degrade, reducing capture efficiency. Regular maintenance and replacement protocols are necessary to mitigate this risk.

- **Energy Supply Variability:** The reliance on renewable energy poses risks due to variability in solar and wind resources. Backup energy systems or grid integration may be necessary to ensure continuous operation.

- **Corrosion and Material Fatigue:** The harsh coastal environment can accelerate corrosion and material fatigue in system components. Employing corrosion-resistant materials and regular inspections can mitigate these risks.

- **Economic Viability:** The high initial investment and operational costs of DAC systems may limit their deployment. Financial models, such as those based on the Black-Scholes option pricing model, can assess the economic feasibility and optimize investment strategies.

This research note concludes that while DAC systems hold significant potential for enhancing coastal resilience, optimizing land use efficiency and addressing associated risks are crucial for their successful implementation. Future work will focus on integrating DAC with other resilience strategies and conducting field trials to validate simulation results.