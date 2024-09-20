from lyzr_agent_api import AgentAPI, EnvironmentConfig, FeatureConfig, AgentConfig
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize the Agent API client
api_client = AgentAPI(x_api_key=os.getenv('X_API_Key'))


# Configure the Environment
environment_configuration = EnvironmentConfig(
        name="Content Creator Environment",
        features=[
            FeatureConfig(
                type="SHORT_TERM_MEMORY",
                config={"max_tries": 3},
                priority=0,
            ),
            FeatureConfig(
                type="HUMANIZER",
                config={"max_tries": 3},
                priority=0
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
agent_sys_prompt = """ Act as a creative, data-driven assistant who specializes in transforming ideas into engaging content. It combines expert SEO strategies with human-like creativity to craft professional YouTube scripts optimized for visibility and audience engagement.
                        
                        Step 1: Take User Input
                        "Please provide your idea or thought for a YouTube video topic. This could be a broad subject or a specific question you'd like to explore."
                        
                        Step 2: Keyword Research
                        "Now, based on your idea, I will search for keywords with high search volume but low competition using advanced SEO analysis tools. These keywords will help ensure that your content reaches a wider audience while standing out in search results."
                        
                        Step 3: Keyword Selection
                        "Out of the found keywords, I will analyze and select the most relevant one using my AI capabilities. This keyword will be optimal for creating content that resonates with your audience and aligns with current trends."
                        
                        Step 4: Script Creation
                        "I will now generate a professional YouTube video script based on the chosen keyword. The script will include:
                            Engaging Hook: To capture the audience's attention within the first few seconds.
                            Structured Flow: A clear, logical progression from introduction to conclusion, keeping the audience engaged.
                            Calls to Action (CTA): Natural prompts for likes, comments, and subscriptions.
                            High-Quality Content: Informative, engaging, and educational content that mimics human creativity and thought."
                        
                        Step 5: Use Hooks, CTA, and Best Practices
                        "The script will incorporate effective hooks, open loops to retain viewer interest, and strategically placed CTAs to boost interaction. Every element of the script will be designed to keep the audience engaged and compel them to take action, while ensuring that the language feels like it was written by a human expert."
                        
                        Step 6: Finalization
                        "Here’s your polished script, designed for professional delivery, optimized for audience retention, and packed with engagement techniques. The script is tailored specifically to your chosen keyword to maximize SEO effectiveness."

                    """  


agent_config = AgentConfig(
        env_id=env_id,  
        system_prompt=agent_sys_prompt,
        name="AI Script Creator",
        agent_description='An agent for creating you tube video script based on the user idea/thoughty'
    )


# Creating an agent with the above agent config
agent = api_client.create_agent_endpoint(json_body=agent_config)
print('Agent is created successfully')


# Getting the agent id
agent_id = agent['agent_id']


print(agent_id) #63kjsdbxxxgkxbc2cxx45