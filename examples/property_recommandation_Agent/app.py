import os
from lyzr_agent_api import AgentAPI, ChatRequest
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
LYZR_API_KEY = os.getenv("LYZR_API_KEY")
AGENT_ID = os.getenv("AGENT_ID")

# Streamlit page configuration
st.set_page_config(
    page_title="Lyzr Property Recommandation chatbot",
    layout="centered",  # or "wide"
    initial_sidebar_state="auto",
    page_icon="lyzr-logo-cut.png",
)

st.title("Lyzr Property Recommandation chatbot")
st.markdown("### Welcome to the Lyzr Property Recommandation chatbot!")

# Initialize the LyzrAgent
client = AgentAPI(x_api_key=LYZR_API_KEY)

# Input area for the product description and target audience
query = st.text_area("Property to Suggest....", height=150)

if st.button("Suggest Property"):
    if query.strip():
        with st.spinner("Looking for Properties..."):
            response = client.chat_with_agent(
                json_body=ChatRequest(
                    agent_id=AGENT_ID,
                    user_id="user@example.com",
                    session_id="djsn",
                    message=query
                )
            )
            # Display the generated email
            st.markdown(f"**Found Properties:**\n\n{response['response']}")
    else:
        st.warning("Please provide property details you are looking for")

# Optional footer or credits
st.markdown("---")
st.markdown("Powered by Lyzr and OpenAI")
