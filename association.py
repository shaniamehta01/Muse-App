import streamlit as st
import pandas as pd
import plotly.express as px
from mlxtend.frequent_patterns import apriori, association_rules

st.title("Customer Behavior Insights")

df = pd.read_csv("muse_dataset.csv")

# ---------------------------
# PREP DATA
# ---------------------------
binary_cols = ['Struggle_Outfits','Body_Fit_Issue','Lack_Inspiration','Budget_Issue']
df_bin = df[binary_cols]

freq = apriori(df_bin, min_support=0.1, use_colnames=True)
rules = association_rules(freq, metric="confidence", min_threshold=0.5)

rules['antecedents'] = rules['antecedents'].apply(lambda x: ', '.join(list(x)))
rules['consequents'] = rules['consequents'].apply(lambda x: ', '.join(list(x)))

rules = rules.sort_values(by='confidence', ascending=False)

# ---------------------------
# 🔥 1. CHART (MOST IMPORTANT)
# ---------------------------
st.subheader("Top Customer Behavior Patterns")

top_rules = rules.head(8)

fig = px.bar(
    top_rules,
    x="confidence",
    y="antecedents",
    color="consequents",
    orientation='h',
    title="Top Problem Combinations Driving Customer Issues"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------
# 🔥 2. INSIGHT CARD
# ---------------------------
top_rule = rules.iloc[0]

st.markdown("### Key Insight")

st.success(f"""
Users facing **{top_rule['antecedents']}**  
are highly likely to also face **{top_rule['consequents']}**

👉 Confidence: {round(top_rule['confidence']*100,1)}%
""")

# ---------------------------
# 🔥 3. BUSINESS IMPACT
# ---------------------------
st.subheader("Why This Matters")

col1, col2 = st.columns(2)

with col1:
    st.info("""
    Customers face multiple issues together  
    → Not single problem solving
    """)

with col2:
    st.info("""
    Higher frustration → Higher drop-off risk  
    → Opportunity for AI styling
    """)

# ---------------------------
# 🔥 4. ACTION (THIS IS WHAT PROF CARES ABOUT)
# ---------------------------
st.subheader("Recommended Action")

st.markdown("""
**Product:**
- AI outfit recommendation engine
- Combine inspiration + fit + occasion

**Marketing:**
- "Confused about outfits? We solve everything."
- Focus on multi-problem users

**Business Goal:**
- Increase conversion
- Improve user satisfaction
""")

# ---------------------------
# OPTIONAL CLEAN TABLE
# ---------------------------
with st.expander("See Detailed Rules"):
    st.dataframe(
        rules[['antecedents','consequents','confidence','lift']].head(10),
        use_container_width=True
    )
