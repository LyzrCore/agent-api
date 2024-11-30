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
    page_title="Lyzr Twitter Agent",
    layout="wide",  # Set the layout to wide
    initial_sidebar_state="auto",
    page_icon="lyzr-logo-cut.png",
)


# Set up two columns for input and output areas
col1, col2 = st.columns([1, 1])  # Adjust the ratio to match the design in the image

with col1:
    st.markdown("## Lyzr Twitter Agent")

    # Input area for the query
    query = st.text_area("Enter Text Here", height=150)

    # Generate button
    if st.button("Generate"):
        if query.strip():
            with st.spinner("🕵🏼‍Researching About Your Topic..."):
                # Initialize the LyzrAgent
                Agent = LyzrAgent(api_key=LYZR_API_KEY, llm_api_key=OPENAI_API_KEY)
                with st.spinner("⚙️Executing Your Tasks...."):
                    response = Agent.send_message(
                        agent_id=AGENT_ID,
                        user_id="7422",
                        session_id="IITV",
                        message=query
                    )
                    st.markdown("🤯Research Completed")
                    st.markdown("✅Your Task Is Completed")

                # Display the response in the second column
                with col2:
                    st.markdown("## Response:")
                    st.markdown(f"**Thoughts:**\n\n{response}")
        else:
            st.warning("Please provide Text")

# Optional footer
st.markdown("---")
st.markdown("Powered by Lyzr and OpenAI")
