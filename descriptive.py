
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Descriptive Analysis")

file = st.file_uploader("Upload CSV", key="desc")

if file:
    df = pd.read_csv(file)
    st.write(df.head())

    fig = px.histogram(df, x="Monthly_Spend")
    st.plotly_chart(fig)
