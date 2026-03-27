import streamlit as st
import pandas as pd

st.title("Executive Summary")

file = st.file_uploader("Upload Dataset")

if file:
    df = pd.read_csv(file)

    # Basic metrics
    total_users = df.shape[0]
    interested = df[df['Adoption'] == 'Yes'].shape[0]
    avg_spend = int(df['Monthly_Spend'].mean())

    # Top barrier (example using most common issue)
    top_issue = df[['Struggle_Outfits','Body_Fit_Issue','Lack_Inspiration','Budget_Issue']].sum().idxmax()

    # Layout
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Interested Users", f"{interested} / {total_users}")
    col2.metric("Avg Monthly Spend", f"₹{avg_spend}")
    col3.metric("Total Users", total_users)
    col4.metric("Top Issue", top_issue)

    st.markdown("---")

    st.subheader("Adoption Distribution")
    st.bar_chart(df['Adoption'].value_counts())

    st.subheader("Spending Distribution")
    st.bar_chart(df['Monthly_Spend'])
