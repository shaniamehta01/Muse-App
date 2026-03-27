import streamlit as st

st.set_page_config(page_title="Muse AI App", layout="wide")

st.title("Muse AI Fashion Analytics App")

# Sidebar Navigation
page = st.sidebar.radio("Go to", [
    "Executive Summary",
    "Descriptive Analysis",
    "Clustering",
    "Association Rules",
    "Prediction Models",
    "Prescriptive Actions",
    "New Customer Scorer"
])

# Routing using exec (IMPORTANT FIX)
if page == "Executive Summary":
    exec(open("descriptive.py").read())

elif page == "Descriptive Analysis":
    exec(open("descriptive.py").read())

elif page == "Clustering":
    exec(open("clustering.py").read())

elif page == "Association Rules":
    exec(open("association.py").read())

elif page == "Prediction Models":
    exec(open("prediction.py").read())

elif page == "Prescriptive Actions":
    exec(open("prescriptive.py").read())

elif page == "New Customer Scorer":
    exec(open("new_user.py").read())
