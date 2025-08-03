import streamlit as st
import numpy as np
import joblib
import os

# Configure Streamlit page
st.set_page_config(page_title="Smart Sprinkler System", layout="wide")

# Load the trained model
@st.cache_resource
def load_model():
    model_path = os.path.join(os.path.dirname(__file__), "Farm_Irrigation_System.pkl")
    if os.path.exists(model_path):
        return joblib.load(model_path)
    else:
        st.error("❌ Model file not found. Please ensure 'Farm_Irrigation_System.pkl' is in the same folder.")
        return None

model = load_model()

# Title and project description
st.title("Smart Sprinkler System")
st.markdown("### Project: **Smart/Automated Irrigation using Soil Moisture and Weather Data**")
st.subheader("AI-based Prediction of Sprinkler Status")

# Footer info (above inputs)
st.markdown("""---  
Developed as part of **AICTE Internship Project**  
Submitted by: **Dendi Bhavya Reddy**
---""")

st.markdown("Enter **scaled sensor values (0 to 1)** for each of the 20 sensors to predict ON/OFF status for 3 sprinklers.")

# Input sliders for 20 sensors
sensor_values = []
columns = st.columns(4)
for i in range(20):
    with columns[i % 4]:
        val = st.slider(f"Sensor {i}", 0.0, 1.0, 0.5, 0.01)
        sensor_values.append(val)

# Predict sprinkler status
if st.button("Predict Sprinklers"):
    if model:
        input_array = np.array(sensor_values).reshape(1, -1)
        prediction = model.predict(input_array)[0]

        # Validate that output is for 3 sprinklers
        if len(prediction) == 3:
            st.markdown("### 💧 Sprinkler Status Prediction:")
            result_cols = st.columns(3)
            for i, status in enumerate(prediction):
                with result_cols[i]:
                    st.success(f"Sprinkler {i}: {'ON ' if status == 1 else 'OFF '}")
        else:
            st.error(f" Unexpected model output: expected 3 values, got {len(prediction)}.")
    else:
        st.warning("Model could not be loaded.")