import requests
import streamlit as st

st.title("HR Attrition Prediction Demo")

age = st.number_input("Age", 18, 60)
income = st.number_input("Monthly Income", 1000, 20000)
distance = st.number_input("Distance From Home", 1, 30)
satisfaction = st.slider("Job Satisfaction", 1, 4)

if st.button("Predict Attrition"):
    payload = {
        "Age": age,
        "MonthlyIncome": income,
        "DistanceFromHome": distance,
        "JobSatisfaction": satisfaction
    }

    response = requests.post("http://127.0.0.1:8000/predict", json=payload)

    st.subheader("Prediction:")
    st.write(response.json())
