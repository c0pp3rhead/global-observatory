# Adversarial AI Attacks in Programmable Logic Controllers (PLCs) in Dual-Use Facilities
**Domain:** Biosystems Engineering (Security) | **Read Time:** 15 min
**Keywords:** Biosystems, Engineering, Modeling

**Adversarial AI Attacks in Programmable Logic Controllers (PLCs) in Dual-Use Facilities**

**1. Engineering Abstract (Problem Statement)**

In the modern landscape of biosystems engineering, dual-use facilities—those capable of manufacturing both civilian and military goods—rely heavily on Programmable Logic Controllers (PLCs) for automation and control. These PLCs are integral to maintaining operational efficiency and safety. However, the rise of adversarial artificial intelligence (AI) poses a significant threat to these systems. This research note examines the vulnerability of PLCs in dual-use facilities to adversarial AI attacks, focusing on the potential consequences for biosystems engineering. We explore the intricacies of system architecture, propose a mathematical framework for understanding these threats, and present simulation results that highlight potential failure modes. Finally, a risk analysis is conducted to assess the broader implications for facility security and operational integrity.

**2. System Architecture (Technical components, inputs/outputs)**

In dual-use facilities, PLCs are the backbone of automated process control. These devices interface with a variety of sensors and actuators to monitor and control processes such as fermentation (C2H5OH production), biopolymer synthesis (C6H10O5 units), and energy generation (measured in kW). The architecture typically includes:

- **Sensors**: Temperature (°C), pressure (MPa), and chemical concentration (mol/L) sensors provide real-time data input.
- **Actuators**: Devices such as pumps (L/min), valves, and mixers (RPM) respond to PLC commands to adjust process parameters.
- **Communication Protocols**: PLCs utilize standards like Modbus and Profibus for data exchange.
- **Control Algorithms**: Implemented via ladder logic, PID (Proportional-Integral-Derivative) controllers, and more advanced AI-driven adaptive control systems.

The outputs of these systems are critical for maintaining process stability and ensuring product quality, with deviations potentially leading to catastrophic failures, especially in high-stakes environments like biosafety level 3 (BSL-3) labs.

**3. Mathematical Framework (Describe the equations/logic used)**

The mathematical framework for assessing adversarial AI attacks on PLCs involves several key components:

- **Control Theory**: Utilizing PID control equations, where the control variable \( u(t) \) is given by:
  \[
  u(t) = K_p e(t) + K_i \int_0^t e(\tau) d\tau + K_d \frac{de(t)}{dt}
  \]
  Here, \( K_p \), \( K_i \), and \( K_d \) are the proportional, integral, and derivative gains, respectively, and \( e(t) \) is the error between setpoint and process variable.

- **Adversarial AI Algorithms**: Algorithms such as Generative Adversarial Networks (GANs) are used to simulate attack scenarios. These algorithms generate input perturbations that the PLC system wrongly interprets, leading to erroneous control actions.

- **Risk Analysis Models**: Utilizing the Failure Mode and Effects Analysis (FMEA) approach, each potential failure mode is evaluated based on its severity, occurrence, and detection, quantified by a Risk Priority Number (RPN).

**4. Simulation Results (Refer to Figure 1)**

Simulation studies were conducted using a custom-built digital twin of a dual-use fermentation facility. The twin was modeled using MATLAB/Simulink and included a detailed representation of the PLC control loop. Adversarial attacks were simulated by injecting noise into sensor data using GAN-generated perturbations.

*Figure 1* illustrates the impact of a simulated attack on the temperature control loop of an exothermic fermentation process. The results indicate that even minor perturbations can lead to significant deviations in temperature, potentially exceeding safe operating limits (e.g., surpassing 95°C from a setpoint of 37°C). Such deviations could result in catastrophic vessel failure due to overpressure (>1.5 MPa), risking operator safety and product integrity.

**5. Failure Modes & Risk Analysis**

Failure modes arising from adversarial AI attacks on PLCs include:

- **Sensor Data Corruption**: Perturbations cause the PLC to misinterpret process conditions, leading to inappropriate control actions.
- **Actuator Malfunction**: Erroneous commands result in actuator operation outside of safe parameters, e.g., pump overdrive leading to fluid overflow (>10 L/min deviation).
- **Process Instability**: Control loops fail to maintain stability, potentially causing oscillations that degrade product quality (e.g., deviation in C6H10O5 synthesis yield by >5%).

The risk analysis, conducted via FMEA, highlighted the most critical failure modes with RPNs exceeding the threshold of 200, necessitating immediate mitigation strategies. Key recommendations include:

- **Robustness Enhancement**: Implementing machine learning algorithms with in-built adversarial robustness, such as adversarial training.
- **Redundancy and Fail-safes**: Incorporating additional sensors and fail-safe mechanisms to detect and counteract unusual PLC commands.
- **Cybersecurity Protocols**: Adopting stringent cybersecurity measures compliant with ISO/IEC 27001 standards to safeguard communication channels and control logic.

In conclusion, the study underscores the pressing need for enhanced security measures in dual-use facilities. As adversarial AI techniques continue to evolve, biosystems engineers must proactively address these challenges to safeguard critical infrastructure and ensure both productivity and safety.