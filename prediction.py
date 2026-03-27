
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_curve, auc
import plotly.express as px

st.title("Prediction Model")

file = st.file_uploader("Upload CSV", key="pred")

if file:
    df = pd.read_csv(file)

    le = LabelEncoder()
    for col in df.select_dtypes(include='object').columns:
        df[col] = le.fit_transform(df[col].astype(str))

    X = df.drop("Adoption", axis=1)
    y = df["Adoption"]

    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

    model = RandomForestClassifier()
    model.fit(X_train,y_train)

    y_pred = model.predict(X_test)

    st.write("Accuracy:", accuracy_score(y_test,y_pred))
    st.write("Precision:", precision_score(y_test,y_pred,average='weighted'))
    st.write("Recall:", recall_score(y_test,y_pred,average='weighted'))
    st.write("F1:", f1_score(y_test,y_pred,average='weighted'))

    if len(set(y))==2:
        y_prob = model.predict_proba(X_test)[:,1]
        fpr,tpr,_ = roc_curve(y_test,y_prob)
        fig = px.line(x=fpr,y=tpr,title="ROC Curve")
        st.plotly_chart(fig)

    importances = model.feature_importances_
    fig2 = px.bar(x=X.columns,y=importances,title="Feature Importance")
    st.plotly_chart(fig2)
