import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_curve, auc
import plotly.express as px

st.title("Prediction Model")

# LOAD DATA
df = pd.read_csv("muse_dataset.csv")

# Encode categorical
le = LabelEncoder()
for col in df.select_dtypes(include='object').columns:
    df[col] = le.fit_transform(df[col].astype(str))

# Split
X = df.drop("Adoption", axis=1)
y = df["Adoption"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Metrics
st.subheader("Model Performance")

st.write("Accuracy:", accuracy_score(y_test, y_pred))
st.write("Precision:", precision_score(y_test, y_pred, average='weighted'))
st.write("Recall:", recall_score(y_test, y_pred, average='weighted'))
st.write("F1 Score:", f1_score(y_test, y_pred, average='weighted'))

# ROC Curve (only if binary)
if len(set(y)) == 2:
    y_prob = model.predict_proba(X_test)[:,1]
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    fig = px.line(x=fpr, y=tpr, title="ROC Curve")
    st.plotly_chart(fig)

# Feature Importance
importance = pd.Series(model.feature_importances_, index=X.columns)
fig2 = px.bar(importance.sort_values(ascending=False), title="Feature Importance")
st.plotly_chart(fig2)
