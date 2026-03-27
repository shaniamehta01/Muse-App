import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# --------------------------
# PAGE HEADER
# --------------------------
st.title("Prediction Models")
st.caption("Predicting user adoption using machine learning to guide business decisions")

# --------------------------
# DATA (CLEAN BUSINESS FLOW)
# --------------------------
try:
    df = pd.read_csv("muse_dataset.csv")
    st.success("Analyzing behavior of 2,000 fashion users")
    st.caption("Model trained on user preferences, shopping patterns, and styling challenges")
except:
    st.error("Dataset not found")
    df = None

# --------------------------
# MODEL LOGIC
# --------------------------
if df is not None:

    df = df.copy()

    # Encode categorical columns
    le = LabelEncoder()
    for col in df.select_dtypes(include='object').columns:
        df[col] = le.fit_transform(df[col].astype(str))

    if "Adoption" not in df.columns:
        st.error("Dataset must contain 'Adoption' column")

    else:
        X = df.drop("Adoption", axis=1)
        y = df["Adoption"]

        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        # Model
        model = RandomForestClassifier(class_weight="balanced")
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        # --------------------------
        # METRICS
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

        st.markdown("---")

        # --------------------------
        # FEATURE IMPORTANCE
        # --------------------------
        st.subheader("What Drives User Adoption?")

        feat_df = pd.DataFrame({
            "Feature": X.columns,
            "Importance": model.feature_importances_
        }).sort_values(by="Importance", ascending=True)

        fig = px.bar(
            feat_df,
            x="Importance",
            y="Feature",
            orientation='h',
            title="Key Drivers of Adoption"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")

        # --------------------------
        # PREDICTION DISTRIBUTION
        # --------------------------
        st.subheader("Predicted User Behavior")

        pred_df = pd.DataFrame({"Predictions": y_pred})

        fig2 = px.histogram(
            pred_df,
            x="Predictions",
            title="How Users Are Likely to Respond"
        )

        st.plotly_chart(fig2, use_container_width=True)

        st.markdown("---")

        # --------------------------
        # BUSINESS INSIGHT
        # --------------------------
        st.subheader("Business Insight")

        top_feature = feat_df.iloc[-1]["Feature"]

        st.success(f"""
**Key Insight: {top_feature} is the strongest driver of adoption**

What this means:
- Users are highly influenced by this factor when deciding to adopt
- Improving this area will directly increase conversions
- This should be a priority in product strategy

Recommended Action:
- Optimize features related to {top_feature}
- Highlight this in marketing messaging
- Use this for personalization strategies
""")
