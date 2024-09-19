import os
import json
import streamlit as st
import shutil
import base64
from openai import OpenAI
from st_social_media_links import SocialMediaIcons 



def social_media(justify=None):
    # This function will help you to render socila media icons with link on the app
    social_media_links = [
    "https://github.com/LyzrCore/lyzr",
    "https://www.youtube.com/@LyzrAI",
    "https://www.instagram.com/lyzr.ai/",
    "https://www.linkedin.com/company/lyzr-platform/posts/?feedView=all"
                        ]   

    social_media_icons = SocialMediaIcons(social_media_links)
    social_media_icons.render(sidebar=True, justify_content=justify) # will render in the sidebar



def style_app():
    # You can put your CSS styles here
    st.markdown("""
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    [data-testid="stSidebar"][aria-expanded="true"]{
           min-width: 450px;
           max-width: 450px;
           background-color: #E9EFEC
;
       }
    </style>
    """, unsafe_allow_html=True)



def page_config(layout = "centered"):
    st.set_page_config(
        page_title="InsightVault AI",
        layout=layout,  # or "wide" 
        initial_sidebar_state="auto",
        page_icon="./logo/lyzr-logo-cut.png"
    )

def about_app():
    with st.sidebar.expander("ℹ️ - Why this InsightVault AI"):
        st.sidebar.caption(""" InsightVault AI is your intelligent research companion leverages the Lyzr Agent API. It provides contextual search for your research queries, automatically summarizes and organizes findings, and maintains a persistent knowledge base to enhance your learning and productivity.
        """)


def template_end():
    st.sidebar.markdown("### This app is build by using Lyzr's Agent API ")

    st.sidebar.markdown(
        """
        <style>
        .button-container {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
        }
        .button-column {
            flex: 1;
            margin-right: 5px;
        }
        .button-column:last-child {
            margin-right: 0;
        }
        .sidebar-button {
            display: block;
            width: 100%;
            padding: 10px;
            margin: 5px 0;
            text-align: center;
            color: white;
            background-color: #ffffff;
            border: none;
            border-radius: 5px;
            text-decoration: none;
        }
        .sidebar-button:hover {
            background-color: #7458E8;
        }
        </style>

        <div class="button-container">
            <div class="button-column">
                <a class="sidebar-button" href="https://www.lyzr.ai/" target="_blank">Lyzr</a>
                <a class="sidebar-button" href="https://www.lyzr.ai/book-demo/" target="_blank">Book a Demo</a>
                <a class="sidebar-button" href="https://agent.api.lyzr.app/docs#overview" target="_blank">Lyzr Agent API</a>
                <a class="sidebar-button" href="https://discord.gg/nm7zSyEFA2" target="_blank">Discord</a>
                <a class="sidebar-button" href="https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw" target="_blank">Slack</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )



