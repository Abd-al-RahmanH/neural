import streamlit as st
import requests

# Streamlit UI
st.title("Neural Seek with Streamlit")
st.write("Enter your query below to interact with Neural Seek:")

# Input Field
user_query = st.text_input("Query", placeholder="Type your query here...")

# Submit Button
if st.button("Submit"):
    if user_query:
        # Neural Seek API Call
        url = "https://<neuralseek-endpoint-url>/query"  # Replace with actual API endpoint
        headers = {
            "Authorization": "Bearer <your-api-key>",  # Replace with your API key
            "Content-Type": "application/json"
        }
        payload = {"query": user_query}

        try:
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                result = response.json()
                # Display Results
                st.write("Result:")
                st.write(result.get("answer", "No answer found."))
            else:
                st.error(f"Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a query.")

# Run the Streamlit app using streamlit run streamlit_app.py
