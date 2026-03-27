import streamlit as st
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import plotly.express as px

st.title("Association Rules (Customer Behavior Patterns)")

df = pd.read_csv("muse_dataset.csv")

# -------------------------------
# PREP DATA
# -------------------------------
binary_cols = ['Struggle_Outfits','Body_Fit_Issue','Lack_Inspiration','Budget_Issue']
df_bin = df[binary_cols]

# -------------------------------
# APPLY APRIORI
# -------------------------------
freq = apriori(df_bin, min_support=0.1, use_colnames=True)
rules = association_rules(freq, metric="confidence", min_threshold=0.5)

# -------------------------------
# CLEAN OUTPUT (REMOVE FROZENSET)
# -------------------------------
rules['antecedents'] = rules['antecedents'].apply(lambda x: ', '.join(list(x)))
rules['consequents'] = rules['consequents'].apply(lambda x: ', '.join(list(x)))

rules = rules.sort_values(by='confidence', ascending=False)

# -------------------------------
# SHOW TOP RULES (CLEAN TABLE)
# -------------------------------
st.subheader("Top Customer Behavior Patterns")

st.dataframe(
    rules[['antecedents','consequents','confidence','lift']].head(10),
    use_container_width=True
)

# -------------------------------
# VISUAL CHART (IMPORTANT)
# -------------------------------
st.subheader("Confidence vs Lift")

fig = px.scatter(
    rules,
    x="confidence",
    y="lift",
    size="support",
    color="confidence",
    hover_data=["antecedents", "consequents"],
    title="Association Rule Strength"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------------
# BUSINESS INSIGHT
# -------------------------------
st.subheader("Business Insight")

top_rule = rules.iloc[0]

st.success(f"""
Users who face **{top_rule['antecedents']}** are highly likely to also face **{top_rule['consequents']}**.

👉 This indicates strong demand for AI-based styling solutions that solve multiple problems together.
""")

# -------------------------------
# ACTIONABLE STRATEGY
# -------------------------------
st.subheader("Recommended Action")

st.info("""
• Bundle features: Outfit Generator + Inspiration Feed  
• Promote AI styling as solution to multiple problems  
• Target users facing multiple issues for higher conversion  
""")
