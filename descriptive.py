import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Descriptive Analysis")

# Load data
df = pd.read_csv("muse_dataset.csv")

st.subheader("User Demographics & Behavior")

# Spending distribution
st.subheader("Monthly Spend Distribution")
fig1 = px.histogram(df, x="Monthly_Spend", nbins=30)
st.plotly_chart(fig1)

# Outfit budget
st.subheader("Outfit Budget Distribution")
fig2 = px.histogram(df, x="Outfit_Budget", nbins=30)
st.plotly_chart(fig2)

# Problems faced
st.subheader("Customer Problems")

problems = ['Struggle_Outfits','Body_Fit_Issue','Lack_Inspiration','Budget_Issue']
problem_counts = df[problems].sum()

fig3 = px.bar(problem_counts, title="Top Problems Faced")
st.plotly_chart(fig3)

# Adoption breakdown
st.subheader("Adoption Breakdown")
fig4 = px.pie(df, names="Adoption")
st.plotly_chart(fig4)
