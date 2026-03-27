import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(layout="wide")
st.title("Executive Summary")

# Load data
df = pd.read_csv("muse_dataset.csv")

# ================= KPI CALCULATIONS =================
total_users = df.shape[0]
interested = df[df['Adoption'] == 'Yes'].shape[0]
conversion_rate = round((interested / total_users) * 100, 1)

avg_spend = int(df['Monthly_Spend'].mean())
revenue = int(avg_spend * interested)

# Clean label for issue
issue_map = {
    "Struggle_Outfits": "Outfit Confusion",
    "Body_Fit_Issue": "Fit Issues",
    "Lack_Inspiration": "Lack of Inspiration",
    "Budget_Issue": "Budget Constraints"
}

top_issue_raw = df[list(issue_map.keys())].sum().idxmax()
top_issue = issue_map[top_issue_raw]

# ================= KPI CARDS =================
st.markdown("### Key Business Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Interested Customers",
    f"{interested} / {total_users}",
    f"{conversion_rate}% conversion"
)

col2.metric(
    "Avg Monthly Spend",
    f"₹{avg_spend}"
)

col3.metric(
    "Total Revenue Potential",
    f"₹{revenue}"
)

col4.metric(
    "Top Customer Pain Point",
    top_issue
)

st.markdown("---")

# ================= CHARTS =================

st.markdown("### Customer Purchase Intent")

fig1 = px.bar(
    df['Adoption'].value_counts().reset_index(),
    x='index',
    y='Adoption',
    labels={'index': 'Adoption Category', 'Adoption': 'Users'},
    title="Purchase Likelihood Distribution"
)

st.plotly_chart(fig1, use_container_width=True)

# ================= SPENDING =================

st.markdown("### Spending Behavior")

fig2 = px.histogram(
    df,
    x="Monthly_Spend",
    nbins=30,
    title="Monthly Spend Distribution"
)

st.plotly_chart(fig2, use_container_width=True)

# ================= INSIGHT TEXT =================

st.markdown("### Key Insights")

st.success(f"""
• {conversion_rate}% of users show purchase intent  
• Major pain point: **{top_issue}**  
• Strong revenue potential of **₹{revenue}**  
• Indicates strong product-market fit for AI styling  
""")
