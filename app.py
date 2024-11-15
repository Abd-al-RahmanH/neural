import streamlit as st
import requests
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams

# NeuralSeek API setup
neuralseek_url = "https://api.neuralseek.com/v1/crn%3Av1%3Abluemix%3Apublic%3Aneuralseek%3Aus-south%3Aa%2F3d921d6e5e204570a252619c28d03770%3A74ef5ca7-03d9-4b62-b3e9-7fe92d57b60b%3A%3A/seek"
neuralseek_headers = {
    "accept": "application/json",
    "apikey": "0635bf09-28e77037-673a0b92-1494764a",
    "Content-Type": "application/json"
}

# Watsonx API setup for IBM Watson Model
api_key = "zf-5qgRvW-_RMBGb0bQw5JPPGGj5wdYpLVypdjQxBGJz"
project_id = "32a4b026-a46a-48df-aae3-31e16caabc3b"

creds = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": api_key
}

params = {
    GenParams.DECODING_METHOD: "sample",
    GenParams.MAX_NEW_TOKENS: 2000,
    GenParams.MIN_NEW_TOKENS: 1,
    GenParams.TEMPERATURE: 0.7,
    GenParams.TOP_K: 50,
    GenParams.TOP_P: 1,
    GenParams.STOP_SEQUENCES: ["Human:", "AI:"]
}

# Initialize the Watsonx LLM model
llm = Model(ModelTypes.CODELLAMA_34B_INSTRUCT_HF, creds, params, project_id)

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def query_neuralseek(question):
    """Queries the NeuralSeek API."""
    payload = {
        "question": question,
        "user_session": {
            "metadata": {"user_id": ""},
            "system": {"session_id": ""}
        },
        "params": [],
        "options": {"response_length": "extended"}
    }
    response = requests.post(neuralseek_url, headers=neuralseek_headers, json=payload)
    if response.status_code == 200:
        return response.json().get("answer", "No answer found from NeuralSeek.")
    else:
        return f"Failed to retrieve answer from NeuralSeek: {response.status_code}"

def query_watsonx(question):
    """Queries the Watsonx LLM."""
    prompttemplate = f"""
    [INST]<<SYS>>Provide a detailed response in English<<SYS>>
    {question}
    [/INST]
    """
    response = llm.generate_text(prompttemplate)
    if response:
        return response
    else:
        return "No answer found from Watsonx."

# Streamlit app layout
st.title("NeuralSeek and Watsonx LLM Chat")
st.markdown("This chat interface uses NeuralSeek and Watsonx for answering queries. Enter your question below:")

# Display chat history
for chat in reversed(st.session_state.chat_history):
    st.write(f"**You:** {chat['question']}")
    st.write(f"**Response:** {chat['response']}")

# Input bar at the bottom
question = st.text_input("Enter your question:", key="question_input")

# Handle new question submission
if question:
    # Choose model based on query content
    # Replace "specific_keyword" with logic to identify NeuralSeek-specific queries if necessary
    if "specific_keyword" in question.lower():
        response = query_neuralseek(question)
    else:
        response = query_watsonx(question)

    # Add question and response to chat history
    st.session_state.chat_history.append({"question": question, "response": response})

    # Clear the input box after submission by reinitializing the text input key
    st.session_state["question_input"] = None
