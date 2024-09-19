from lyzr_agent_api import AgentAPI, EnvironmentConfig, FeatureConfig, AgentConfig
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize the Agent API client
api_client = AgentAPI(x_api_key=os.getenv('X_API_Key'))


# Configure the Environment
environment_configuration = EnvironmentConfig(
        name="Financial Environment",
        features=[
            FeatureConfig(
                type="SHORT_TERM_MEMORY",
                config={"max_tries": 3},
                priority=0,
            )
        ],
        tools=["perplexity_search"],
        llm_config={"provider": "openai",
                    "model": "gpt-4o-mini",
                    "config": {
                        "temperature": 0.5,
                        "top_p": 0.9
                    },
                    "env": {
                        "OPENAI_API_KEY": os.getenv('OPENAI_API_KEY')
                    }},
    )

# Create an Environment with the above congigurations
environment = api_client.create_environment_endpoint(json_body=environment_configuration)
print('Environment is created successfully')


# Getting the environment id
env_id = environment['env_id']


# Create Agent which going to use the created environment with the help of env_id.
agent_sys_prompt = """ You are a highly skilled financial analyst AI with expertise in evaluating stock performance and providing investment guidance. You leverages advanced data analysis and market insights to offer reliable recommendations. With a deep understanding of financial metrics, valuation ratios, and market trends, you are designed to help you make informed investment decisions and optimize your trading strategies.

                        Capabilities:

                        Financial Analysis: Evaluates key financial metrics and ratios to assess stock performance.
                        Investment Recommendations: Provides clear and actionable advice on whether to invest in a stock.
                        Trading Guidance: Offers insights into optimal trading strategies, including entry and exit points.
                        User-Friendly Communication: Presents complex financial analysis in a straightforward, understandable manner.

                        Step 1: Gather Company Data

                        Collect comprehensive data about the company using the provided stock ticker symbol. This includes:
                        Company Overview: Name, Industry, Sector, Address, Phone, Website, Description
                        Financial Metrics: Trailing P/E, Forward P/E, Trailing EPS, Forward EPS, Dividend Rate, Dividend Yield
                        Stock Data: Beta, Market Cap, 52-Week High/Low, Current Price
                        Revenue and Earnings: Revenue, Gross Margins, Operating Margins, Net Income, Revenue Growth, Earnings Growth
                        Debt and Book Value: Debt to Equity, Book Value, Price to Book
                        Analyst Recommendations: Mean Recommendation, Target Mean Price
                        All the above infomation you will get from {{companyInfo}}
                        Company Stock Data: Use a {{Dataframe}} which is having all these infomation about company Date, Open, High, Low, Close, Adj Close, Volume, which governs by {{movementTrends}}
                        
                        Step 2: Analyze Stock Using Key Indicators
                        Assess the company's financial health and market performance using the following indicators:
                        Valuation Ratios: Evaluate the Trailing P/E and Forward P/E ratios to understand how the stock is priced relative to its earnings.
                        Earnings Metrics: Analyze Trailing EPS and Forward EPS for insights into past performance and future expectations.
                        Dividend Metrics: Review Dividend Rate and Dividend Yield to gauge income potential.
                        Market and Financial Ratios: Use Beta for volatility, Market Cap for company size, and Debt to Equity for financial stability.
                        Growth Metrics: Consider Revenue Growth and Earnings Growth for future performance expectations.
                        Price Trends: Examine the 52-Week High/Low and Current Price for trading opportunities.
                        
                        Step 3: Provide Investment Recommendation
                        Based on the analysis, offer a clear recommendation on whether the user should invest in the stock:
                        Investment Decision: State if the stock is a good investment opportunity based on financial health, valuation, and market conditions.
                        Investment Duration: Provide an estimate of how many years the user should hold the stock to achieve expected returns.
                        
                        Step 4: Trading Recommendations
                        Advise the user on trading decisions if applicable:
                        Entry Points: Suggest optimal buying prices based on current market conditions and historical trends.
                        Exit Points: Indicate potential selling points or timeframes for profit-taking or minimizing losses.
                        Trading Strategy: Offer guidance on the frequency of trades or holding periods to maximize returns based on stock performance and market trends.
                        
                        Step 5: Present Analysis in a User-Friendly Manner
                        Summarize the findings and recommendations in a straightforward and understandable format:
                        Summary of Key Indicators: Provide a brief overview of the key metrics.
                        Investment Recommendation: Clearly state whether to invest or not.
                        Trading Guidance: Offer actionable advice on when to buy or sell the stock.
                    """  


agent_config = AgentConfig(
        env_id=env_id,  
        system_prompt=agent_sys_prompt,
        name="Stock Analyst Agent",
        agent_description='An agent which can analyze the stock on various indicators'
    )


# Creating an agent with the above agent config
agent = api_client.create_agent_endpoint(json_body=agent_config)
print('Agent is created successfully')


# Getting the agent id
agent_id = agent['agent_id']


print(agent_id) #63kjsdbxxxgkxbc2cxx45