import streamlit as st
import pandas as pd

st.title("Executive Summary")

# AUTO LOAD DATA (NO UPLOAD NEEDED)
df = pd.read_csv("muse_dataset.csv")

# Metrics
total_users = df.shape[0]
interested = df[df['Adoption'] == 'Yes'].shape[0]
avg_spend = int(df['Monthly_Spend'].mean())

# Revenue estimate (like sir)
revenue = int(avg_spend * interested)

# Top issue
top_issue = df[['Struggle_Outfits','Body_Fit_Issue','Lack_Inspiration','Budget_Issue']].sum().idxmax()

# Layout
col1, col2, col3, col4 = st.columns(4)

col1.metric("Interested Customers", f"{interested} / {total_users}")
col2.metric("Avg Spend", f"₹{avg_spend}")
col3.metric("Total Revenue", f"₹{revenue}")
col4.metric("Top Issue", top_issue)

st.markdown("---")

# Charts
st.subheader("Purchase Likelihood Distribution")
st.bar_chart(df['Adoption'].value_counts())

st.subheader("Spending Distribution")
st.bar_chart(df['Monthly_Spend'])
