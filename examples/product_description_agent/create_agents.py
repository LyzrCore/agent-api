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
        name="NewsLetter Environment",
        features=[
            FeatureConfig(
                type="HUMANIZER",
                config={},
                priority=0
            )
        ],
        tools=[],
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
        Write a Product Description for below product based on given product specification.
        
        Follow Below Instruction:
        1/ Understand who your target customers are and tailor the description to their needs, preferences, and interests.
        2/ Identify the most important features of the product and emphasize them in your description. Focus on what sets the product apart from others.
        3/ Incorporate relevant keywords into your description to improve search engine visibility and attract organic traffic to your product page.
        4/ Write in a clear and straightforward manner, avoiding jargon or technical language that might confuse customers. Keep sentences and paragraphs short for easy reading.""",
        name="Product description Agent",
        agent_description="This Agent is Craft Product Description."
)

agent = client.create_agent_endpoint(
        json_body=agent_config,
    )

print(agent)  #e.g.{'agent_id':'6jsbjdsxxxxxx'}


