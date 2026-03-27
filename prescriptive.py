import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Prescriptive Strategy Dashboard")
st.caption("Turning customer insights into actionable business decisions")

df = pd.read_csv("muse_dataset.csv")

# --------------------------
# 🔥 1. PROBLEM DISTRIBUTION
# --------------------------
st.subheader("Customer Pain Point Analysis")

issues = ['Struggle_Outfits','Body_Fit_Issue','Lack_Inspiration','Budget_Issue']
issue_counts = df[issues].sum().sort_values(ascending=False)

fig = px.bar(
    x=issue_counts.index,
    y=issue_counts.values,
    title="Most Common Customer Problems",
    labels={'x':'Issue','y':'Number of Users'}
)

st.plotly_chart(fig, use_container_width=True)

# --------------------------
# 🔥 2. PRIORITY INSIGHT
# --------------------------
top_issue = issue_counts.idxmax()

st.subheader("Key Strategic Focus")

st.success(f"""
**Top Problem Identified:** {top_issue}

👉 This should be the primary focus for product and marketing efforts.
""")

# --------------------------
# 🔥 3. SEGMENTATION INSIGHT
# --------------------------
st.subheader("High-Value Customer Segment")

high_spenders = df[df['Monthly_Spend'] > df['Monthly_Spend'].mean()]

st.info(f"""
Users spending above average: {len(high_spenders)}

👉 Focus retention strategies on this segment
👉 Offer premium features & styling assistance
""")

# --------------------------
# 🔥 4. STRATEGIC ACTIONS
# --------------------------
st.subheader("Recommended Business Actions")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Product Strategy")
    st.write("• Build AI outfit recommendation engine")
    st.write("• Combine styling + inspiration + fit")
    st.write("• Personalize based on user behavior")

    st.markdown("### Pricing Strategy")
    st.write("• Introduce premium subscription")
    st.write("• Offer free trial for conversion")

with col2:
    st.markdown("### Marketing Strategy")
    st.write("• Target users facing styling issues")
    st.write("• Focus on Instagram & influencer campaigns")
    st.write("• Messaging: 'We solve outfit confusion instantly'")

    st.markdown("### Growth Strategy")
    st.write("• Retarget high-intent users")
    st.write("• Push personalized recommendations")

# --------------------------
# 🔥 5. FINAL IMPACT (THIS IS KEY)
# --------------------------
st.subheader("Expected Business Impact")

st.warning("""
📈 Increase conversion rate  
📈 Improve customer satisfaction  
📈 Boost average order value  
📈 Strengthen retention
""")
