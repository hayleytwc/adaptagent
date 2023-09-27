import streamlit as st
import openai
import toml
import nltk

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
        bot_response = response.choices[0].text.strip()
        st.text("AdaptAgent: " + bot_response)

# Extract the AI response
ai_response = response.choices[0].text

# Post-process the response to truncate it at the end of a sentence
sentences = nltk.sent_tokenize(ai_response)
if len(sentences) > 0:
    truncated_response = ' '.join(sentences[:-1])  # Keep all sentences except the last one
else:
    truncated_response = ai_response  # No sentences found, use the original response

# Display the truncated response
print("Truncated Response:", truncated_response)
