import streamlit as st
import os
import pandas as pd
from lyzr_agent_api import AgentAPI, ChatRequest
from utils import page_config, style_app, template_end, about_app, social_media, disclamer_app
from utils import company_list, save_option, extract_company_info, get_files_in_directory
from utils import  remove_existing_files, file_checker, select_box_css

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


image = "src/logo/lyzr-logo-light.png"
st.image(image=image, width=200)

st.header("StockSage AI")
st.markdown("##### Powered by [Lyzr Agent API](https://agent.api.lyzr.app/docs#overview)")
st.markdown('---')


options_list = company_list()

select_box_css()
selected_option = st.selectbox("Select a Company", options_list)
movement_trends = st.selectbox('Select any movement trend', ['30-days', '90-days'])

col1, col2 = st.columns(2)
with col1:
    if st.button("Save Option"):
        if movement_trends == "30-days":
            save_option(selected_option, movementTrends='1mo', directory=Data)

        elif movement_trends == "90-days":
            save_option(selected_option, movementTrends='3mo', directory=Data)


with col2:
    if st.button('Clear'):
        remove_existing_files(Data)
        


file = file_checker(directoryName=Data)
if len(file) > 0:
    st.info(f"You have selected: {selected_option} Company Stocks with price movement trend of {movement_trends}")
else:
    st.warning("You don't have any data to analyze")



if st.button('Analyze'):
    if (len(file) > 0):

        company_info = extract_company_info(ticker_symbol=selected_option)

        company_csv_filepath = get_files_in_directory(directory=Data)
        company_df = pd.read_csv(company_csv_filepath[0])

        agent_api_client = AgentAPI(x_api_key=LYZR_API_KEY)

        chat_body = ChatRequest(
            user_id=User_ID,
            agent_id=Agent_ID,
            message=f"This is company info:{company_info} and this is the company stock data file{company_df} for {movement_trends}",
            session_id=Session_ID
        )

        analysis = agent_api_client.chat_with_agent(json_body=chat_body)

        if analysis:
            disclamer_app()
            st.markdown('---')
            st.write(analysis['response'])

    else:
        st.warning('Please save the company data')



template_end()
st.sidebar.markdown('---')
about_app()
st.sidebar.markdown('---')
social_media(justify="space-evenly")