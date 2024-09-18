import os

import streamlit as st
from lyzr_agent_api.client import AgentAPI
from lyzr_agent_api.models.chat import ChatRequest
from dotenv import load_dotenv

load_dotenv()
AGENT_ID = os.getenv("AGENT_ID")
LYZR_API_KEY = os.getenv("OPENAI_API_KEY")


# Initialize the API client
def get_client(api_key):
    return AgentAPI(x_api_key=api_key)


# Streamlit title
st.title("AI Therapist")

# Initialize session state for messages
if 'messages' not in st.session_state:
    st.session_state.messages = []


# Function to handle message sending
def send_message(message):
    if message:
        # Initialize the API client
        client = get_client(LYZR_API_KEY)

        # Send message to agent
        response = client.chat_with_agent(
            json_body=ChatRequest(
                user_id="user@example.com",
                agent_id=AGENT_ID,
                message=message,
                session_id="asjs",
            )
        )
        return response


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = send_message(prompt)
        chat_response = response['response']
        response = st.write(chat_response)
    st.session_state.messages.append(
        {"role": "assistant", "content": chat_response}
    )
