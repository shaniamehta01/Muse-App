import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Executive Summary")

# Load dataset
df = pd.read_csv("muse_dataset.csv")

# -------------------------------
# 🔹 KPI METRICS
# -------------------------------
total_users = df.shape[0]
interested_users = df[df['Adoption'] == 'Yes'].shape[0]
avg_spend = int(df['Monthly_Spend'].mean())
total_revenue = int(df['Monthly_Spend'].sum())

# Top issue
issues = ['Struggle_Outfits', 'Body_Fit_Issue', 'Lack_Inspiration', 'Budget_Issue']
top_issue = df[issues].sum().idxmax()

# Display KPIs
col1, col2, col3, col4 = st.columns(4)

col1.metric("Interested Customers", f"{interested_users} / {total_users}")
col2.metric("Avg Monthly Spend", f"₹{avg_spend}")
col3.metric("Total Revenue Potential", f"₹{total_revenue}")
col4.metric("Top Customer Pain Point", top_issue)

st.markdown("---")

# -------------------------------
# 🔹 PURCHASE INTENT CHART (FIXED)
# -------------------------------
st.subheader("Customer Purchase Intent")

adoption_counts = df['Adoption'].value_counts().reset_index()
adoption_counts.columns = ['Adoption', 'Count']

fig1 = px.bar(
    adoption_counts,
    x='Adoption',
    y='Count',
    title="Purchase Likelihood Distribution",
    color='Adoption'
)

st.plotly_chart(fig1, use_container_width=True)

# -------------------------------
# 🔹 SPENDING DISTRIBUTION
# -------------------------------
st.subheader("Spending Distribution")

fig2 = px.histogram(
    df,
    x='Monthly_Spend',
    nbins=20,
    title="Monthly Spending Distribution"
)

st.plotly_chart(fig2, use_container_width=True)

# -------------------------------
# 🔹 QUICK INSIGHT
# -------------------------------
st.markdown("### Key Insight")

conversion_rate = round((interested_users / total_users) * 100, 1)

st.success(f"""
✔ {conversion_rate}% users are likely to adopt the app  
✔ Main problem users face: {top_issue}  
✔ Strong opportunity for AI-based styling solutions  
""")
