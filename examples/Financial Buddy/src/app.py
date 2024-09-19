import streamlit as st
import os
import pandas as pd
from lyzr_agent_api import AgentAPI, ChatRequest
from utils import page_config, style_app, template_end, about_app, social_media
from utils import  remove_existing_files, save_uploaded_file, get_files_in_directory

from dotenv import load_dotenv

load_dotenv()

LYZR_API_KEY = os.getenv('X_API_Key')
Agent_ID = os.getenv('AGENT_ID')
User_ID = os.getenv('USER_ID')
Session_ID = os.getenv('SESSION_ID')

Data = 'Data'
os.makedirs(name=Data, exist_ok=True)

page_config()
style_app()


image = "src/logo/lyzr-logo.png"
st.image(image=image, width=200)

st.header("Finance Buddy AI")
st.markdown("##### Powered by [Lyzr Agent API](https://agent.api.lyzr.app/docs#overview)")
st.markdown('---')

budget_csv_file = st.file_uploader(label="Upload your Monthly Expenses CSV file", type=["csv"])
monthly_income = st.text_input(label="Provide your monthly income")


if st.button('Get Analysis'):
    if (budget_csv_file and monthly_income):
        remove_existing_files(directory=Data)
        save_uploaded_file(directory=Data, uploaded_file=budget_csv_file)

        budget_file = get_files_in_directory(directory=Data)
        budgetDataFrame = pd.read_csv(budget_file[0])

        agent_api_client = AgentAPI(x_api_key=LYZR_API_KEY)
        chat_body = ChatRequest(
            user_id=User_ID,
            agent_id=Agent_ID,
            message=f"This is the Budget file:{budgetDataFrame} and users montly income:{monthly_income}",
            session_id=Session_ID
        )

        analysis = agent_api_client.chat_with_agent(json_body=chat_body)

        if analysis:
            st.markdown('---')
            st.write(analysis['response'])

    else:
        st.warning('Please provide the Budget file and monthly income')



template_end()
st.sidebar.markdown('---')
about_app()
st.sidebar.markdown('---')
social_media(justify="space-evenly")

