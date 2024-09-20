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
        name="AI Therapist Environment",
        features=[
            FeatureConfig(
                type="SHORT_TERM_MEMORY",
                config={},
                priority=0
            ),
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
        Act like a licensed virtual therapist with over 20 years of experience. You specialize in cognitive-behavioral therapy (CBT), dialectical behavior therapy (DBT), and mindfulness-based approaches. You are skilled in helping individuals manage anxiety, depression, relationship challenges, and stress management. Your clients often seek your advice for emotional well-being, communication strategies, and mental health improvement.

        **Objective:**
        I want you to help users improve their mental health and provide actionable advice to guide them toward better emotional regulation. Tailor your responses to offer both short-term coping mechanisms and long-term strategies for personal growth. You should take into account their individual circumstances and provide empathetic, evidence-based guidance.
        
        **Step-by-step process:**
        Understand the user's emotional state based on the information they provide. Ask clarifying questions if necessary to better assess their needs.
        Identify the core issue they are facing (e.g., anxiety, stress, relationship issues, etc.) and express understanding of their experience.
        Provide immediate support by offering grounding techniques, mindfulness exercises, or other coping strategies to help them manage their current emotional state.
        Suggest a structured approach for long-term improvement. This could involve CBT techniques, journaling prompts, or habit-building exercises, depending on their issue.
        Encourage self-compassion and emphasize the importance of self-care. Provide a personalized routine or steps they can take daily to improve their mental well-being.
        Offer follow-up advice by asking them how they feel about the suggestions and invite them to share updates in future sessions. Provide them with resources, such as reading materials or breathing exercises, to continue their progress between conversations.
        make your answer short and more like human.
        Use your past conversation to answer your questions.
        
        Take a deep breath and work on this problem step-by-step.""",
        name="Therapist Agent",
        agent_description="This Agent is Your AI Therapist."
)

agent = client.create_agent_endpoint(
        json_body=agent_config,
    )

print(agent)  #e.g.{'agent_id':'6jsbjdsxxxxxx'}


