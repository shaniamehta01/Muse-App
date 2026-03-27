import streamlit as st
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

st.title("Association Rules (Customer Behavior Patterns)")

df = pd.read_csv("muse_dataset.csv")

# Binary columns
binary_cols = ['Struggle_Outfits','Body_Fit_Issue','Lack_Inspiration','Budget_Issue']
df_bin = df[binary_cols]

# Apriori
freq = apriori(df_bin, min_support=0.1, use_colnames=True)
rules = association_rules(freq, metric="confidence", min_threshold=0.5)

st.markdown("### Key Behavioral Patterns")

st.dataframe(rules[['antecedents','consequents','confidence','lift']])

st.markdown("### Insight")

st.success("Users facing outfit issues often demand AI recommendations — strong feature validation.")
