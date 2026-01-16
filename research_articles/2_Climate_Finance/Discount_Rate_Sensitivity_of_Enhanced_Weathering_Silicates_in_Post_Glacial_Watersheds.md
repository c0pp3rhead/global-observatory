# Discount Rate Sensitivity of Enhanced Weathering Silicates in Post-Glacial Watersheds
**Domain:** Biosystems Engineering (Finance) | **Read Time:** 15 min
**Keywords:** Biosystems, Engineering, Modeling

**Title: Discount Rate Sensitivity of Enhanced Weathering Silicates in Post-Glacial Watersheds**

**1. Engineering Abstract (Problem Statement)**

Enhanced weathering (EW) using silicate minerals has emerged as a promising carbon dioxide removal (CDR) strategy, particularly in post-glacial watersheds where mineral availability and weathering potential are high. However, the financial viability of EW projects is heavily influenced by the discount rate applied to future benefits and costs. This research note addresses the sensitivity of EW projects to discount rate variations, specifically focusing on the application of silicate minerals in post-glacial watersheds. By incorporating financial models into biosystems engineering, we aim to provide a comprehensive evaluation of EW projects' economic feasibility over time, considering technical, environmental, and financial factors.

**2. System Architecture**

The system architecture for evaluating the financial viability of EW using silicates in post-glacial watersheds encompasses several technical components and processes:

- **Mineral Input**: Olivine (\(\text{Mg}_2\text{SiO}_4\)) and basalt (\(\text{CaMg(\text{CO}_3)_2}\)) are the primary silicate minerals utilized. These are sourced from local quarries, reducing transportation costs and associated emissions.
  
- **Weathering Process**: The minerals are distributed across targeted watershed areas, where natural hydrological processes facilitate weathering. The dissolution of these minerals captures atmospheric CO\(_2\) and converts it into bicarbonates.

- **Outputs**: The primary output is the sequestration of CO\(_2\) (measured in kg/day) and the stabilization of watershed pH levels. Secondary benefits include enhanced soil fertility and increased agricultural yields.

- **Financial Model Inputs**: Key financial input variables include mineral extraction and transportation costs, CO\(_2\) market prices, and the discount rate, expressed in percentage terms.

- **Outputs**: The model outputs a net present value (NPV) for the project, accounting for varying discount rates and CO\(_2\) price scenarios.

**3. Mathematical Framework**

The economic assessment of enhanced weathering in post-glacial watersheds involves several mathematical models and equations:

- **Weathering Kinetics**: The rate of mineral dissolution is modeled using the Arrhenius equation, accounting for temperature-dependent reaction rates:
  \[
  k = A \exp\left(-\frac{E_a}{RT}\right)
  \]
  where \(k\) is the rate constant, \(A\) is the pre-exponential factor, \(E_a\) is the activation energy (kJ/mol), \(R\) is the universal gas constant, and \(T\) is the temperature (K).

- **Carbon Sequestration**: The amount of CO\(_2\) captured is calculated using:
  \[
  \text{CO}_2 = \text{MW}_{\text{CO}_2} \times \frac{\text{mass}_{\text{mineral}} \times \text{weathering efficiency}}{\text{MW}_{\text{mineral}}}
  \]
  where MW denotes molecular weight.

- **Financial Model**: The NPV of the project is calculated using:
  \[
  \text{NPV} = \sum_{t=0}^{n} \frac{R_t - C_t}{(1 + r)^t}
  \]
  where \(R_t\) is the revenue from carbon credits at time \(t\), \(C_t\) is the cost, \(r\) is the discount rate, and \(n\) is the project lifespan.

- **Discount Rate Sensitivity**: The sensitivity of NPV to changes in the discount rate is analyzed using partial derivative techniques, providing insights into threshold rates beyond which the project becomes non-viable.

**4. Simulation Results**

The simulation results (refer to Figure 1) demonstrate the relationship between the discount rate and the NPV of EW projects. At a discount rate of 2%, the NPV is positive, indicating economic viability over a 20-year project horizon. As the discount rate increases to 5%, the NPV declines significantly, highlighting the importance of securing low-cost financing or government subsidies to enhance project attractiveness.

Figure 1 also illustrates the impact of varying CO\(_2\) market prices on project profitability. Higher CO\(_2\) prices offset the negative impact of higher discount rates, suggesting a synergistic effect between policy-driven carbon pricing and EW project success.

**5. Failure Modes & Risk Analysis**

Several potential failure modes and risks could impact the financial and operational success of EW projects:

- **Mineral Supply Chain Risks**: Disruptions in local quarry operations or transportation logistics could lead to cost overruns and project delays. Mitigation strategies include diversifying supply sources and establishing long-term contracts.

- **Weathering Rate Variability**: Uncertainties in weathering kinetics due to variable climatic conditions could affect CO\(_2\) capture efficiency. Real-time monitoring and adaptive management strategies are essential for optimizing weathering outcomes.

- **Financial Risk**: Fluctuations in CO\(_2\) market prices and discount rates could impact project returns. Developing flexible financial models that incorporate scenario analysis and Monte Carlo simulations can provide robustness against market volatility.

- **Regulatory and Environmental Risks**: Changes in environmental regulations or public opposition to mineral application could pose significant risks. Engaging stakeholders and adhering to ISO environmental standards can enhance project acceptance and compliance.

In conclusion, this research note elucidates the critical role of discount rate sensitivity in the financial viability of enhanced weathering projects in post-glacial watersheds. By integrating technical, environmental, and financial analyses, we provide a comprehensive framework for evaluating the economic potential of EW as a scalable CDR solution. Future work should focus on refining weathering models and exploring innovative financing mechanisms to support the widespread deployment of EW technologies.