import streamlit as st
import openai
import toml

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
        # Call the GPT-3 API to get a response
        prompt = f"As a workplace strategy consultant, how can I assist you with '{user_input}'?"
        temperature = 0.4
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=1024,  # Adjust the response length as needed
            temperature=temperature
        )
        bot_response = response.choices[0].text.strip()
        st.text("AdaptAgent: " + bot_response)
