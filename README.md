# 🔋 EV Battery Pack Thermal Management Digital Twin

A physics-based transient thermal simulation and interactive web dashboard modeling the thermal behavior, heat generation, and cooling efficiency of an Electric Vehicle (EV) lithium-ion battery pack under fast-charging conditions.

## 🚀 Live Demo
*(You can mention that it runs locally via Streamlit or note the simulation architecture below)*

## 🧠 Engineering & Physics Background
Fast-charging electric vehicles places severe thermal stress on battery cells. This digital twin models the energy balance equation:
$$\frac{dT}{dt} = \frac{Q_{\text{gen}} - Q_{\text{cool}}}{m \cdot c_p}$$

* **Heat Generation ($Q_{\text{gen}}$):** Calculated via Ohmic heating ($I^2 \cdot R$) based on charging current and internal cell resistance.
* **Heat Dissipation ($Q_{\text{cool}}$):** Modeled using a cooling plate coefficient and convection relative to ambient temperature.
* **Safety Thresholds:** Automatically flags thermal throttling and critical temperature warnings if cell temperatures exceed $55^\circ\text{C}$.

## 🛠️ Tech Stack
* **Python** (NumPy, Pandas, Matplotlib)
* **Streamlit** (Interactive Web Dashboard UI)
* **Git & GitHub** (Version Control & Documentation)

## ⚙️ How to Run Locally
1. Clone this repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/ev-battery-thermal-digital-twin.git](https://github.com/YOUR_USERNAME/ev-battery-thermal-digital-twin.git)
