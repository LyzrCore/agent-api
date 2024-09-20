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
        name="Property suggestor Environment",
        features=[
            FeatureConfig(
                type="KNOWLEDGE_BASE",
                config={
                "lyzr_rag": {
                    "base_url": "https://rag-agent-api.dev.app.lyzr.ai",
                    "rag_id": "14011xxxxxx"
                }
                },
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
        You are a Property Recommandation Chatbot.Your Task is to Recommend best property for their requirements from given property.
        Give all Properties information with virtual tour link and listing link.
        After recommending Property tell them if they want to discuss more or want to see more properties then book meeting and give below meeting link.
        Meeting link: https://calendly.com/xxxxxx""",
        name="Property Suggestor Agent",
        agent_description="This Agent is Suggest Properties based on your requirements."
)

agent = client.create_agent_endpoint(
        json_body=agent_config,
    )

print(agent)  #e.g.{'agent_id':'6jsbjdsxxxxxx'}


