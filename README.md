# 💡 Customer Churn Prediction using ANN & Streamlit

This project focuses on predicting whether a telecom customer will **churn (leave)** using advanced **machine learning and deep learning techniques**. The goal is to help telecom companies proactively retain customers by identifying those at risk.

---

## 🧠 Problem Statement

Customer churn directly impacts company revenue. Predicting churn using customer behavioral and account data allows businesses to design better retention strategies.

---

## 📂 Dataset Overview

- **Source**: [Telco Customer Churn Dataset - Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- **Rows**: 7043  
- **Target**: `Churn` (Yes/No)

### 🔑 Key Features:
- **Demographics**: Gender, SeniorCitizen, Partner, Dependents  
- **Account Info**: Tenure, Contract, PaperlessBilling, PaymentMethod  
- **Usage & Charges**: InternetService, MonthlyCharges, TotalCharges  

---

## ⚙️ Workflow Summary

### ✅ 1. Data Preprocessing
- Removed irrelevant column: `customerID`
- Handled nulls in `TotalCharges`
- Encoded categorical columns
- Normalized numerical features
- Converted target `Churn` to binary (Yes → 1, No → 0)

### ✅ 2. Handling Imbalanced Data
Implemented and compared different sampling techniques to address **class imbalance**:
- **Under-sampling**
- **Over-sampling**
- **SMOTE (Synthetic Minority Over-sampling Technique)**

### ✅ 3. Model Building with ANN
Used an **Artificial Neural Network** with:
- Input, Hidden, and Output layers
- Activation: `ReLU`, `Sigmoid`
- Optimizer: `Adam`
- Loss: `binary_crossentropy`

### ✅ 4. Evaluation Metrics
- Accuracy Score
- Confusion Matrix
- Precision, Recall, F1-Score
- ROC-AUC Score

### ✅ 5. Ensemble Techniques
Used **Voting Classifier** and **Bagging** to improve model robustness and performance.

---

## 🧪 Model Results

| Technique         | Accuracy | AUC Score | Remarks                         |
|------------------|----------|-----------|----------------------------------|
| ANN (SMOTE)      | 83.2%    | 0.86      | Best performance overall ✅       |
| ANN (Over-sample)| 81.7%    | 0.84      | Good with slightly lower recall |
| ANN (Under-sample)| 78.4%   | 0.81      | Less effective due to data loss |
| Ensemble Voting  | 82.5%    | 0.85      | Robust alternative model        |

---

## 🌐 Streamlit Web App

A lightweight web application was built using **Streamlit** to allow users to:
- Input customer data
- View prediction result (Churn or Not)
- See model accuracy and explanation

### ▶️ To run the app:
```bash
streamlit run app.py
