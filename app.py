import streamlit as st
import requests

# Set up the API endpoint and headers
url = "https://api.neuralseek.com/v1/crn%3Av1%3Abluemix%3Apublic%3Aneuralseek%3Aus-south%3Aa%2F3d921d6e5e204570a252619c28d03770%3A74ef5ca7-03d9-4b62-b3e9-7fe92d57b60b%3A%3A/seek"
headers = {
    "accept": "application/json",
    "apikey": "0635bf09-28e77037-673a0b92-1494764a",
    "Content-Type": "application/json"
}

# Streamlit app
st.title("NeuralSeek Query")
question = st.text_input("Enter your question:")

if st.button("Submit"):
    # Create the request payload
    payload = {
        "question": question,
        "user_session": {
            "metadata": {"user_id": ""},
            "system": {"session_id": ""}
        },
        "params": [],
        "options": {}
    }
    
    # Make the API request
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        # Extract and display only the answer
        answer = response.json().get("answer", "No answer found.")
        st.write("Answer:", answer)
    else:
        st.write("Failed to retrieve answer:", response.status_code)
