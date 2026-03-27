import streamlit as st
import pandas as pd

st.title("Prescriptive Actions")

# Load data
df = pd.read_csv("muse_dataset.csv")

st.subheader("Key Business Insights")

# Top issue
issues = ['Struggle_Outfits','Body_Fit_Issue','Lack_Inspiration','Budget_Issue']
top_issue = df[issues].sum().idxmax()

# High value users
high_spend = df[df['Monthly_Spend'] > df['Monthly_Spend'].mean()]

# Interested users
interested = df[df['Adoption'] == 'Yes']

# Display insights
st.write(f"🔴 Top Customer Problem: {top_issue}")
st.write(f"💰 High Value Customers: {len(high_spend)} users")
st.write(f"🔥 Interested Users: {len(interested)} users")

st.markdown("---")

st.subheader("Recommended Actions")

# Prescriptive logic
if top_issue == "Struggle_Outfits":
    st.success("👉 Focus on AI Outfit Recommendation Feature")

elif top_issue == "Lack_Inspiration":
    st.success("👉 Build Instagram-like Inspiration Feed")

elif top_issue == "Body_Fit_Issue":
    st.success("👉 Improve Virtual Try-On & Body Fit AI")

elif top_issue == "Budget_Issue":
    st.success("👉 Introduce Budget-Based Styling Suggestions")

st.markdown("---")

st.subheader("Marketing Strategy")

if len(high_spend) > len(df)*0.3:
    st.write("👉 Target premium users with subscription plans")

if len(interested) > len(df)*0.5:
    st.write("👉 Strong product-market fit — invest in growth marketing")

else:
    st.write("👉 Improve product before scaling marketing")

st.markdown("---")

st.subheader("Launch Strategy")

st.write("👉 Start with high-intent users (Interested segment)")
st.write("👉 Offer free trial for conversion boost")
st.write("👉 Use influencer + Instagram marketing")
