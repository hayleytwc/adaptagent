import streamlit as st
import openai
import re

# Access the OpenAI API key from st.secrets
api_key = st.secrets["openai"]["api_key"]

# Initialize the OpenAI API client with the retrieved API key
openai.api_key = api_key

# Streamlit UI
st.title("Meet AdaptAgent - Workplace Strategy and Change Chatbot")
st.write("Chat with the Workplace Strategy Consultant!")

user_input = st.text_input("You:", "")
if st.button("Send"):
    if user_input.strip() != "":
        # Call the API to get a response
        prompt = f"As a workplace strategy consultant, tell me '{user_input}'?"
        temperature = 0.4
        response = openai.Completion.create(
            engine="babbage-002",
            prompt=prompt,
            max_tokens=500,  # Adjust the response length as needed
            temperature=temperature
        )

        # Extract the response text
        text = response.choices[0].text.strip()

        # Split the response into sentences
        sentences = re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s", text)

        # Print the sentences (for debugging)
        print(sentences)
