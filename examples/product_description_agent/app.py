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
    page_title="Lyzr Product Description Generator",
    layout="centered",  # or "wide"
    initial_sidebar_state="auto",
    page_icon="lyzr-logo-cut.png",
)

image = Image.open("lyzr-logo.png")
st.image(image, width=150)

st.title("Lyzr Product Description Generator")
st.markdown("### Welcome to the Lyzr Product Description Generator!")

# Initialize the LyzrAgent
client = AgentAPI(x_api_key=LYZR_API_KEY)

# Input area for the product description and target audience
query = st.text_area("Enter Product Specification Here", height=150)

if st.button("Generate"):
    if query.strip():
        with st.spinner("Writing Product Description..."):
            response = client.chat_with_agent(
                json_body=ChatRequest(
                    user_id="user@example.com",
                    agent_id=AGENT_ID,
                    message=query,
                    session_id="sdfw",
                )
            )
            # Display the generated email
            st.markdown(f"**Product Description:**\n\n{response['response']}")
    else:
        st.warning("Please provide Product Specification")

# Optional footer or credits
st.markdown("---")
st.markdown("Powered by Lyzr and OpenAI")
