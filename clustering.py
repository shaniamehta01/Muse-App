import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
import plotly.express as px

st.title("Clustering")

# LOAD DATA
df = pd.read_csv("muse_dataset.csv")

# Encode
df_enc = df.copy()
le = LabelEncoder()

for col in df_enc.select_dtypes(include='object').columns:
    df_enc[col] = le.fit_transform(df_enc[col].astype(str))

# KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
df_enc['Cluster'] = kmeans.fit_predict(df_enc)

# Plot
fig = px.scatter(df_enc, x="Monthly_Spend", y="Outfit_Budget", color="Cluster")
st.plotly_chart(fig)
