import streamlit as st
import requests


API_KEY = '38814d34b5912fa3ec491d6c866f24a0'

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        main_data = data['main']
        weather_data = data['weather'][0]

        return {
            'city_name': data['name'],
            'temperature': main_data['temp'],
            'humidity': main_data['humidity'],
            'description': weather_data['description'].capitalize(),
            'icon': f"http://openweathermap.org/img/wn/{weather_data['icon']}@2x.png"
        }
    else:
        return None


st.set_page_config(page_title="Weather App 🌤️", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1e1e2f 0%, #2c2c54 100%);
        font-family: 'Segoe UI', sans-serif;
        color: #f0f0f0;
    }
    .weather-card {
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
        background-color: #24243e !important; /* Sidebar background */
        color: #f1f1f1 !important;
    }
    .css-1cpxqw2, .css-ffhzg2, .css-1avcm0n {
        color: #ffffff !important; /* Sidebar text */
    }
    </style>
""", unsafe_allow_html=True)


with st.sidebar:
    st.title("🌍 Navigation")
    selected = st.radio("Go to:", ["Home", "About"])
    st.markdown("---")
    st.info("📖 This app gives you real-time weather info using OpenWeatherMap's API. Just type a city!")


st.markdown('<div class="main-title">☁️ Weather Forecast Dashboard</div>', unsafe_allow_html=True)


if selected == "Home":
    city = st.text_input("Enter City Name 🌆", "London")

    if st.button("Get Weather"):
        if city:
            weather_data = get_weather(city)
            if weather_data:
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.image(weather_data['icon'], width=100)
                with col2:
                    st.markdown('<div class="weather-card">', unsafe_allow_html=True)
                    st.subheader(f"📍 {weather_data['city_name']}")
                    st.write(f"🌡️ **Temperature**: {weather_data['temperature']}°C")
                    st.write(f"💧 **Humidity**: {weather_data['humidity']}%")
                    st.write(f"🌤️ **Description**: {weather_data['description']}")
                    
                    # Basic prediction
                    desc = weather_data['description'].lower()
                    if "rain" in desc:
                        st.warning("☔ Might be a rainy day—carry that umbrella!")
                    elif "clear" in desc:
                        st.success("🌞 Clear skies—perfect day to go outside!")
                    elif "cloud" in desc:
                        st.info("🌥️ Cloudy with a chance of... mood swings.")
                    else:
                        st.info("🔍 Skies are undecided today.")
                    st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.error("⚠️ City not found. Try another name.")
        else:
            st.warning("✏️ Please enter a city name!")

elif selected == "About":
    st.header("About This App")
    st.markdown("""
    This is a simple yet elegant weather dashboard built with ❤️ using Python and Streamlit.  
    It fetches real-time weather data and gives you a friendly breakdown including predictions based on the sky condition.
    
    **Features:**
    - Real-time weather info
    - Emoji-based feedback 😎
    - Clean & responsive layout
    - Fun little weather predictions

    Built for learners, dreamers, and Gen Z weather watchers 🌈
    """)
    st.markdown("---")