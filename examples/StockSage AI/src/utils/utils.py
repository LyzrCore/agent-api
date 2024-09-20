import os
import streamlit as st
import shutil
import yfinance as yf
import pandas as pd
from pathlib import Path
from st_social_media_links import SocialMediaIcons 

def remove_existing_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            st.error(f"Error while removing existing files: {e}")



def get_files_in_directory(directory):
    # This function help us to get the file path along with filename.
    files_list = []

    if os.path.exists(directory) and os.path.isdir(directory):
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            
            if os.path.isfile(file_path):
                files_list.append(file_path)

    return files_list


def save_uploaded_file(directory, uploaded_file):
    remove_existing_files(directory=directory)
    file_path = os.path.join(directory, uploaded_file.name)
    with open(file_path, "wb") as file:
        file.write(uploaded_file.read())


def get_file_name(directory):
    try:
        files = os.listdir(directory)
        file_names = [file for file in files if os.path.isfile(os.path.join(directory, file))]
        
        return file_names[0]
    
    except FileNotFoundError:
        return f"The directory '{directory}' does not exist."
    
    except Exception as e:
        return f"An error occurred: {e}"


def file_checker(directoryName):
    file = []
    for filename in os.listdir(directoryName):
        file_path = os.path.join(directoryName, filename)
        file.append(file_path)

    return file

def company_list():
    company_lst = []
    eq = pd.read_csv(Path('EquityData/equity.csv'))

    for name in eq.SYMBOL:
        company_lst.append(f"{name}.NS")

    return company_lst

def save_option(ticker_symbol, directory, movementTrends):
    # Downlaod company data
    dataframe = yf.download(ticker_symbol, period=movementTrends)
    remove_existing_files(directory=directory)
    dataframe.to_csv(f"{directory}/{ticker_symbol}.csv")

def extract_company_info(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    
    # Fetch company info
    company_info = ticker.info
    
    # Extract relevant information
    extracted_info = {
        'Symbol': ticker_symbol,
        'Name': company_info.get('longName'),
        'Industry': company_info.get('industry'),
        'Sector': company_info.get('sector'),
        'Address': f"{company_info.get('address1')}, {company_info.get('address2')}, {company_info.get('city')}, {company_info.get('country')}",
        'Phone': company_info.get('phone'),
        'Website': company_info.get('website'),
        'Description': company_info.get('longBusinessSummary'),
        'Full-Time Employees': company_info.get('fullTimeEmployees'),
        'Trailing P/E': company_info.get('trailingPE'),
        'Forward P/E': company_info.get('forwardPE'),
        'Trailing EPS': company_info.get('trailingEps'),
        'Forward EPS': company_info.get('forwardEps'),
        'Dividend Rate': company_info.get('dividendRate'),
        'Dividend Yield': company_info.get('dividendYield'),
        'Beta': company_info.get('beta'),
        'Market Cap': company_info.get('marketCap'),
        '52-Week High': company_info.get('fiftyTwoWeekHigh'),
        '52-Week Low': company_info.get('fiftyTwoWeekLow'),
        'Revenue': company_info.get('totalRevenue'),
        'Gross Margins': company_info.get('grossMargins'),
        'Operating Margins': company_info.get('operatingMargins'),
        'Net Income': company_info.get('netIncomeToCommon'),
        'Debt to Equity': company_info.get('debtToEquity'),
        'Book Value': company_info.get('bookValue'),
        'Price to Book': company_info.get('priceToBook'),
        'Analyst Recommendation Mean': company_info.get('recommendationMean'),
        'Target Mean Price': company_info.get('targetMeanPrice'),
        'Current Price': company_info.get('currentPrice'),
        'Revenue Growth': company_info.get('revenueGrowth'),
        'Earnings Growth': company_info.get('earningsGrowth')
    }
    
    return extracted_info

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
           background-color: #2C2C2C;
       }
    </style>
    """, unsafe_allow_html=True)

def select_box_css():
    st.markdown(
    """
    <style>
    /* Change background and text color of the selectbox */
    div[data-baseweb="select"] > div {
        background-color: #ffffff; /* Change this to your desired background color */
        color: #000000; /* Change this to your desired text color */
        font-weight: bold;
    }
    /* Optional: Change the dropdown options' text color */
    div[data-baseweb="select"] > div > div > div {
        color: #000000; /* Change this to your desired text color */
    }
    </style>
    """,
    unsafe_allow_html=True
    )


def page_config(layout = "centered"):
    st.set_page_config(
        page_title="StockSage AI:",
        layout=layout,  # or "wide" 
        initial_sidebar_state="auto",
        page_icon="./logo/lyzr-logo-cut.png"
    )

def about_app():
    with st.sidebar.expander("ℹ️ - Why this StockCast AI"):
        st.sidebar.caption("""StockSage is an AI-powered stock analysis tool leveraging Lyzr's Agent API to evaluate stock performance based on historical trends, market sentiment, and key financial indicators. The app provides users with intelligent insights to identify and invest in better-performing stocks.
        """)

def disclamer_app():
    with st.expander("Disclaimer - StockCast AI"):
        st.caption("""StockSage provides stock recommendations based on data-driven analysis; however, all investments carry risk, and past performance is not indicative of future results. Users are advised to conduct their own research and consult with a licensed financial advisor before making any investment decisions.
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



