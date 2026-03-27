import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_curve, auc

st.title("Prediction Models")
st.caption("Predicting user adoption using machine learning to guide growth strategy")

# Upload dataset
file = st.file_uploader("Upload CSV", key="pred")

if file:
    df = pd.read_csv(file)

    # --------------------------
    # DATA PREPROCESSING
    # --------------------------
    df = df.copy()

    le = LabelEncoder()
    for col in df.select_dtypes(include='object').columns:
        df[col] = le.fit_transform(df[col].astype(str))

    if "Adoption" not in df.columns:
        st.error("Dataset must contain 'Adoption' column")
    else:
        X = df.drop("Adoption", axis=1)
        y = df["Adoption"]

        # Train Test Split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        # Model
        model = RandomForestClassifier()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        y_prob = model.predict_proba(X_test)[:, 1]

        # --------------------------
        # 🔥 KPI METRICS
        # --------------------------
        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred)
        rec = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)

        st.subheader("Model Performance")

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Accuracy", f"{acc*100:.1f}%")
        col2.metric("Precision", f"{prec*100:.1f}%")
        col3.metric("Recall", f"{rec*100:.1f}%")
        col4.metric("F1 Score", f"{f1*100:.1f}%")

        # --------------------------
        # 🔥 ROC CURVE
        # --------------------------
        st.subheader("ROC Curve")

        fpr, tpr, _ = roc_curve(y_test, y_prob)
        roc_auc = auc(fpr, tpr)

        roc_df = pd.DataFrame({
            "False Positive Rate": fpr,
            "True Positive Rate": tpr
        })

        fig_roc = px.line(
            roc_df,
            x="False Positive Rate",
            y="True Positive Rate",
            title=f"ROC Curve (AUC = {roc_auc:.2f})"
        )

        st.plotly_chart(fig_roc, use_container_width=True)

        # --------------------------
        # 🔥 FEATURE IMPORTANCE
        # --------------------------
        st.subheader("Feature Importance")

        importance = model.feature_importances_
        feat_df = pd.DataFrame({
            "Feature": X.columns,
            "Importance": importance
        }).sort_values(by="Importance", ascending=True)

        fig_feat = px.bar(
            feat_df,
            x="Importance",
            y="Feature",
            orientation='h',
            title="Top Features Influencing Adoption"
        )

        st.plotly_chart(fig_feat, use_container_width=True)

        # --------------------------
        # 🔥 BUSINESS INSIGHT
        # --------------------------
        st.subheader("Key Insight")

        top_feature = feat_df.iloc[-1]["Feature"]

        st.success(f"""
Top driver of adoption: **{top_feature}**

👉 Users with strong signals in this feature are more likely to adopt the platform  
👉 Focus product and marketing strategies around this factor
""")

else:
    st.info("Upload a dataset to view prediction insights")
