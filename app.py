
import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
# Load the trained model
model = load_model("churn_model.h5")

st.title("Customer Churn Prediction App")

# Collect inputs
gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.slider("Tenure (scaled)", 0.0, 1.0, 0.5)
phone_service = st.selectbox("Phone Service", ["Yes", "No"])
multiple_lines = st.selectbox("Multiple Lines", ["Yes", "No"])
online_security = st.selectbox("Online Security", ["Yes", "No"])
online_backup = st.selectbox("Online Backup", ["Yes", "No"])
device_protection = st.selectbox("Device Protection", ["Yes", "No"])
tech_support = st.selectbox("Tech Support", ["Yes", "No"])
streaming_tv = st.selectbox("Streaming TV", ["Yes", "No"])
streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No"])
paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
monthly_charges = st.slider("Monthly Charges (scaled)", 0.0, 1.0, 0.5)
total_charges = st.slider("Total Charges (scaled)", 0.0, 1.0, 0.5)
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
payment_method = st.selectbox("Payment Method", [
    "Bank transfer (automatic)", "Credit card (automatic)",
    "Electronic check", "Mailed check"
])

# Helper function
def bin_encode(val): return 1 if val == "Yes" or val == "Female" else 0

# Prepare input vector
input_data = [
    bin_encode(gender),
    senior,
    bin_encode(partner),
    bin_encode(dependents),
    tenure,
    bin_encode(phone_service),
    bin_encode(multiple_lines),
    bin_encode(online_security),
    bin_encode(online_backup),
    bin_encode(device_protection),
    bin_encode(tech_support),
    bin_encode(streaming_tv),
    bin_encode(streaming_movies),
    bin_encode(paperless_billing),
    monthly_charges,
    total_charges,
    # One-hot for Internet Service
    1 if internet_service == "DSL" else 0,
    1 if internet_service == "Fiber optic" else 0,
    1 if internet_service == "No" else 0,
    # One-hot for Contract
    1 if contract == "Month-to-month" else 0,
    1 if contract == "One year" else 0,
    1 if contract == "Two year" else 0,
    # One-hot for Payment Method
    1 if payment_method == "Bank transfer (automatic)" else 0,
    1 if payment_method == "Credit card (automatic)" else 0,
    1 if payment_method == "Electronic check" else 0,
    1 if payment_method == "Mailed check" else 0,
]

# Prediction
if st.button("Predict"):
    prediction = model.predict(np.array([input_data]))
    result = "Yes" if prediction[0][0] > 0.5 else "No"
    st.success(f"Churn Prediction: {result}")
