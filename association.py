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

# Clean labels
rules['antecedents'] = rules['antecedents'].apply(lambda x: ', '.join(list(x)))
rules['consequents'] = rules['consequents'].apply(lambda x: ', '.join(list(x)))

rules = rules.sort_values(by='confidence', ascending=False)

# ---------------------------
# 🔥 1. BUSINESS FRIENDLY CHART
# ---------------------------
st.subheader("Most Common Customer Problems")

issue_counts = df_bin.sum().sort_values(ascending=False)

fig1 = px.bar(
    issue_counts,
    x=issue_counts.values,
    y=issue_counts.index,
    orientation='h',
    title="Top Pain Points Across Users",
    labels={"x": "Number of Users", "y": "Problem"}
)

st.plotly_chart(fig1, use_container_width=True)

# ---------------------------
# 🔥 2. ASSOCIATION INSIGHT (SIMPLIFIED)
# ---------------------------
st.subheader("Key Behavior Pattern")

top_rule = rules.iloc[0]

st.success(f"""
Users struggling with **{top_rule['antecedents']}**  
are very likely to ALSO face **{top_rule['consequents']}**

👉 Confidence: {round(top_rule['confidence']*100,1)}%

This shows users don’t face isolated issues —  
they experience **multiple styling problems together**
""")

# ---------------------------
# 🔥 3. VISUAL RELATION (BETTER CHART)
# ---------------------------
st.subheader("Problem Relationships")

top_rules = rules.head(6)

fig2 = px.scatter(
    top_rules,
    x="confidence",
    y="lift",
    size="support",
    color="antecedents",
    hover_data=["consequents"],
    title="Strength of Problem Combinations"
)

st.plotly_chart(fig2, use_container_width=True)

# ---------------------------
# 🔥 4. WHY THIS MATTERS
# ---------------------------
st.subheader("Why This Matters")

st.info("""
Users are not struggling with just one issue.

They face **clusters of problems**:
- Outfit confusion + lack of inspiration
- Fit issues + budget constraints

👉 This increases frustration and drop-offs
👉 Solving only one issue is not enough
""")

# ---------------------------
# 🔥 5. BUSINESS STRATEGY (IMPORTANT)
# ---------------------------
st.subheader("Recommended Product Strategy")

st.success("""
🚀 Build an AI Styling Assistant that:

- Combines outfit inspiration + body fit recommendations
- Suggests complete looks (not single items)
- Personalizes based on user preferences

💡 Positioning:
"From confusion to complete outfit — instantly"

🎯 Impact:
- Higher conversions
- Better user experience
- Strong differentiation vs competitors
""")

# ---------------------------
# OPTIONAL TABLE
# ---------------------------
with st.expander("See Detailed Rules"):
    st.dataframe(
        rules[['antecedents','consequents','confidence','lift']].head(10),
        use_container_width=True
    )
