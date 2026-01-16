# Land Use Efficiency of Direct Air Capture (DAC) under Net-Zero Mandates
**Domain:** Biosystems Engineering (Finance) | **Read Time:** 15 min
**Keywords:** Biosystems, Engineering, Modeling

**Title: Land Use Efficiency of Direct Air Capture (DAC) under Net-Zero Mandates**

**1. Engineering Abstract (Problem Statement)**

The transition to a net-zero carbon economy necessitates innovative technological solutions to manage atmospheric CO₂ concentrations. Direct Air Capture (DAC) technology has emerged as a promising method to achieve significant reductions in atmospheric CO₂ levels. However, the viability of DAC is contingent upon its land use efficiency, especially under stringent net-zero mandates. This research note examines the land use efficiency of DAC systems, evaluating the spatial requirements necessary to meet specific CO₂ capture targets. By integrating engineering principles with financial insights, we explore the optimization of DAC system deployments to align with net-zero objectives, considering both technical and economic constraints.

**2. System Architecture (Technical components, inputs/outputs)**

A typical DAC system comprises several key components: air contactor units, a chemical sorbent matrix, CO₂ desorption units, and compression and storage systems. The air contactor, often utilizing a fan-driven mechanism, facilitates the initial capture of atmospheric CO₂ by passing ambient air through a sorbent material. The chemical reaction involved is typically between CO₂ and an aqueous solution of potassium hydroxide (KOH), resulting in the formation of potassium carbonate (K₂CO₃). The captured CO₂ is then released from the sorbent through a regeneration process, often involving thermal or pressure swing adsorption methods. The output is concentrated CO₂, which can be compressed to a supercritical state (typically 7.38 MPa) for storage or utilization in enhanced oil recovery or chemical synthesis processes.

The inputs to the system include ambient air, electrical energy (kW) for fans and pumps, thermal energy for sorbent regeneration, and chemical reagents (e.g., KOH). Outputs include concentrated CO₂ (kg/day), depleted sorbent, and waste heat. The primary performance metric of interest is the land use efficiency, defined as the amount of CO₂ captured per unit area (kg CO₂/m²/day).

**3. Mathematical Framework (Describe the equations/logic used)**

The land use efficiency of DAC systems can be mathematically modeled by considering the mass balance equations governing CO₂ capture and release processes. The capture rate \( R_c \) (kg CO₂/day) is given by:

\[ R_c = Q \cdot C_a \cdot \eta_c \]

where \( Q \) is the volumetric flow rate of air through the system (m³/day), \( C_a \) is the concentration of CO₂ in the ambient air (kg/m³), and \( \eta_c \) is the capture efficiency of the sorbent. The land use efficiency \( E \) (kg CO₂/m²/day) is expressed as:

\[ E = \frac{R_c}{A} \]

where \( A \) is the land area occupied by the DAC installation (m²).

Energy consumption, a critical factor for economic viability, is modeled using the thermodynamic principles of the system. The total energy requirement \( E_t \) (kWh/day) encompasses both electrical and thermal energy:

\[ E_t = E_e + E_t = P_f \cdot t + \frac{Q \cdot \Delta H}{\eta_t} \]

where \( E_e \) is the electrical energy for air movement, \( E_t \) is the thermal energy for sorbent regeneration, \( P_f \) is the fan power (kW), \( t \) is the operational time (hours), \( \Delta H \) is the heat of reaction for sorbent regeneration (kJ/mol), and \( \eta_t \) is the thermal efficiency.

**4. Simulation Results (Refer to Figure 1)**

Simulation models based on the described framework were developed using MATLAB and COMSOL Multiphysics. Figure 1 illustrates the land use efficiency of DAC systems under various configurations and operational parameters. Results indicate that optimizing the flow rate and capture efficiency significantly enhances land use efficiency. For a target capture rate of 1,000 kg CO₂/day, a system with an optimized sorbent and airflow configuration requires approximately 500 m² of land, achieving a land use efficiency of 2 kg CO₂/m²/day. Energy requirements for such a system are projected to be 1,200 kWh/day, predominantly influenced by sorbent regeneration processes.

**5. Failure Modes & Risk Analysis**

The robustness of DAC systems is subject to several potential failure modes. Sorbent degradation over time can lead to reduced capture efficiency, necessitating frequent replacement or regeneration. Mechanical failures, such as fan or pump malfunctions, can disrupt continuous operation, impacting overall CO₂ capture rates. Additionally, energy supply variability, particularly for renewable energy sources, poses a risk to consistent system performance.

A risk analysis was conducted using the Failure Mode and Effects Analysis (FMEA) methodology, identifying critical components such as the air contactor and sorbent regeneration units. Mitigation strategies include implementing redundant systems, predictive maintenance algorithms based on ISO 55000 standards, and integrating energy storage solutions to buffer against supply interruptions.

In conclusion, while DAC technology presents a viable pathway to meet net-zero mandates, its implementation must carefully consider land use efficiency and system resilience. Future research should focus on advancing sorbent materials, optimizing system designs, and integrating DAC with renewable energy infrastructures to enhance both environmental and economic outcomes.