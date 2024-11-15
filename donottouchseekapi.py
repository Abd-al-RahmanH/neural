import streamlit as st
import requests
import json

# Define the API endpoint and headers
API_URL = "https://api.neuralseek.com/v1/crn%3Av1%3Abluemix%3Apublic%3Aneuralseek%3Aus-south%3Aa%2F3d921d6e5e204570a252619c28d03770%3A74ef5ca7-03d9-4b62-b3e9-7fe92d57b60b%3A%3A/seek"
API_KEY = "0635bf09-28e77037-673a0b92-1494764a"
HEADERS = {
    "accept": "application/json",
    "apikey": API_KEY,
    "Content-Type": "application/json"
}

# Streamlit app layout
st.title("NeuralSeek API Query")
st.write("Authenticate and query the NeuralSeek API.")

# Input fields for the query
question = st.text_input("Enter your question:")
user_id = st.text_input("User ID (optional):")
session_id = st.text_input("Session ID (optional):")

if st.button("Submit Query"):
    # Payload for the request
    payload = {
        "question": question,
        "user_session": {
            "metadata": {"user_id": user_id},
            "system": {"session_id": session_id}
        },
        "params": [{"name": "", "value": ""}],
        "options": {
            "personalize": {
                "preferredName": "",
                "noWelcome": "",
                "forceFirstPerson": "",
                "products": ["string"],
                "additionalDetails": ""
            },
            "proposalID": "",
            "streaming": False,
            "seekLLM": "",
            "language": "",
            "filter": "",
            "lastTurn": [{"input": "", "response": ""}],
            "promptEngineering": "",
            "promptEngineeringPhrase": "",
            "answerLength": 4,
            "url": "",
            "stump": "",
            "includeSourceResults": False,
            "includeHighlights": False,
            "includeSourceResultsFormatted": False,
            "sourceResultsNumber": 3,
            "sourceResultsSummaryLength": 100,
            "returnVariables": False,
            "returnVariablesExpanded": False
        }
    }

    # Send POST request to the API
    response = requests.post(API_URL, headers=HEADERS, data=json.dumps(payload))

    # Display the response
    if response.status_code == 200:
        result = response.json()
        st.write("Response:")
        st.json(result)
    else:
        st.error(f"Error: {response.status_code}")
