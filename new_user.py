
import streamlit as st
import pandas as pd

st.title("New User Scorer")

file = st.file_uploader("Upload New Users CSV")

if file:
    df = pd.read_csv(file)
    st.write(df.head())
    st.success("Scoring logic can be applied here")
