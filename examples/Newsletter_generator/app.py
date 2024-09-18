import os
from lyzr_agent_api import AgentAPI, ChatRequest
import streamlit as st
from dotenv import load_dotenv
from PIL import Image

# Load environment variables
load_dotenv()
LYZR_API_KEY = os.getenv("LYZR_API_KEY")
AGENT_ID = os.getenv("AGENT_ID")

# Streamlit page configuration
st.set_page_config(
    page_title="Lyzr Newsletter Generator",
    layout="centered",  # or "wide"
    initial_sidebar_state="auto",
    page_icon="lyzr-logo-cut.png",
)

image = Image.open("lyzr-logo.png")
st.image(image, width=150)

st.title("Lyzr Newsletter Generator")
st.markdown("### Welcome to the Lyzr Newsletter Generator!")

# Initialize the LyzrAgentAPI
client = AgentAPI(x_api_key=LYZR_API_KEY)


# Input area for the product description and target audience
query = st.text_area("Enter Topic and description", height=150)

if st.button("Generate NewsLetter"):
    with st.spinner("Generating NewsLetter..."):
        response = client.chat_with_agent(
            json_body=ChatRequest(
                user_id="user@example.com",
                agent_id=AGENT_ID,
                message=query,
                session_id="sdfw",
            )
        )
        # Display the generated email
        st.markdown(f"**Generated NewsLetter:**\n\n{response['response']}")

# Optional footer or credits
st.markdown("---")
st.markdown("Powered by Lyzr and OpenAI")
