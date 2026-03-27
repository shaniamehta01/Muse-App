import streamlit as st
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

st.title("Customer Behavior Insights")

df = pd.read_csv("muse_dataset.csv")

# -------------------------------
# PREP DATA
# -------------------------------
binary_cols = ['Struggle_Outfits','Body_Fit_Issue','Lack_Inspiration','Budget_Issue']
df_bin = df[binary_cols]

# Run Apriori
freq = apriori(df_bin, min_support=0.1, use_colnames=True)
rules = association_rules(freq, metric="confidence", min_threshold=0.5)

# Clean text
rules['antecedents'] = rules['antecedents'].apply(lambda x: ', '.join(list(x)))
rules['consequents'] = rules['consequents'].apply(lambda x: ', '.join(list(x)))

rules = rules.sort_values(by='confidence', ascending=False)

# -------------------------------
# 🔥 1. MAIN BUSINESS FINDING
# -------------------------------
st.subheader("🚨 What Are Users Struggling With?")

top_rule = rules.iloc[0]

st.markdown(f"""
### 👉 Most Important Insight

Users facing **{top_rule['antecedents']}**  
are highly likely to also face **{top_rule['consequents']}**

📊 Confidence: **{round(top_rule['confidence']*100,1)}%**
""")

st.markdown("---")

# -------------------------------
# 🔥 2. WHY IT MATTERS
# -------------------------------
st.subheader("💡 What This Means")

st.info("""
Users don’t face isolated problems — they experience multiple styling challenges together.

This means:
• Solving just one issue is not enough  
• Users expect complete styling assistance  
""")

# -------------------------------
# 🔥 3. PRODUCT DECISION
# -------------------------------
st.subheader("🚀 Product Strategy")

st.success("""
👉 Build an **AI Outfit Recommendation Engine**  
👉 Combine it with **Inspiration Feed**  
👉 Add **Body Fit + Occasion suggestions together**

Position Muse as:
👉 "Your complete personal stylist"
""")

# -------------------------------
# 🔥 4. MARKETING STRATEGY
# -------------------------------
st.subheader("📢 Marketing Strategy")

st.write("""
• Target users facing multiple issues  
• Use messaging like:  
  "Confused about outfits? We fix EVERYTHING."  
• Highlight transformation (before vs after styling)
""")

# -------------------------------
# 🔥 5. OPTIONAL (MINIMAL DATA VIEW)
# -------------------------------
with st.expander("See Supporting Data (Optional)"):
    st.dataframe(
        rules[['antecedents','consequents','confidence','lift']].head(5),
        use_container_width=True
    )
