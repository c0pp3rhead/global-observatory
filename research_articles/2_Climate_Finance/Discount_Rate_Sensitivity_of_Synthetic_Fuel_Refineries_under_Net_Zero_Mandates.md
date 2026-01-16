# Discount Rate Sensitivity of Synthetic Fuel Refineries under Net-Zero Mandates
**Domain:** Biosystems Engineering (Finance) | **Read Time:** 15 min
**Keywords:** Biosystems, Engineering, Modeling

**Engineering Abstract**

The transition to net-zero carbon emissions has accelerated the development of synthetic fuel refineries, which utilize renewable energy to convert atmospheric CO\(_2\) and water into hydrocarbon fuels. As these systems gain traction, understanding their financial viability under varying economic conditions becomes critical. This research note investigates the discount rate sensitivity of synthetic fuel refineries, focusing on the impact of fluctuating economic parameters on the financial sustainability of these systems under net-zero mandates. A rigorous financial analysis is conducted, incorporating engineering-economic models and stochastic simulations to assess the viability and resilience of these refineries.

**System Architecture**

The synthetic fuel refinery system is composed of several interconnected components, including CO\(_2\) capture units, electrolysis modules, and Fischer-Tropsch synthesis reactors. The CO\(_2\) capture unit employs an amine-based absorption process, operating at 1.5 MPa, to extract CO\(_2\) from ambient air. This CO\(_2\) is then fed into the high-temperature electrolysis unit (operating at 750°C) powered by renewable energy sources, such as solar photovoltaics (PV) and wind turbines, to produce hydrogen gas (H\(_2\)).

The system's electrolysis units are designed to deliver a throughput of 1000 kg/day of H\(_2\), operating at a conversion efficiency of 70%. The synthesized H\(_2\) and captured CO\(_2\) are subsequently introduced into the Fischer-Tropsch reactor, which operates at 2.5 MPa and 220°C, to produce synthetic hydrocarbons. The final output includes a range of liquid fuels, such as synthetic diesel and kerosene, with a production capacity of 500 barrels per day.

**Mathematical Framework**

The financial model for synthetic fuel refineries is based on the Net Present Value (NPV) approach, incorporating elements of the Black-Scholes option pricing model to account for uncertainties in input costs and market prices. The NPV is calculated using the formula:

\[ \text{NPV} = \sum_{t=0}^{T} \frac{R_t - C_t}{(1 + r)^t} \]

where \(R_t\) is the revenue at time \(t\), \(C_t\) is the cost at time \(t\), \(r\) is the discount rate, and \(T\) is the project lifespan. The discount rate \(r\) is treated as a stochastic variable following a geometric Brownian motion, characterized by:

\[ dr = \mu r dt + \sigma r dW_t \]

where \(\mu\) is the drift term, \(\sigma\) is the volatility, and \(dW_t\) is the Wiener process increment.

Additionally, the engineering model incorporates the thermodynamic and kinetic equations governing the system's operation. Specifically, the energy balance for the electrolysis unit follows:

\[ \Delta H = \Delta G + T\Delta S \]

where \(\Delta H\) is the enthalpy change, \(\Delta G\) is the Gibbs free energy change, and \(T\Delta S\) is the entropy change at temperature \(T\).

**Simulation Results**

Simulations were conducted using MATLAB and Simulink, employing Monte Carlo methods to generate a range of potential outcomes for the financial model. Figure 1 illustrates the sensitivity of the NPV to varying discount rates, showing a significant impact on financial feasibility as rates fluctuate between 2% and 10%. The probability distribution of NPVs reveals a bimodal pattern, indicating distinct scenarios of financial success and failure.

The results demonstrate that a lower discount rate increases the probability of achieving a positive NPV, rendering the project financially viable. Conversely, higher discount rates decrease this likelihood, emphasizing the importance of securing favorable financing conditions.

**Failure Modes & Risk Analysis**

The analysis identifies several critical failure modes that could jeopardize the financial and operational success of synthetic fuel refineries. These include:

1. **Feedstock Supply Risk**: Variability in CO\(_2\) capture efficiency could lead to feedstock shortages, impacting fuel output. Mitigation strategies involve enhancing capture technology and diversifying energy sources.

2. **Technological Failure**: The reliability of high-temperature electrolysis is essential. Potential failures include system degradation due to thermal stress. Compliance with ISO 9001 standards for quality management can mitigate these risks.

3. **Market Volatility**: Fluctuations in energy and fuel prices introduce economic uncertainty. The integration of real options analysis, akin to the Black-Scholes model, can provide strategic flexibility in investment decisions.

4. **Regulatory Changes**: Shifts in net-zero mandates and carbon pricing policies could affect project economics. Continuous monitoring of regulatory frameworks is essential to adapt to policy changes.

In conclusion, the financial viability of synthetic fuel refineries under net-zero mandates is highly sensitive to discount rate variations. This study underscores the necessity of robust financial planning, technological innovation, and strategic risk management to ensure the success of these emerging systems. Future research should focus on optimizing system components and exploring alternative financing mechanisms to bolster resilience against economic uncertainties.