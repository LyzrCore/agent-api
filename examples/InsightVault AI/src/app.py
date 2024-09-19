import streamlit as st
import os
from lyzr_agent_api import AgentAPI, ChatRequest
from utils import page_config, style_app, template_end, about_app, social_media
from dotenv import load_dotenv

load_dotenv()

LYZR_API_KEY = os.getenv('X_API_Key')
Agent_ID = os.getenv('AGENT_ID')
User_ID = os.getenv('USER_ID')
Session_ID = os.getenv('SESSION_ID')

page_config()
style_app()


image = "src/logo/lyzr-logo-cut.png"
st.image(image=image, width=100)

st.header("InsightVault AI")
st.markdown("##### Powered by [Lyzr Agent API](https://agent.api.lyzr.app/docs#overview)")
st.markdown('---')

researchquery = st.text_input(label="Enter you research query")

if st.button('Search'):
    if researchquery:    
        with st.spinner("Getting the Search Data"):
            client = AgentAPI(x_api_key=LYZR_API_KEY)

            chat_json = ChatRequest(
                user_id=User_ID,
                agent_id=Agent_ID,
                message=researchquery,
                session_id=Session_ID
            )

                    
            script = client.chat_with_agent(json_body=chat_json)
                    
            if script:
                st.write(script['response']) 

    else:
        st.warning('First provide the research input')


template_end()
st.sidebar.markdown('---')
about_app()
st.sidebar.markdown('---')
social_media(justify="space-evenly")