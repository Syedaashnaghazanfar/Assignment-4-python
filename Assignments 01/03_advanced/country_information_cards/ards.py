import streamlit as st
import requests

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Country Info 🌍", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #57319e 0%, #2c2c54 100%);
        font-family: 'Segoe UI', sans-serif;
        color: #f0f0f0;
    }
    .info-card {
        background-color: rgba(255, 255, 255, 0.05);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        margin-top: 2rem;
        color: #ffffff;
    }
    .main-title {
        font-size: 3rem;
        color: #e0eaff;
        text-align: center;
        font-weight: bold;
        margin-top: 1rem;
    }
    .css-1d391kg, .css-1v0mbdj, .css-1r6slb0 {
        background-color: #24243e !important;
        color: #f1f1f1 !important;
    }
    </style>
""", unsafe_allow_html=True)


# ---- SIDEBAR ----
with st.sidebar:
    st.title("🧭 Country Explorer")
    selected = st.radio("Choose:", ["Home", "About"])
    st.markdown("---")
    st.info("🌐 Enter any country name and get its basic facts. Powered by the REST Countries API!")

# ---- TITLE ----
st.markdown('<div class="main-title">🌍 Country Info Dashboard</div>', unsafe_allow_html=True)

# ---- FUNCTIONS ----
def get_country_info(name):
    url = f"https://restcountries.com/v3.1/name/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[0]
    return None

# ---- MAIN SECTION ----
if selected == "Home":
    country = st.text_input("Enter Country Name 🗺️", "Pakistan")

    if st.button("Get Info"):
        if country:
            data = get_country_info(country)
            if data:
                st.image(data['flags']['png'], width=120)
                st.markdown('<div class="info-card">', unsafe_allow_html=True)
                st.subheader(f"📌 {data['name']['common']}")
                st.write(f"🌍 **Region**: {data.get('region', 'N/A')}")
                st.write(f"🏛️ **Capital**: {data.get('capital', ['N/A'])[0]}")
                st.write(f"👥 **Population**: {data.get('population', 'N/A'):,}")
                st.write(f"📏 **Area**: {data.get('area', 'N/A'):,} km²")
                st.write(f"🗣️ **Languages**: {', '.join(data.get('languages', {}).values())}")
                st.write(f"💱 **Currency**: {', '.join([cur['name'] for cur in data.get('currencies', {}).values()])}")
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.error("🚫 Country not found. Please try again.")
        else:
            st.warning("✍️ Type a country name to begin!")

elif selected == "About":
    st.header("About This App")
    st.markdown("""
    This is a sleek and simple app to explore country data ✨  
    Built with Python + Streamlit using the REST Countries API.  
    
    **Features:**
    - Flag, Capital, Population, Area, Currency, Languages
    - Dark-mode friendly UI
    - Sidebar with emoji nav 😎

    Happy exploring, fellow geographer 🌐
    """)
    st.markdown("---")
