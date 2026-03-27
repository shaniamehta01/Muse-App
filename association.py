import streamlit as st
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

st.title("Association Rules")

df = pd.read_csv("muse_dataset.csv")

binary_cols = [col for col in df.columns if df[col].nunique()==2]

df_bin = df[binary_cols]

freq = apriori(df_bin, min_support=0.1, use_colnames=True)
rules = association_rules(freq, metric="confidence", min_threshold=0.5)

st.write(rules[['antecedents','consequents','confidence','lift']])
