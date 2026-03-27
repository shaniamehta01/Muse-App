import streamlit as st

st.set_page_config(page_title="Muse AI App", layout="wide")

st.title("Muse AI Fashion Analytics App")

# Sidebar navigation
page = st.sidebar.radio("Go to", [
    "Executive Summary",
    "Descriptive Analysis",
    "Clustering",
    "Association Rules",
    "Prediction Models",
    "Prescriptive Actions",
    "New Customer Scorer"
])

if page == "Executive Summary":
    import descriptive
elif page == "Descriptive Analysis":
    import descriptive
elif page == "Clustering":
    import clustering
elif page == "Association Rules":
    import association
elif page == "Prediction Models":
    import prediction
elif page == "Prescriptive Actions":
    import prescriptive
elif page == "New Customer Scorer":
    import new_user
