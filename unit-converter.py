import streamlit as st

# 🌈 Ultra-Vibrant Custom CSS
st.markdown("""
<style>
    .main-title {
        color: #FF2D00;
        font-size: 42px !important;
        font-weight: 900;
        text-align: center;
        text-shadow: 2px 2px 4px #FF9800;
        margin-bottom: 25px;
    }
    .subheader {
        color: #00B4FF;
        font-size: 24px !important;
        font-weight: 700;
        text-align: center;
        margin-bottom: 30px;
    }
    .conversion-box {
        background: linear-gradient(145deg, #F4F4F4, #FFFFFF);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
        margin-bottom: 25px;
        border-left: 6px solid #FF5722;
    }
    .stButton>button {
        background: linear-gradient(to right, #FF416C, #FF4B2B) !important;
        color: white !important;
        font-size: 18px !important;
        font-weight: 800 !important;
        padding: 12px 24px !important;
        border-radius: 50px !important;
        border: none !important;
        box-shadow: 0 4px 8px rgba(255,75,43,0.4) !important;
        width: 100%;
        transition: all 0.3s ease !important;
    }
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 12px rgba(255,75,43,0.6) !important;
    }
    .stSelectbox>div>div>select {
        font-size: 18px !important;
        font-weight: 600 !important;
        border: 3px solid #6200EA !important;
        border-radius: 10px !important;
        padding: 12px !important;
    }
    .stRadio>div {
        background: linear-gradient(135deg, #E3F2FD, #BBDEFB) !important;
        padding: 15px !important;
        border-radius: 15px !important;
        border-left: 5px solid #2196F3 !important;
    }
    .result-card {
        background: linear-gradient(to right, #4CAF50, #8BC34A) !important;
        color: white !important;
        font-size: 22px !important;
        font-weight: 700 !important;
        padding: 20px !important;
        border-radius: 12px !important;
        text-align: center !important;
        box-shadow: 0 6px 12px rgba(76,175,80,0.3) !important;
        margin-top: 20px !important;
    }
    .number-input {
        font-size: 20px !important;
        font-weight: 600 !important;
    }
</style>
""", unsafe_allow_html=True)

# Your original conversion functions (unchanged)
def length_converter(value, choice):
    if choice == "Kilometers to Miles":
        return f"🚀 {value} km = {value * 0.621371:.4f} miles"
    elif choice == "Miles to Kilometers":
        return f"🚀 {value} miles = {value * 1.60934:.4f} km"

def weight_converter(value, choice):
    if choice == "Kilograms to Pounds":
        return f"⚖️ {value} kg = {value * 2.20462:.4f} pounds"
    elif choice == "Pounds to Kilograms":
        return f"⚖️ {value} pounds = {value * 0.453592:.4f} kg"

def temperature_converter(value, choice):
    if choice == "Celsius to Fahrenheit":
        return f"🌡️ {value}°C = {(value * 9/5) + 32:.2f}°F"
    elif choice == "Fahrenheit to Celsius":
        return f"🌡️ {value}°F = {(value - 32) * 5/9:.2f}°C"

def main():
    # 🌟 Mega Header Section
    st.markdown('<p class="main-title">🔥 ULTIMATE UNIT CONVERTER 🔥</p>', unsafe_allow_html=True)
    st.markdown('<p class="subheader">UNIT UNIVERSE EXPLORER</p>', unsafe_allow_html=True)
    
    # Main conversion box
    with st.container():
        st.markdown('<div class="conversion-box">', unsafe_allow_html=True)
        
        option = st.selectbox(
            "SELECT CONVERSION TYPE", 
            ["Length Converter", "Weight Converter", "Temperature Converter"],
            key="main_select"
        )
        
        if option == "Length Converter":
            choice = st.radio(
                "LENGTH CONVERSION", 
                ["Kilometers to Miles", "Miles to Kilometers"],
                key="length_radio"
            )
            value = st.number_input(
                "ENTER VALUE", 
                min_value=0.0, 
                format="%.4f",
                key="length_input"
            )
            
        elif option == "Weight Converter":
            choice = st.radio(
                "WEIGHT CONVERSION", 
                ["Kilograms to Pounds", "Pounds to Kilograms"],
                key="weight_radio"
            )
            value = st.number_input(
                "ENTER VALUE", 
                min_value=0.0, 
                format="%.4f",
                key="weight_input"
            )
            
        elif option == "Temperature Converter":
            choice = st.radio(
                "TEMPERATURE CONVERSION", 
                ["Celsius to Fahrenheit", "Fahrenheit to Celsius"],
                key="temp_radio"
            )
            value = st.number_input(
                "ENTER VALUE", 
                format="%.2f",
                key="temp_input"
            )
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Convert button with mega style
    if st.button("⚡ CONVERT NOW ⚡", key="convert_button"):
        with st.spinner('⚙️ Crunching numbers...'):
            if option == "Length Converter":
                result = length_converter(value, choice)
            elif option == "Weight Converter":
                result = weight_converter(value, choice)
            else:
                result = temperature_converter(value, choice)
            
            # Display result with animated celebration
            st.markdown(f'<div class="result-card">{result}</div>', unsafe_allow_html=True)
            st.balloons()
            st.success("✅ Conversion successful!")

if __name__ == "__main__":
    main()