import streamlit as st

# Set page config
st.set_page_config(
    page_title="BMI Calculator",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to:", ["Calculator", "About Us"])

# Gradient theme using CSS
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #ff9a9e, #fad0c4, #a18cd1, #fbc2eb, #84fab0);
        color: #333;
    }
    .stSidebar {
        background: linear-gradient(to bottom, #a1c4fd, #c2e9fb);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# About Us section
if selection == "About Us":
    st.header("About This BMI Calculator")
    st.write(
        "This BMI (Body Mass Index) Calculator helps you evaluate your body weight relative to height. "
        "Simply enter your height and weight, and it computes your BMI and indicates whether you fall under underweight, normal, overweight, or obese categories. "
        "Always consult a healthcare professional for medical advice."
    )

# Calculator page
else:
    st.header("BMI Calculator")
    st.write("Enter your details below:")

    # User inputs
    weight = st.number_input("Weight (kg)", min_value=1.0, max_value=300.0, value=70.0, step=0.1)
    height_cm = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=170.0, step=0.1)

    if st.button("Calculate BMI"):
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)
        bmi_rounded = round(bmi, 2)

        # BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        st.subheader(f"Your BMI is {bmi_rounded}")
        st.write(f"Category: **{category}**")
    
    st.write("\n---")
    st.write("Made with ❤️ using Streamlit.")