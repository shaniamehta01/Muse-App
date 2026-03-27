import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_curve, auc
import plotly.express as px

st.title("Predictive Model (Adoption Prediction)")

df = pd.read_csv("muse_dataset.csv")

# Encode
le = LabelEncoder()
for col in df.select_dtypes(include='object').columns:
    df[col] = le.fit_transform(df[col].astype(str))

X = df.drop("Adoption", axis=1)
y = df["Adoption"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

st.markdown("### Model Performance")

st.write("Accuracy:", round(accuracy_score(y_test, y_pred), 2))
st.write("Precision:", round(precision_score(y_test, y_pred, average='weighted'), 2))
st.write("Recall:", round(recall_score(y_test, y_pred, average='weighted'), 2))
st.write("F1 Score:", round(f1_score(y_test, y_pred, average='weighted'), 2))

# Feature importance
importance = pd.Series(model.feature_importances_, index=X.columns)

fig = px.bar(
    importance.sort_values(ascending=False),
    title="Feature Importance"
)
st.plotly_chart(fig, use_container_width=True)

st.success("Top drivers help optimize marketing and feature prioritization.")
