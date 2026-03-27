import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_curve, auc

st.title("Prediction Models")
st.caption("Predicting user adoption using machine learning to guide growth strategy")

# --------------------------
# 🔥 USE DEFAULT DATASET FIRST
# --------------------------
try:
    df = pd.read_csv("muse_dataset.csv")
    st.success("Using default dataset")
except:
    df = None

# Optional upload (override)
file = st.file_uploader("Upload your dataset (optional)")

if file:
    df = pd.read_csv(file)
    st.success("Custom dataset loaded")

# --------------------------
# IF NO DATA
# --------------------------
if df is None:
    st.error("No dataset found. Please upload one.")
else:

    df = df.copy()

    # Encode categorical
    le = LabelEncoder()
    for col in df.select_dtypes(include='object').columns:
        df[col] = le.fit_transform(df[col].astype(str))

    if "Adoption" not in df.columns:
        st.error("Dataset must contain 'Adoption' column")

    else:
        X = df.drop("Adoption", axis=1)
        y = df["Adoption"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        model = RandomForestClassifier()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        y_prob = model.predict_proba(X_test)[:, 1]

        # --------------------------
        # 🔥 METRICS
        # --------------------------
        st.subheader("Model Performance")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Accuracy", f"{accuracy_score(y_test, y_pred)*100:.1f}%")
        col2.metric("Precision", f"{precision_score(y_test, y_pred)*100:.1f}%")
        col3.metric("Recall", f"{recall_score(y_test, y_pred)*100:.1f}%")
        col4.metric("F1 Score", f"{f1_score(y_test, y_pred)*100:.1f}%")

        # --------------------------
        # 🔥 ROC CURVE
        # --------------------------
        st.subheader("ROC Curve")

        fpr, tpr, _ = roc_curve(y_test, y_prob)
        roc_auc = auc(fpr, tpr)

        fig = px.line(
            x=fpr,
            y=tpr,
            title=f"ROC Curve (AUC = {roc_auc:.2f})"
        )

        fig.add_shape(
            type='line',
            line=dict(dash='dash'),
            x0=0, x1=1, y0=0, y1=1
        )

        st.plotly_chart(fig, use_container_width=True)

        # --------------------------
        # 🔥 FEATURE IMPORTANCE
        # --------------------------
        st.subheader("Feature Importance")

        feat_df = pd.DataFrame({
            "Feature": X.columns,
            "Importance": model.feature_importances_
        }).sort_values(by="Importance", ascending=True)

        fig2 = px.bar(
            feat_df,
            x="Importance",
            y="Feature",
            orientation='h'
        )

        st.plotly_chart(fig2, use_container_width=True)

        # --------------------------
        # 🔥 INSIGHT
        # --------------------------
        st.subheader("Key Insight")

        top_feature = feat_df.iloc[-1]["Feature"]

        st.success(f"""
Top driver of adoption: **{top_feature}**

👉 Users influenced by this factor are most likely to adopt  
👉 Focus product and marketing around this behavior
""")
