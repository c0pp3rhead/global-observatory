# Discount Rate Sensitivity of Direct Air Capture (DAC) in Coastal Resilience Projects
**Domain:** Biosystems Engineering (Finance) | **Read Time:** 15 min
**Keywords:** Biosystems, Engineering, Modeling

**Title: Discount Rate Sensitivity of Direct Air Capture (DAC) in Coastal Resilience Projects**

---

**1. Engineering Abstract (Problem Statement)**

Direct Air Capture (DAC) technology, which chemically extracts CO2 from the atmosphere, emerges as a promising approach in coastal resilience projects, aimed at mitigating climate change impacts. The economic viability of DAC systems predominantly hinges on the discount rate applied during financial assessments. This research note explores the sensitivity of DAC's cost-effectiveness to discount rate variations within coastal resilience frameworks, focusing on the complex interplay between technological efficiency, economic assumptions, and environmental benefits. By quantifying this sensitivity, we aim to provide insights into financial planning and risk management for stakeholders in biosystems engineering and coastal management.

---

**2. System Architecture (Technical Components, Inputs/Outputs)**

The DAC system architecture integrates several technical components: an air contactor, a chemical sorbent system, a regeneration unit, and a compression stage. Air is first drawn through the contactor using fans operating at 5 kW, capturing CO2 with a sorbent such as KOH (potassium hydroxide). The air contactor processes approximately 1000 kg of air per hour, capturing CO2 concentrations of about 400 ppm. 

The captured CO2 is then released from the sorbent in a regeneration unit operating at 120°C and 1.5 MPa, requiring energy input of approximately 2.5 GJ per ton of CO2. Post-regeneration, CO2 is compressed to supercritical state for transport or storage, necessitating additional energy input around 1.0 GJ per ton of CO2.

**Inputs:**
- Ambient air (1000 kg/hour)
- Energy (kW, GJ per ton CO2)
- Sorbent (KOH)

**Outputs:**
- Captured CO2 (kg/day)
- Energy consumption (kW, GJ)
- Operational cost per ton of CO2 (USD)

---

**3. Mathematical Framework**

To analyze the financial dynamics of DAC systems within coastal resilience projects, we employ a modified Net Present Value (NPV) model. The NPV is calculated using the following formula:

\[ NPV = \sum_{t=0}^{T} \frac{C_t}{(1 + r)^t} \]

Where:
- \(C_t\) represents the net cash flow at time \(t\), combining operating costs, carbon credit revenues, and tax incentives.
- \(r\) is the discount rate, a variable of interest in our sensitivity analysis.
- \(T\) is the project lifespan, typically considered as 20 years.

To capture the economic implications of CO2 removal, we integrate a carbon pricing mechanism and potential penalties for non-compliance with environmental standards, as per ISO 14064 guidelines. The analysis also considers the stochastic nature of future energy prices using a Geometric Brownian Motion (GBM) model:

\[ dP = \mu P dt + \sigma P dW \]

Where:
- \(P\) is the energy price,
- \(\mu\) and \(\sigma\) are the drift and volatility parameters,
- \(dW\) represents a Wiener process.

---

**4. Simulation Results (Refer to Figure 1)**

Our simulations, conducted using Monte Carlo methods, reveal a pronounced sensitivity of NPV to discount rate adjustments. Figure 1 illustrates NPV trajectories under varying discount rates (2%, 4%, 6%). At lower discount rates (2%), DAC projects exhibit a positive NPV, driven by enhanced valuation of future carbon credits and environmental benefits. Conversely, higher rates (6%) significantly diminish project viability, underscoring the criticality of financial assumptions in project planning.

**Figure 1**: NPV Sensitivity Analysis for DAC Systems in Coastal Resilience Projects.

---

**5. Failure Modes & Risk Analysis**

The implementation of DAC systems in coastal resilience projects is fraught with potential failure modes, necessitating a comprehensive risk analysis. Key risks include:

- **Technical Failures**: Sorbent degradation and mechanical breakdowns could impede CO2 capture efficiency, elevating operational costs. Regular maintenance schedules and adherence to IEEE 1547 standards for system reliability are recommended.

- **Economic Risks**: Fluctuations in energy prices and carbon markets can affect financial outcomes. Hedging strategies and adaptive financial models are essential to mitigate such risks.

- **Environmental Risks**: Coastal ecosystems may face unforeseen impacts from DAC operations, such as sorbent leakage or thermal pollution. Implementing ISO 14001 environmental management systems can help manage such risks.

In conclusion, the discount rate plays a pivotal role in the financial feasibility of DAC projects within coastal resilience efforts. Rigorous sensitivity analysis and risk management strategies are imperative for informed decision-making in biosystems engineering finance.

---

**References**

- International Organization for Standardization (ISO) 14064
- Institute of Electrical and Electronics Engineers (IEEE) 1547
- Relevant literature on Geometric Brownian Motion in financial modeling.

---

This research note provides a comprehensive overview of the economic and technical considerations necessary for integrating DAC systems into coastal resilience projects. Through quantitative analysis and risk assessment, we aim to pave the way for sustainable and financially viable environmental engineering solutions.