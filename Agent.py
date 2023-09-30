import openai
import streamlit as st
from streamlit_chat import message

# Access the OpenAI API key from st.secrets
api_key = st.secrets["openai"]["api_key"]

# Initialize the OpenAI API client with the retrieved API key
openai.api_key = api_key

# Define a workplace strategy knowledge base
workplace_strategy_knowledge = """
Workplace Strategy is the art and science of aligning an organisation's people with their physical work environment(s) to improve organisational performance. It is led by business outcomes, not design. It is the foundation for workplace transformation. It works by aligning people outcomes (such as behaviours and perceptions) and translating these into a recipe for the design and operation of their workplace environments.
It includes: management consulting, workforce discovery activities, workspace analytics, occupancy studies, clarification of the future state, leadership alignment, design requirements and technology requirements.
It does not include: Interior design, Architecture, Project Management, Technology expertise, Organisational Development or Organisational Psychology.
Change management supports Workplace Strategy by helping to deliver on the people outcomes. It includes capability building, influencing, alignment and change leadership. It does not include Interior design, Architecture, Project Management, Technology expertise, Organisational Development or Organisational Psychology.
"""

def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt + workplace_strategy_knowledge,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.4,
    )
    return completions.choices[0].text.strip()

# Creating the chatbot interface
st.title("Meet AdaptAgent - our Workplace Strategy and Change Chatbot")

# Initialize session state for storing chat history
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

# Display chat history
if st.session_state['generated']:
    for i in range(len(st.session_state['generated']) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

# Get user input below the output
user_input = st.text_input("You:", "What is workplace strategy?", key="input")

if user_input:
    output = generate_response(user_input)
    # Store the conversation history
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)
