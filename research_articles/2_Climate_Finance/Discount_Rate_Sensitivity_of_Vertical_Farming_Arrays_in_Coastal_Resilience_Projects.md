# Discount Rate Sensitivity of Vertical Farming Arrays in Coastal Resilience Projects
**Domain:** Biosystems Engineering (Finance) | **Read Time:** 15 min
**Keywords:** Biosystems, Engineering, Modeling

**Biosystems Engineering Research Note: Discount Rate Sensitivity of Vertical Farming Arrays in Coastal Resilience Projects**

**1. Engineering Abstract (Problem Statement)**

The increasing vulnerability of coastal regions to climate change and rising sea levels necessitates innovative solutions for enhancing resilience and sustainability. Vertical farming arrays (VFAs) present a promising approach by integrating food production with coastal protection strategies. However, the financial viability of such projects is heavily influenced by the discount rate, a critical factor in net present value (NPV) calculations. This research note investigates the sensitivity of VFAs to discount rate variations within the context of coastal resilience projects. By analyzing the economic and engineering aspects, we aim to provide a comprehensive understanding of how discount rates impact the feasibility of implementing VFAs in these regions.

**2. System Architecture (Technical Components, Inputs/Outputs)**

The VFA system is composed of several integrated components designed to optimize both agricultural yield and coastal protection. Key components include:

- **Structural Framework:** The physical support structure, typically made from high-grade stainless steel (ASTM A240) capable of withstanding marine environments, is designed to support hydroponic modules and environmental control systems.

- **Hydroponic Modules:** Utilizing nutrient film technique (NFT) systems, these modules deliver essential nutrients (N, P, K) in solution, with a flow rate of 1 L/min per channel, optimized for crops such as Lactuca sativa (lettuce) and Solanum lycopersicum (tomato) with yields up to 10 kg/m²/day.

- **Environmental Control Systems:** These include sensors and actuators for regulating temperature, humidity, and CO₂ levels, utilizing algorithms compliant with IEEE 1451 standards for smart transducer interfaces.

- **Energy Systems:** The energy demand, approximately 50 kW per module, is met through a combination of solar photovoltaic panels (ISO 9050) and grid backup, ensuring a reliable supply even during adverse weather conditions.

Outputs include high-density crop production and enhanced coastal resilience through wave attenuation and sediment stabilization.

**3. Mathematical Framework (Describe the Equations/Logic Used)**

The financial analysis of VFAs is grounded in the NPV model, where the cash flows are discounted at a specific rate to assess the project's viability. The NPV is calculated using:

\[ \text{NPV} = \sum_{t=0}^{T} \frac{R_t - C_t}{(1 + r)^t} \]

where \( R_t \) is the revenue generated from crop sales and ecosystem services (USD), \( C_t \) is the cost of operation and maintenance (USD), \( r \) is the discount rate (expressed as a decimal), and \( t \) is the time in years.

The sensitivity analysis involves varying \( r \) from 0.02 to 0.10 to observe its impact on NPV. Additionally, the Black-Scholes option pricing model is adapted to assess the flexibility value of delaying investments under uncertainty:

\[ C = S_0 N(d_1) - Xe^{-rt} N(d_2) \]

where \( C \) is the call option value, \( S_0 \) is the current project value, \( X \) is the exercise price, and \( N(d) \) are cumulative normal distribution functions.

**4. Simulation Results (Refer to Figure 1)**

Simulation results, as illustrated in Figure 1, demonstrate a significant sensitivity of NPV to discount rate variations. At a 2% discount rate, the NPV remains positive, indicating project feasibility. However, as the rate increases to 10%, the NPV turns negative, suggesting economic infeasibility. Notably, the option value analysis shows that delaying investment during high uncertainty periods can add substantial value, justifying the use of real options in project planning.

**5. Failure Modes & Risk Analysis**

The primary failure modes identified include structural failure due to extreme weather events (e.g., hurricanes with wind speeds >150 km/h), nutrient delivery system malfunctions, and energy supply disruptions. Risk analysis, conducted using Fault Tree Analysis (FTA), highlights the critical components and failure probabilities.

- **Structural Failure:** Risk mitigated by designing to withstand pressures up to 200 MPa, with redundancy in load-bearing elements.

- **Nutrient System Failure:** Addressed by implementing ISO 9001-certified quality management protocols and redundant pump systems.

- **Energy Supply Disruption:** Mitigated through hybrid solar-grid systems with battery storage, ensuring a 99.9% uptime.

In conclusion, the research underscores the importance of discount rate consideration in the financial planning of VFA systems within coastal resilience projects. By integrating engineering design with financial analysis, stakeholders can make informed decisions to enhance both economic and environmental benefits. Further research is recommended to refine real options valuation and explore alternative financing mechanisms for broader implementation.