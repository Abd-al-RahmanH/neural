import streamlit as st
import requests

# NeuralSeek Webhook Details
API_URL = "https://api.neuralseek.com/v1/crn%3Av1%3Abluemix%3Apublic%3Aneuralseek%3Aus-south%3Aa%2F3d921d6e5e204570a252619c28d03770%3A74ef5ca7-03d9-4b62-b3e9-7fe92d57b60b%3A%3A/seek"  # Replace with your actual Webhook URL
API_KEY = "0635bf09-28e77037-673a0b92-1494764a"  # Replace with your actual API Key

# Streamlit UI
st.title("NeuralSeek Chat Interface")
st.write("Ask NeuralSeek a question and get a response from your knowledge base.")

# User input for the query
user_input = st.text_input("Type your question here:")

if st.button("Submit"):
    if user_input.strip():
        # Define the payload and headers
        payload = {
            "userId": "streamlit_user",  # Customize the user ID if needed
            "message": user_input.strip()  # Strip extra spaces
        }
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        try:
            # Make a request to NeuralSeek Webhook
            response = requests.post(API_URL, json=payload, headers=headers)

            # Check if the request was successful
            if response.status_code == 200:
                result = response.json()
                st.success("NeuralSeek Response:")
                st.write(result.get("answer", "No answer available"))
            else:
                st.error(f"Failed to get a response from NeuralSeek. Status code: {response.status_code}")
                st.write("Response content:", response.text)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.error("Please enter a valid question.")
