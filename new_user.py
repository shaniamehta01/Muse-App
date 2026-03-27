import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

st.title("AI Styling Interest Predictor")

df = pd.read_csv("muse_dataset.csv")

# -------------------------------
# TRAIN MODEL
# -------------------------------
df_encoded = df.copy()
le_dict = {}

for col in df_encoded.select_dtypes(include='object').columns:
    le = LabelEncoder()
    df_encoded[col] = le.fit_transform(df_encoded[col].astype(str))
    le_dict[col] = le

X = df_encoded.drop("Adoption", axis=1)
y = df_encoded["Adoption"]

model = RandomForestClassifier()
model.fit(X, y)

model_columns = X.columns

# -------------------------------
# 🔥 SIMPLIFIED USER INPUT
# -------------------------------
st.subheader("Tell us about the user")

col1, col2 = st.columns(2)

with col1:
    shopping_freq = st.selectbox("Shopping Frequency", df["Shopping_Frequency"].unique())
    platform = st.selectbox("Shopping Platform", df["Platform"].unique())
    monthly_spend = st.slider("Monthly Spend (₹)", 500, 10000, 4000)

with col2:
    style = st.selectbox("Preferred Style", df["Style"].unique())
    struggle = st.selectbox("Struggles with outfits?", ["Yes", "No"])
    inspiration = st.selectbox("Lacks inspiration?", ["Yes", "No"])

# -------------------------------
# BUILD INPUT DATA
# -------------------------------
user_data = {
    "Shopping_Frequency": shopping_freq,
    "Platform": platform,
    "Monthly_Spend": monthly_spend,
    "Style": style,
    "Struggle_Outfits": 1 if struggle == "Yes" else 0,
    "Lack_Inspiration": 1 if inspiration == "Yes" else 0,
    "Body_Fit_Issue": 0,
    "Budget_Issue": 0,
    "Occasion_Issue": 0
}

input_df = pd.DataFrame([user_data])

# -------------------------------
# ENCODE
# -------------------------------
for col in input_df.columns:
    if col in le_dict:
        le = le_dict[col]
        input_df[col] = input_df[col].astype(str)
        input_df[col] = input_df[col].map(
            lambda x: le.transform([x])[0] if x in le.classes_ else 0
        )

# Align columns
input_df = input_df.reindex(columns=model_columns, fill_value=0)

# -------------------------------
# PREDICT
# -------------------------------
if st.button("Predict Interest"):
    prediction = model.predict(input_df)[0]
    proba = model.predict_proba(input_df).max()

    label = le_dict['Adoption'].inverse_transform([prediction])[0]

    st.subheader("Prediction Result")

    if label == "Yes":
        st.success(f"🔥 High Interest ({round(proba*100,1)}%)")
    elif label == "Maybe":
        st.warning(f"⚡ Moderate Interest ({round(proba*100,1)}%)")
    else:
        st.error(f"❌ Low Interest ({round(proba*100,1)}%)")

    st.info("👉 Use this insight to target users with personalized marketing")
