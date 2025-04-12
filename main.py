import streamlit as st

def convert_units(category, value, from_unit, to_unit):
    conversions = {
        "Length": {
            "Meter": 1,
            "Kilometer": 0.001,
            "Centimeter": 100,
            "Millimeter": 1000,
            "Mile": 0.000621371,
            "Yard": 1.09361,
            "Foot": 3.28084,
            "Inch": 39.3701
        },
        "Weight": {
            "Kilogram": 1,
            "Gram": 1000,
            "Milligram": 1e6,
            "Pound": 2.20462,
            "Ounce": 35.274
        },
        "Temperature": "temperature"
    }
    
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value
    
    else:
        return value * (conversions[category][to_unit] / conversions[category][from_unit])

st.title("Unit Converter")
st.write("Convert Length, Weight, and Temperature easily!")

category = st.selectbox("Select a category", ["Length", "Weight", "Temperature"])

units = {
    "Length": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"],
    "Weight": ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

from_unit = st.selectbox("From Unit", units[category])
to_unit = st.selectbox("To Unit", units[category])
value = st.number_input("Enter Value", min_value=0.0, format="%.6f")

if st.button("Convert"):
    result = convert_units(category, value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.6f} {to_unit}")