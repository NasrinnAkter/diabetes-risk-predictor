import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Diabetes Risk Predictor", page_icon="🩺")

model = joblib.load("model.pkl")

st.title("🩺 Diabetes Risk Predictor")
st.write(
    "Enter patient measurements to estimate diabetes risk. "
    "Built with Python, scikit-learn and Streamlit on the Pima Indians Diabetes dataset."
)

col1, col2 = st.columns(2)
with col1:
    pregnancies = st.number_input("Pregnancies", 0, 20, 1)
    glucose = st.number_input("Glucose (mg/dL)", 40, 250, 120)
    blood_pressure = st.number_input("Blood pressure (mm Hg)", 20, 150, 72)
    skin = st.number_input("Skin thickness (mm)", 5, 100, 29)
with col2:
    insulin = st.number_input("Insulin (mu U/ml)", 10, 900, 125)
    bmi = st.number_input("BMI", 10.0, 70.0, 32.0)
    dpf = st.number_input("Diabetes pedigree function", 0.05, 2.5, 0.37)
    age = st.number_input("Age", 15, 100, 30)

if st.button("Predict risk"):
    data = pd.DataFrame(
        [[pregnancies, glucose, blood_pressure, skin, insulin, bmi, dpf, age]],
        columns=["Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
                 "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"],
    )
    prob = model.predict_proba(data)[0][1]
    st.metric("Estimated diabetes risk", f"{prob * 100:.1f}%")
    if prob >= 0.5:
        st.error("Higher risk of diabetes")
    else:
        st.success("Lower risk of diabetes")
    st.progress(float(prob))

st.caption("Educational project only. This is not medical advice or a diagnosis.")
