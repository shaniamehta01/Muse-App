import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
st.title("Prescriptive Strategy")

df = pd.read_csv("muse_dataset.csv")

# Key insights
issues = ['Struggle_Outfits','Body_Fit_Issue','Lack_Inspiration','Budget_Issue']
top_issue = df[issues].sum().idxmax()

avg_spend = df['Monthly_Spend'].mean()

st.markdown("### Strategic Recommendations")

if top_issue == "Struggle_Outfits":
    st.success("👉 Prioritize AI outfit recommendation engine")

elif top_issue == "Lack_Inspiration":
    st.success("👉 Build personalized inspiration feed")

elif top_issue == "Body_Fit_Issue":
    st.success("👉 Improve virtual try-on experience")

elif top_issue == "Budget_Issue":
    st.success("👉 Introduce budget-based styling")

st.markdown("### Pricing Strategy")

if avg_spend > 3000:
    st.write("👉 Introduce premium subscription tier")
else:
    st.write("👉 Focus on freemium model to drive adoption")

st.markdown("### Marketing Strategy")

st.write("👉 Target high-intent users")
st.write("👉 Use influencer + Instagram marketing")
st.write("👉 Offer free trial for conversion boost")
