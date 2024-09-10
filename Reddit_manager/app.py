import os
from lyzr_agent import LyzrAgent
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LYZR_API_KEY = os.getenv("LYZR_API_KEY")
AGENT_ID = os.getenv("AGENT_ID")

# Streamlit page configuration
st.set_page_config(
    page_title="Reddit Manager",
    layout="wide",  # Set the layout to wide
    initial_sidebar_state="auto",
    page_icon="lyzr-logo-cut.png",
)

# Add banner image at the top
st.image("Reddit-Logomark-White-Dark-Background-Logo.wine.svg", width=150)  # Replace with the correct path for the banner image

# Set up two columns for input and output areas
col1, col2 = st.columns([1, 1])  # Adjust the ratio to match the design in the image

with col1:
    st.markdown("## Reddit Manager")

    # Input area for the query
    query = st.text_area("Enter Text Here", height=150)

    # Generate button
    if st.button("Generate"):
        if query.strip():
            with st.spinner("Generating response..."):
                # Initialize the LyzrAgent
                Agent = LyzrAgent(api_key=LYZR_API_KEY, llm_api_key=OPENAI_API_KEY)

                response = Agent.send_message(
                    agent_id=AGENT_ID,
                    user_id="7422",
                    session_id="IITV",
                    message=query
                )

                # Display the response in the second column
                with col2:
                    st.markdown("## Response:")
                    st.markdown(f"**Thoughts:**\n\n{response['response']}")
        else:
            st.warning("Please provide Text")

# Optional footer
st.markdown("---")
st.markdown("Powered by Lyzr and OpenAI")
