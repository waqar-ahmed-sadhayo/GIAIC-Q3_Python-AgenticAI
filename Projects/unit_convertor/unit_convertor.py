import streamlit as st


def convert_units(value, unit_from, unit_to):

    conversions = {
        'meter_kilometer': 0.001,
        'kilometer_meter': 1000,
        'gram_kilogram': 0.001,
        'kilogram_gram': 1000
    }

    key = f"{unit_from}_{unit_to}"

    if key in conversions:
        conversion  = conversions[key]
        return value * conversion
    else:
        return "Conversion not supported"


st.set_page_config(page_title="📏🔁 Unit Converter", layout="wide")
st.title("📏🔁 Unit Converter")

value = st.number_input("Enter the number:")

unit_from = st.selectbox("Convert from:", ['meter', 'kilometer', 'gram', 'kilogram'])

unit_to = st.selectbox("Convert to:", ['meter', 'kilometer', 'gram', 'kilogram'])

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Converted value: {result}")