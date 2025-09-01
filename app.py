import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load trained model
with open("model.pkl", "rb") as f:
    model, sklearn_version = pickle.load(f)

st.title("🏦 Loan Approval Prediction App")
st.write("Enter applicant details to check loan approval prediction.")

# User input fields
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0)
loan_term = st.selectbox("Loan Term (months)", [12, 36, 60, 84, 120, 180, 240, 300, 360, 480])
credit_history = st.selectbox("Credit History", ["0", "1", "Unknown"])
property_area = st.selectbox("Property Area", ["Rural", "Semiurban", "Urban"])

# Process categorical inputs
def preprocess_input():
    # Binary encodings (same as training pipeline)
    gender_val = 1 if gender == "Male" else 0
    married_val = 1 if married == "Yes" else 0
    education_val = 1 if education == "Graduate" else 0
    self_emp_val = 1 if self_employed == "Yes" else 0

    # Credit history (map Unknown -> 2)
    if credit_history == "Unknown":
        credit_val = 2
    else:
        credit_val = int(credit_history)

    # One-hot encoding for Dependents (drop_first=True used in training)
    dep_1 = 1 if dependents == "1" else 0
    dep_2 = 1 if dependents == "2" else 0
    dep_3p = 1 if dependents == "3+" else 0

    # One-hot encoding for Property_Area (drop_first=True used in training)
    prop_semiurban = 1 if property_area == "Semiurban" else 0
    prop_urban = 1 if property_area == "Urban" else 0

    # Final feature vector (must match training order!)
    features = [
        gender_val, married_val, education_val, self_emp_val,
        applicant_income, coapplicant_income, loan_amount, loan_term, credit_val,
        dep_1, dep_2, dep_3p,
        prop_semiurban, prop_urban
    ]
    return np.array(features).reshape(1, -1)

# Predict button
if st.button("Predict Loan Approval"):
    input_data = preprocess_input()
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.success("✅ Loan Approved!")
    else:
        st.error("❌ Loan Rejected!")


