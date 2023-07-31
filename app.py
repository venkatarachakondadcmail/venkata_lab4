
import streamlit as st
import requests

# Streamlit app title and description
st.title("Fish Weight Prediction using Flask API")
st.write("Enter fish features and get the predicted weight.")

# Form to input fish features
length_ver = st.number_input("LengthVer", value=20.0)
length_dia = st.number_input("LengthDia", value=15.0)
length_cro = st.number_input("LengthCro", value=25.0)
height = st.number_input("Height", value=5.0)
width = st.number_input("Width", value=3.0)

# Predict button
if st.button("Predict Weight"):
    data = {
        'LengthVer': length_ver,
        'LengthDia': length_dia,
        'LengthCro': length_cro,
        'Height': height,
        'Width': width
    }

    # Make a POST request to the Flask API
    api_url = 'http://0.0.0.0:8000/predict'
    response = requests.post(api_url, json=data)

    if response.status_code == 200:
        prediction = response.json().get('predicted_weight', None)
        if prediction is not None:
            st.success(f"Predicted Weight: {prediction:.2f} grams")
        else:
            st.error("Failed to get a valid prediction.")
    else:
        st.error("Error occurred during prediction. Please try again.")
