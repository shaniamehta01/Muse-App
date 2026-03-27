import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
import plotly.express as px

st.title("Customer Segmentation (Clustering)")

df = pd.read_csv("muse_dataset.csv")

# Encode
df_enc = df.copy()
le = LabelEncoder()

for col in df_enc.select_dtypes(include='object').columns:
    df_enc[col] = le.fit_transform(df_enc[col].astype(str))

# KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
df_enc['Cluster'] = kmeans.fit_predict(df_enc)

# Map cluster names
cluster_map = {
    0: "Budget Users",
    1: "Mid-Range Users",
    2: "High-Value Users"
}
df_enc['Segment'] = df_enc['Cluster'].map(cluster_map)

# Plot
fig = px.scatter(
    df_enc,
    x="Monthly_Spend",
    y="Outfit_Budget",
    color="Segment",
    title="Customer Segments"
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("### Segment Insights")

for seg in df_enc['Segment'].unique():
    count = df_enc[df_enc['Segment'] == seg].shape[0]
    st.write(f"• {seg}: {count} users")
