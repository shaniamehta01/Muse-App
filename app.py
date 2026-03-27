import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Muse AI", layout="wide")

# ---------------- PURPLE THEME ----------------
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #f5f0ff, #ffffff);
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #ede7ff;
    }

    /* Titles */
    h1, h2, h3 {
        color: #4b2e83;
    }

    /* Buttons */
    .stButton>button {
        background-color: #7b5cff;
        color: white;
        border-radius: 8px;
        border: none;
    }

    /* Highlight box */
    .block-container {
        padding-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- TOP RIGHT LOGO ----------------
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
