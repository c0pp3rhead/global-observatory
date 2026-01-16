# Insider Threats in Programmable Logic Controllers (PLCs) during Pandemics
**Domain:** Biosystems Engineering (Security) | **Read Time:** 15 min
**Keywords:** Biosystems, Engineering, Modeling

**Insider Threats in Programmable Logic Controllers (PLCs) during Pandemics**

---

**1. Engineering Abstract (Problem Statement)**

The COVID-19 pandemic underscored the vulnerability of industrial control systems, particularly Programmable Logic Controllers (PLCs), to insider threats. As biosystems engineering integrates more sophisticated PLCs for critical tasks such as waste management, water purification, and food production, the potential impact of insider attacks has escalated. This research note explores the unique challenges of securing PLCs during pandemics, where remote work and reduced onsite personnel increase insider threat risks. The focus is on the quantitative assessment of these threats, employing engineering principles to propose a robust security framework.

**2. System Architecture (Technical components, inputs/outputs)**

The PLCs in focus are utilized in large-scale biosystems facilities, such as wastewater treatment plants and automated greenhouses. Key components include:

- **Processing Unit**: Executes control algorithms, typically based on ladder logic or function block diagrams.
- **Input Modules**: Receive signals from sensors (e.g., temperature, pH level).
- **Output Modules**: Send signals to actuators (e.g., pumps, valves).
- **Communication Interface**: Implements protocols such as Modbus TCP/IP, Profibus-DP for remote monitoring and control.

Inputs range from environmental data (temperature in °C, pH levels) to operational signals (flow rate in L/s, pressure in MPa). Outputs include actuator commands and system alerts.

**3. Mathematical Framework**

The mathematical framework incorporates both control theory and risk assessment models. Control logic is described using differential equations derived from the system's physical laws. For instance, the rate of change of a chemical concentration in a bioreactor (kg/day) is modeled as:

\[ \frac{dC}{dt} = -kC + I(t) \]

where \( k \) is the reaction rate constant (1/day), \( C \) is the concentration (kg/m³), and \( I(t) \) is the input flow rate (L/s).

The insider threat risk is quantified using a probabilistic risk assessment model, akin to the SIR (Susceptible-Infectious-Recovered) model used in epidemiology, adapted to account for insider activities:

\[ \frac{dS}{dt} = -\beta SI \]
\[ \frac{dI}{dt} = \beta SI - \gamma I \]
\[ \frac{dR}{dt} = \gamma I \]

where \( S \) is the number of secure components, \( I \) the compromised components, and \( R \) the recovered components. Parameters \( \beta \) (contact rate) and \( \gamma \) (recovery rate) are adapted to reflect system-specific conditions.

**4. Simulation Results**

Simulation scenarios were conducted using MATLAB/Simulink to evaluate the impact of insider threats during pandemic conditions. The scenarios varied by the number of insiders (\( n \)), the breach probability (\( p \)), and the system's resilience (\( r \)).

- **Scenario A (Figure 1)**: With \( n = 2 \), \( p = 0.05 \), and \( r = 0.9 \), the system remained operational with minor disruptions.
- **Scenario B**: Increasing \( n \) to 5, and reducing \( r \) to 0.6, led to significant operational failures, highlighting vulnerabilities.

The results demonstrate that increased remote access and reduced on-site supervision during pandemics exacerbate the risk of insider threats. Effective mitigation strategies involve enhancing authentication protocols and increasing redundancy.

**5. Failure Modes & Risk Analysis**

Failure modes were identified based on the Fault Tree Analysis (FTA) approach, focusing on:

- **Unauthorized Access**: Exploitation of remote access protocols.
- **Data Manipulation**: Alteration of sensor inputs or actuator commands, causing operational disruptions.
- **System Overload**: Induced by the simultaneous activation of multiple actuators, exceeding the system's power capacity (e.g., 500 kW).

Risk analysis, following ISO/IEC 27005 standards, prioritized risks based on likelihood and impact, recommending the deployment of advanced encryption algorithms (AES-256) and real-time anomaly detection systems.

In conclusion, the pandemic has intensified the need for robust security measures in PLCs used in biosystems engineering. By integrating control theory, risk assessment models, and simulation results, this research provides a quantitative foundation for developing strategies to mitigate insider threats, ensuring the reliability and safety of critical infrastructure. Future work includes the exploration of AI-driven anomaly detection to dynamically adapt security protocols.

---

**References**

1. ISO/IEC 27005: Information Security Risk Management.
2. IEEE 802.1X: Port-Based Network Access Control.
3. MATLAB/Simulink: High-Fidelity Simulation Software for System Modeling.