import streamlit as st
import numpy as np
import joblib  # For loading scaler and model

scaler = joblib.load('E:\GIAIC-Q3_Python-AgenticAI\Projects\growth-mindset-challenge\Scaler.pkl')

model = joblib.load('model.pkl')

st.title("Real Estate Price Prediction App")

st.divider()

bed = st.number_input("Enter the number of bedrooms", value=2, step=1)
bath = st.number_input("Enter the number of bathrooms", value=1, step=1 )
size = st.number_input("Enter the size:", value=1000, step=50)

X = [bed, bath, size]

st.divider()

predict_button = st.button("Predict!")

st.divider()

if predict_button:

    st.balloons()

    X1 = np.array(X)

    X_array = scaler.transform([X1])

    prediction = model.predict(X_array)[0]

    st.write(f"The Prediction is: {prediction:.2f}")

else:
    st.warning("PLease use the button for prediction")