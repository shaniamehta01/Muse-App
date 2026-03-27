import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

st.title("New Customer Scorer")

# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv("muse_dataset.csv")

# -------------------------------
# ENCODE DATA
# -------------------------------
df_encoded = df.copy()
le_dict = {}

for col in df_encoded.select_dtypes(include='object').columns:
    le = LabelEncoder()
    df_encoded[col] = le.fit_transform(df_encoded[col].astype(str))
    le_dict[col] = le

# -------------------------------
# TRAIN MODEL
# -------------------------------
X = df_encoded.drop("Adoption", axis=1)
y = df_encoded["Adoption"]

model = RandomForestClassifier()
model.fit(X, y)

# Save column structure
model_columns = X.columns

# -------------------------------
# USER INPUT
# -------------------------------
st.subheader("Enter New User Details")

user_data = {}

for col in X.columns:
    if col in df.columns:
        unique_vals = df[col].unique()
        
        if df[col].dtype == 'object':
            user_data[col] = st.selectbox(col, unique_vals)
        else:
            user_data[col] = st.number_input(col, value=int(df[col].mean()))

# Convert to DataFrame
input_df = pd.DataFrame([user_data])

# -------------------------------
# ENCODE INPUT
# -------------------------------
for col in input_df.columns:
    if col in le_dict:
        le = le_dict[col]
        input_df[col] = input_df[col].astype(str)
        input_df[col] = input_df[col].map(
            lambda x: le.transform([x])[0] if x in le.classes_ else 0
        )

# -------------------------------
# ALIGN COLUMNS (IMPORTANT FIX)
# -------------------------------
input_df = input_df.reindex(columns=model_columns, fill_value=0)

# -------------------------------
# PREDICT
# -------------------------------
if st.button("Predict"):
    prediction = model.predict(input_df)[0]

    # Decode output
    adoption_label = le_dict['Adoption'].inverse_transform([prediction])[0]

    st.success(f"Prediction: {adoption_label}")

    if adoption_label == "Yes":
        st.info("👉 High probability of app adoption")
    elif adoption_label == "Maybe":
        st.warning("👉 Moderate interest — needs targeting")
    else:
        st.error("👉 Low interest — requires strong incentives")
