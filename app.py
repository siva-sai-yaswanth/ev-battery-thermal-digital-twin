import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("🔋 EV Battery Pack Thermal Management Digital Twin")
st.markdown("### Engineering Portfolio Project | Author: Mudunuri Siva Sai Yaswanth")
st.write("This tool simulates the transient thermal response and cooling efficiency of an EV battery module under varying fast-charging loads and ambient conditions.")

st.sidebar.header("Simulation Parameters")
ambient_temp = st.sidebar.slider("Ambient Temperature (°C)", min_value=-10.0, max_value=50.0, value=25.0, step=1.0)
charge_current = st.sidebar.slider("Charging Current (Amps)", min_value=50.0, max_value=400.0, value=150.0, step=10.0)
total_time = st.sidebar.slider("Simulation Duration (Minutes)", min_value=15, max_value=120, value=60, step=5)

def run_simulation(amb_t, current, duration):
    mass_kg = 50.0                
    specific_heat_j_kgk = 900.0   
    internal_resistance_ohm = 0.015 
    
    time_steps = np.arange(0, duration + 1, 1)
    temperatures = [amb_t + 5.0]
    cooling_coefficient = 35.0  

    for t in range(1, len(time_steps)):
        current_temp = temperatures[-1]
        q_gen = (current ** 2) * internal_resistance_ohm
        q_cool = cooling_coefficient * (current_temp - amb_t)
        net_heat_rate = q_gen - q_cool
        dT_dt = net_heat_rate / (mass_kg * specific_heat_j_kgk)
        new_temp = current_temp + (dT_dt * 60)
        temperatures.append(new_temp)
        
    return pd.DataFrame({
        'Time_Minutes': time_steps,
        'Battery_Temperature_C': temperatures
    })

df = run_simulation(ambient_temp, charge_current, total_time)

max_temp = df['Battery_Temperature_C'].max()
col1, col2 = st.columns(2)
col1.metric("Peak Battery Temperature", f"{max_temp:.2f} °C")
if max_temp > 55.0:
    col2.error("⚠️ Status: Thermal Throttling / Danger Zone!")
else:
    col2.success("✅ Status: Safe Operating Zone")

st.subheader("Transient Thermal Profile Over Time")
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(df['Time_Minutes'], df['Battery_Temperature_C'], color='tab:red', linewidth=2.5, label='Cell Temp (°C)')
ax.axhline(y=55.0, color='orange', linestyle='--', label='Critical Threshold (55°C)')
ax.axhline(y=ambient_temp, color='blue', linestyle=':', label='Ambient Temp (°C)')
ax.set_xlabel("Time (Minutes)")
ax.set_ylabel("Temperature (°C)")
ax.legend()
ax.grid(True)
st.pyplot(fig)
