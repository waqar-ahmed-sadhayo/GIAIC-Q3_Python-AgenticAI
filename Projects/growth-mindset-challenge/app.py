import streamlit as st
import numpy as np
import joblib
from pathlib import Path

# Get the current directory of the script
base_path = Path(__file__).resolve().parent

# Load Scaler.pkl
scaler_path = base_path / 'Scaler.pkl'
model_path = base_path / 'model.pkl'

try:
    scaler = joblib.load(scaler_path)
except FileNotFoundError:
    st.error("Scaler.pkl file not found. Make sure it's uploaded with the app.")
    st.stop()

try:
    model = joblib.load(model_path)
except FileNotFoundError:
    st.error("model.pkl file not found. Make sure it's uploaded with the app.")
    st.stop()


st.set_page_config(page_title="🏠 Real Estate Price Predictor 🧮", layout="wide")

# App title
st.title("🏠 Real Estate Price Predictor 🧮")
st.subheader("Estimate your property's worth instantly!")

st.divider()

# Inputs
bed = st.number_input("Enter the number of bedrooms", value=2, step=1)
bath = st.number_input("Enter the number of bathrooms", value=1, step=1)
size = st.number_input("Enter the size:", value=1000, step=50)

X = [bed, bath, size]
st.divider()

# Button and prediction
predict_button = st.button("📈 Predict!")
st.divider()

if predict_button:
    st.balloons()
    X_array = scaler.transform([np.array(X)])
    prediction = model.predict(X_array)[0]
    st.success(f"The predicted price is: {prediction:.2f}")
else:
    st.info("Click the button to generate prediction.")


st.markdown("""
Develop with 💖 *Waqar Ahmed*
""")