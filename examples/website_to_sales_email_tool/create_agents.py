import os
from lyzr_agent_api.client import AgentAPI
from lyzr_agent_api.models.agents import AgentConfig
from lyzr_agent_api.models.environment import EnvironmentConfig, FeatureConfig
from dotenv import load_dotenv

load_dotenv()
LYZR_API_KEY = os.getenv("LYZR_API_KEY")

#Initialize Lyzr Agent API client
client = AgentAPI(x_api_key=LYZR_API_KEY)

env_config = EnvironmentConfig(
        name="Twitter Environment",
        features=[
            FeatureConfig(
                type="TOOL_CALLING",
                config={"max_tries": 5},
                priority=0
            )
        ],
        tools=["fetch_content"],
        llm_config={
            "provider": "openai",
            "model": "gpt-4o-mini",
            "config": {
                "temperature": 0.5,
                "top_p": 0.9
            },
            "env": {
                "OPENAI_API_KEY": "OPENAI-API-KEY"
            }
        },
)

environment = client.create_environment_endpoint(
    json_body=env_config
)

print(environment)  #e.g. {'environment_id':'63bjsdbxxxxxxx'}

agent_config = AgentConfig(
        env_id=environment['environment_id'],  # Example environment ID
        system_prompt="""
        You are an web scrapping agent your task is to scrap given url by using fetch_content Tool and show response.""",
        name="Scraping Agent",
        agent_description="This Agent is Scrap Websites."
)

agent = client.create_agent_endpoint(
        json_body=agent_config,
    )

print(agent)  #e.g.{'agent_id':'6jsbjdsxxxxxx'}


