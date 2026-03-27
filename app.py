import streamlit as st

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(page_title="Muse AI App", layout="wide")

# ---------------------------
# 🎨 PURPLE THEME
# ---------------------------
st.markdown("""
<style>
.stApp {
    background-color: #f9f6ff;
}

section[data-testid="stSidebar"] {
    background-color: #f3ecff;
}

h1, h2, h3 {
    color: #6a0dad;
}

.stButton>button {
    background-color: #6a0dad;
    color: white;
    border-radius: 8px;
}

[data-testid="stMetricValue"] {
    color: #6a0dad;
}

.stSuccess {
    background-color: #ede4ff;
    color: #4b0082;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# TITLE + TAGLINE
# ---------------------------
st.title("Muse AI Fashion Analytics App")
st.sidebar.image("Muse.png", width=120)
st.markdown("### Turning fashion confusion into confident decisions")

# ---------------------------
# SIDEBAR NAVIGATION
# ---------------------------
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

# ---------------------------
# HOME PAGE (NEW 🔥)
# ---------------------------
if page == "Home":
    st.header("Welcome to Muse AI")

    st.write("""
Choosing outfits is not as simple as it seems. Even with countless options, users often feel confused due to lack of inspiration, fit concerns, and multiple overlapping issues.

This leads to hesitation, decision fatigue, and lower conversions.
""")

    st.subheader("What This App Does")

    st.write("""
This application uses data analytics and machine learning to:

- Identify key customer pain points  
- Understand behavior patterns  
- Predict user decisions  
- Recommend business strategies  
""")

    st.subheader("What's Inside")

    st.write("""
- **Executive Summary** → Key business metrics  
- **Descriptive Analysis** → What users are facing  
- **Clustering** → User segmentation  
- **Association Rules** → Behavior patterns  
- **Prediction Models** → Likelihood of action  
- **Prescriptive Actions** → Strategic recommendations  
- **New Customer Scorer** → Evaluate new users  
""")

    st.success("Goal: Move from product-based selling to solution-driven fashion experiences.")

# ---------------------------
# ROUTING (KEEP SAME)
# ---------------------------
elif page == "Executive Summary":
    exec(open("executive.py").read())

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
