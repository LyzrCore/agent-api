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
                type="SHORT_TERM_MEMORY",
                config={},
                priority=0
            ),
            FeatureConfig(
                type="TOOL_CALLING",
                config={"max_tries": 3},
                priority=0
            )
        ],
        tools=["perplexity_search"],
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
        Act like an experienced newsletter writer skilled in crafting engaging and informative content. 
        Use a perplexity search to find the most relevant and current information on Given Topic. 
        Your goal is to summarize the key insights and trends into a concise, well-structured newsletter that keeps readers informed and interested. 
        Include engaging headlines, clear sections, and a call to action.
    
        Take a deep breath and work on this problem step-by-step.""",
        name="NewsLetter Agent",
        agent_description="This Agent is Research And Craft newsletter."
)

agent = client.create_agent_endpoint(
        json_body=agent_config,
    )

print(agent)  #e.g.{'agent_id':'6jsbjdsxxxxxx'}


