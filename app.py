import streamlit as st
import requests

# NeuralSeek Webhook Details
API_URL = "https://api.neuralseek.com/v1/crn%3Av1%3Abluemix%3Apublic%3Aneuralseek%3Aus-south%3Aa%2F3d921d6e5e204570a252619c28d03770%3A74ef5ca7-03d9-4b62-b3e9-7fe92d57b60b%3A%3A/seek"  # Replace with your URL from the Webhook page
API_KEY = "0635bf09-28e77037-673a0b92-1494764a"  # Replace with your API Key

# Streamlit UI
st.title("NeuralSeek Chat Interface")
user_input = st.text_input("Ask NeuralSeek:")

if st.button("Submit"):
    # Define the payload and headers
    payload = {
        "userId": "streamlit_user",  # You can customize this
        "message": user_input
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # Make a request to NeuralSeek Webhook
    response = requests.post(API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        result = response.json()
        st.write("NeuralSeek Response:", result.get("answer", "No answer available"))
    else:
        st.error("Failed to get a response from NeuralSeek")
