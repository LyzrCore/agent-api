import streamlit as st
import os
from utils import (social_media,
                   template_end,
                   page_config,
                   style_app,
                   save_uploaded_file,
                   remove_existing_files,
                   reference_email_draft,
                   about_app)

from job_finder import JobFinder
from create_agent import chat_agent
from dotenv import load_dotenv

load_dotenv()

page_config()
style_app()


openai_api_key = os.getenv('OPENAI_API_KEY')
serp_api_key = os.getenv('SERP_KEY')
Agent_ID = os.getenv('AGENT_ID')
User_ID = os.getenv('USER_ID')
Session_ID = os.getenv('SESSION_ID')


image = "src/logo/lyzr-logo-cut.png"
st.image(image=image)

ResumeData = "ResumeData"
os.makedirs(ResumeData, exist_ok=True)

st.header("Job Agent")
st.markdown("##### Powered by [Lyzr Agent API](https://agent.api.lyzr.app/docs#overview)")
about_app()
st.markdown('---')

resume_file = st.file_uploader(label="Upload your resume pdf file", type=["pdf"])

# Get Job button
if st.button("Search Jobs"):
    if resume_file:
        remove_existing_files(directory=ResumeData)
        save_uploaded_file(directory=ResumeData, uploaded_file=resume_file)
        with st.spinner("🕵🏼‍Searching Jobs For You..."):
            jobs, resumeData = JobFinder(SERP_KEY=serp_api_key, OPENAI_API_KEY=openai_api_key)
            emailReference = reference_email_draft()

            if (jobs and resumeData) != '':
                response = chat_agent(
                    user_id=User_ID,
                    agent_id=Agent_ID,
                    message=f"""This is resume data:{resumeData} and here are the jobs:{jobs}, the reference mail:{emailReference}""",
                    session_id=Session_ID
                )

                if response:
                    st.write('📧Email has been sent...')
                    st.write(response['response'])

            else:
                st.write('Search Again...')

    else:
        st.warning('Please provide the resume')
        remove_existing_files(directory=ResumeData)



template_end()
st.sidebar.markdown('---')
social_media(justify="space-evenly")

