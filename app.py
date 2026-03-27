import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Muse AI", layout="wide")

# ---------------- TITLE ----------------
st.title("Muse AI Fashion Analytics App")

# ---------------- SIDEBAR LOGO ----------------
st.sidebar.image("Muse.png", width=120)

# ---------------- SIDEBAR NAVIGATION ----------------
page = st.sidebar.radio("Go to", [
    "Home",
    "Executive Summary",
    "Descriptive Analysis",
    "Clustering",
    "Association Rules",
    "Prediction Models",
    "Prescriptive Actions",
    "New Customer Scorer"
])

# ---------------- ROUTING ----------------

# -------- HOME PAGE --------
if page == "Home":

    col1, col2 = st.columns([1, 4])

    with col1:
        st.image("Muse.png", width=120)

    with col2:
        st.markdown("## Welcome to Muse AI")

    st.write("""
Choosing outfits is not as simple as it seems. Even with endless options, users still struggle with decisions. 
Lack of inspiration, fit concerns, and multiple overlapping issues often make the experience frustrating.

Muse AI uses data-driven insights to understand these behaviors and help improve fashion decision-making.
    """)

    st.markdown("### What this app does:")

    st.markdown("""
- 📊 Analyzes customer behavior  
- 🧠 Identifies key fashion pain points  
- 🔮 Predicts purchase likelihood  
- 🚀 Suggests business strategies  
    """)

# -------- EXECUTIVE SUMMARY --------
elif page == "Executive Summary":
    exec(open("executive.py").read())

# -------- DESCRIPTIVE --------
elif page == "Descriptive Analysis":
    exec(open("descriptive.py").read())

# -------- CLUSTERING --------
elif page == "Clustering":
    exec(open("clustering.py").read())

# -------- ASSOCIATION --------
elif page == "Association Rules":
    exec(open("association.py").read())

# -------- PREDICTION --------
elif page == "Prediction Models":
    exec(open("prediction.py").read())

# -------- PRESCRIPTIVE --------
elif page == "Prescriptive Actions":
    exec(open("prescriptive.py").read())

# -------- NEW USER --------
elif page == "New Customer Scorer":
    exec(open("new_user.py").read())
