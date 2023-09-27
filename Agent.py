import openai
import streamlit as st
from streamlit_chat import message

# Access the OpenAI API key from st.secrets
api_key = st.secrets["openai"]["api_key"]

# Initialize the OpenAI API client with the retrieved API key
openai.api_key = api_key

# Define a workplace strategy knowledge base
workplace_strategy_knowledge = """
Workplace strategy refers to the long-term planning and design of a physical workspace to optimize productivity, employee well-being, and organizational goals. In the UK, workplace strategies have evolved to accommodate flexible working arrangements, sustainability initiatives, and technology integration.

Key aspects of workplace strategy in the UK include:
1. Flexible Work Arrangements: Embracing remote and hybrid work models, hot-desking, and flexible scheduling to adapt to changing work dynamics.
2. Well-being: Prioritizing employee health and well-being through ergonomic design, access to natural light, and wellness programs.
3. Sustainability: Implementing eco-friendly practices, energy-efficient buildings, and reducing the carbon footprint.
4. Technology Integration: Leveraging digital tools for collaboration, data analytics, and smart office solutions.
5. Employee Engagement: Fostering a sense of community, collaboration, and employee engagement through the workspace design.

Keep in mind that workplace strategy should align with your organization's unique goals and culture.
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
st.title("Meet AdaptAgent - Workplace Strategy and Change Chatbot")

# Initialize session state for storing chat history
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

# Initialize the conversation with a greeting
initial_greeting = "How can I help you today?"
st.session_state.generated.append(initial_greeting)

# Get user input
user_input = st.text_input("You:", "What is workplace strategy", key="input")

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
