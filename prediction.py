import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

st.title("Prediction Models")
st.caption("Predicting user adoption using machine learning")

# --------------------------
# LOAD DATA
# --------------------------
try:
    df = pd.read_csv("muse_dataset.csv")
    st.success("Using default dataset")
except:
    df = None

file = st.file_uploader("Upload your dataset (optional)")

if file:
    df = pd.read_csv(file)
    st.success("Custom dataset loaded")

if df is None:
    st.error("No dataset found")
else:
    df = df.copy()

    # --------------------------
    # ENCODE DATA
    # --------------------------
    le = LabelEncoder()
    for col in df.select_dtypes(include='object').columns:
        df[col] = le.fit_transform(df[col].astype(str))

    if "Adoption" not in df.columns:
        st.error("Dataset must contain 'Adoption'")
    else:
        X = df.drop("Adoption", axis=1)
        y = df["Adoption"]

        # --------------------------
        # TRAIN MODEL
        # --------------------------
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        model = RandomForestClassifier(class_weight="balanced")
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        # --------------------------
        # FIXED METRICS (MULTI-CLASS SAFE)
        # --------------------------
        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred, average='weighted', zero_division=0)
        rec = recall_score(y_test, y_pred, average='weighted', zero_division=0)
        f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)

        st.subheader("Model Performance")

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Accuracy", f"{acc*100:.1f}%")
        col2.metric("Precision", f"{prec*100:.1f}%")
        col3.metric("Recall", f"{rec*100:.1f}%")
        col4.metric("F1 Score", f"{f1*100:.1f}%")

        # --------------------------
        # FEATURE IMPORTANCE
        # --------------------------
        st.subheader("Feature Importance")

        feat_df = pd.DataFrame({
            "Feature": X.columns,
            "Importance": model.feature_importances_
        }).sort_values(by="Importance", ascending=True)

        fig = px.bar(
            feat_df,
            x="Importance",
            y="Feature",
            orientation='h',
            title="Top Drivers of Adoption"
        )

        st.plotly_chart(fig, use_container_width=True)

        # --------------------------
        # PREDICTION DISTRIBUTION
        # --------------------------
        st.subheader("Prediction Distribution")

        pred_df = pd.DataFrame({"Predictions": y_pred})
        fig2 = px.histogram(pred_df, x="Predictions")

        st.plotly_chart(fig2, use_container_width=True)

        # --------------------------
        # INSIGHT
        # --------------------------
        st.subheader("Business Insight")

        top_feature = feat_df.iloc[-1]["Feature"]

        st.success(f"""
Top driver of adoption: **{top_feature}**

👉 Focus product improvements around this  
👉 This feature strongly influences user decisions  
""")
