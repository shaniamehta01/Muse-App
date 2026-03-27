import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

st.title("New Customer Scorer")

# Load data
df = pd.read_csv("muse_dataset.csv")

# Encode
le = LabelEncoder()
df_encoded = df.copy()

for col in df_encoded.select_dtypes(include='object').columns:
    df_encoded[col] = le.fit_transform(df_encoded[col].astype(str))

# Train model
X = df_encoded.drop("Adoption", axis=1)
y = df_encoded["Adoption"]

model = RandomForestClassifier()
model.fit(X, y)

st.subheader("Enter New Customer Details")

# Simple input fields (keep it basic)
monthly_spend = st.number_input("Monthly Spend", 0, 5000, 1000)
outfit_budget = st.number_input("Outfit Budget", 0, 5000, 1000)

struggle = st.selectbox("Struggles with outfits?", ["Yes", "No"])
inspiration = st.selectbox("Needs inspiration?", ["Yes", "No"])

# Convert input into dataframe
input_data = pd.DataFrame({
    "Monthly_Spend": [monthly_spend],
    "Outfit_Budget": [outfit_budget],
    "Struggle_Outfits": [1 if struggle=="Yes" else 0],
    "Lack_Inspiration": [1 if inspiration=="Yes" else 0]
})

# Fill missing columns
for col in X.columns:
    if col not in input_data.columns:
        input_data[col] = 0

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("High chance of adoption ✅")
    else:
        st.error("Low chance of adoption ❌")
