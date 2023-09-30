import openai
import streamlit as st
from streamlit_chat import message

# Set your OpenAI API key
openai.api_key = st.secrets["api_key"]

def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.4,
    )
    return completions.choices[0].text.strip()

# Creating the chatbot interface
st.title("Meet AdaptAgent - Workplace Strategy and Change Chatbot")

# Initialize session state for storing chat history
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

# Get user input
user_input = st.text_input("You:", "Hello, how are you?", key="input")

if user_input:
    output = generate_response(user_input)
    # Store the conversation history
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

# Display chat history
if st.session_state['generated']:
    for i in range(len(st.session_state['generated']) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
