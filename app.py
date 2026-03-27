import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Muse AI", layout="wide")

# ---------------- PURPLE THEME ----------------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #f5f0ff, #ffffff);
    }

    section[data-testid="stSidebar"] {
        background-color: #ede7ff;
    }

    h1, h2, h3 {
        color: #4b2e83;
    }

    .stButton>button {
        background-color: #7b5cff;
        color: white;
        border-radius: 8px;
        border: none;
    }

    .block-container {
        padding-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER WITH LOGO ----------------
col1, col2 = st.columns([8,1])

with col1:
    st.title("Muse AI Fashion Analytics App")

with col2:
    st.image("Muse.png", width=80)

# ---------------- SIDEBAR ----------------
st.sidebar.image("Muse.png", width=120)

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

# ---------------- HOME ----------------
if page == "Home":

    st.markdown("## Welcome to Muse AI")

    st.write("""
Finding the perfect outfit shouldn’t feel confusing. But in reality, most users struggle with multiple challenges — 
what to wear, how it fits, and whether it suits the occasion.

Muse AI is designed as a smart fashion assistant that understands these problems and helps users make better styling decisions.
    """)

    st.markdown("### What Muse AI helps you do:")

    col1, col2 = st.columns(2)

    with col1:
        st.write("👗 Discover outfit ideas based on your style")
        st.write("✨ Get recommendations when you're unsure what to wear")

    with col2:
        st.write("🧠 Solve fit, budget & styling confusion together")
        st.write("📈 Improve decision-making with AI-driven insights")

# ---------------- ROUTING ----------------
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
