import streamlit as st
import pandas as pd
import numpy as np
import joblib
from datetime import datetime

# Load the trained model and scaler
model = joblib.load("solar_Power_Generation_model.pkl")

st.title(" Solar DC Power Forecasting App")

st.markdown("Enter the environmental conditions and date/time to predict solar power generation.")

# ✅ FIXED DATE INPUT (No format error possible now)
date_input = st.datetime_input("Select Date and Time")

IRRADIATION = st.number_input("IRRADIATION", min_value=0.0, step=0.1, format="%.2f")
MODULE_TEMPERATURE = st.number_input("MODULE TEMPERATURE (°C)", min_value=0.0, step=0.1, format="%.2f")
AMBIENT_TEMPERATURE = st.number_input("AMBIENT TEMPERATURE (°C)", min_value=0.0, step=0.1, format="%.2f")

if st.button("Predict DC Power"):
    try:
        # Extract time features directly (no strptime needed)
        hour = date_input.hour
        day = date_input.day
        month = date_input.month
        day_of_week = date_input.weekday()

        # Create feature input
        input_df = pd.DataFrame([[ 
    IRRADIATION,
    MODULE_TEMPERATURE,
    AMBIENT_TEMPERATURE
]], columns=[
    'IRRADIATION',
    'MODULE_TEMPERATURE',
    'AMBIENT_TEMPERATURE'
])

        # Scale and predict
        predicted_dc_power = model.predict(input_df)

        st.success(f"⚡ Predicted DC Power: {predicted_dc_power[0]:.4f} kW")

    except Exception as e:
        st.error(f"Error: {e}")