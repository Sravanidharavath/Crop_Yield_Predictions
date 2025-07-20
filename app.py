import streamlit as st #used to build interactive data apps
import numpy as np
import pickle

# Load models
dtr = pickle.load(open('dtr.pkl', 'rb'))
preprocessor = pickle.load(open('preprocessor.pkl', 'rb'))

# Streamlit UI
st.set_page_config(page_title="Crop Yield Prediction", page_icon="🌾")

st.title("🌾 Crop Yield Prediction Model")
st.markdown("Enter the agricultural parameters below to predict the **crop yield**:")

# Input form
with st.form(key='prediction_form'):
    year = st.number_input("Year", min_value=1960, max_value=2050, step=1)
    rainfall = st.number_input("Average Rainfall (mm/year)", min_value=0.0)
    pesticides = st.number_input("Pesticides Used (tonnes)", min_value=0.0)
    avg_temp = st.number_input("Average Temperature (°C)", min_value=-10.0, max_value=60.0)
    area = st.text_input("Area (Region/State)", value="India")
    item = st.text_input("Crop Type", value="Wheat")

    submit_button = st.form_submit_button(label='Predict Yield')

if submit_button:
    try:
        # Prepare input
        input_data = np.array([[year, rainfall, pesticides, avg_temp, area, item]])
        processed_input = preprocessor.transform(input_data)
        prediction = dtr.predict(processed_input)

        st.success(f"🌱 **Predicted Crop Yield:** {prediction[0]:.2f} tonnes per hectare")
    except Exception as e:
        st.error(f"⚠️ Prediction failed: {e}")
