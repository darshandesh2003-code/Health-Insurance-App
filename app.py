import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load Saved Gradient Boosting Pipeline
model = joblib.load("Gradient Boosting.pkl")

# App Title
st.title("Insurance Price Prediction")

st.write("Enter the details below to predict insurance charges.")

# =========================
# User Inputs
# =========================

age = st.number_input(
    "Enter Age",
    min_value=18,
    max_value=100,
    value=25
)

sex = st.selectbox(
    "Select Gender",
    ["male", "female"]
)

bmi = st.number_input(
    "Enter BMI",
    min_value=10.0,
    max_value=60.0,
    value=25.0
)

children = st.number_input(
    "Number of Children",
    min_value=0,
    max_value=10,
    value=0
)

smoker = st.selectbox(
    "Smoker",
    ["yes", "no"]
)

region = st.selectbox(
    "Region",
    ["northeast", "northwest", "southeast", "southwest"]
)

# =========================
# Encoding Inputs
# =========================
if st.button("Predict"):

    # Encoding
    smoker_value = 1 if smoker == "yes" else 0

    sex_female = 1 if sex == "female" else 0
    sex_male = 1 if sex == "male" else 0

    region_value = {
        'southwest': 0,
        'northwest': 1,
        'northeast': 2,
        'southeast': 3
    }[region]

    # Create Input DataFrame
    input_data = pd.DataFrame({
        'age': [float(age)],
        'bmi': [float(bmi)],
        'children': [int(children)],

        'Smoker': [int(smoker_value)],

        'sex_female': [int(sex_female)],
        'sex_male': [int(sex_male)],

        'Region': [int(region_value)]
    })

    # Prediction
    prediction = model.predict(input_data)

    final_price =np.exp(prediction[0])
    st.success(
        f"Predicted Insurance Price: ₹ {final_price:,.2f}"
    )