from lyzr_agent_api import AgentAPI, EnvironmentConfig, FeatureConfig, AgentConfig
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize the Agent API client
api_client = AgentAPI(x_api_key=os.getenv('X_API_Key'))


# Configure the Environment
environment_configuration = EnvironmentConfig(
        name="Agriculture Environment",
        features=[
            FeatureConfig(
                type="SHORT_TERM_MEMORY",
                config={"max_tries": 3},
                priority=0,
            ),
            FeatureConfig(
                type="TOOL_CALLING",
                config={"max_tries": 3},
                priority=0
            ),
            FeatureConfig(
                type="HUMANIZER",
                config={"max_tries": 3},
                priority=0
            )
        ],
        tools=["perplexity_search","send_email"],
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
agent_sys_prompt = """
                        Task 1: Problem Identification
                        Analyze the leaf image description: {leafImageDescription}. Identify any visible issues such as diseases, nutrient deficiencies, pests, or environmental stress. Provide a detailed diagnosis of the problems affecting the plant’s health.

                        Task 2: Treatment Recommendations and Analysis
                        For the identified problems from Task 1, provide the following:

                        Treatment Recommendations: Specific actions or products to treat or mitigate the issue.
                        Causes: Explanation of the root cause (e.g., pest infestation, nutrient deficiency, fungal infection).
                        Why This Happens: Insights into contributing factors (e.g., environmental conditions, improper care).
                        Task 3: Pesticide/Fertilizer Search and Recommendations
                        Find relevant pesticides, fertilizers, or other products to address the diagnosed issues. Provide links or detailed recommendations for their use, ensuring they are suitable for the problems identified in Task 1.

                        [Important] After completing all tasks, combine the information into a clear and concise output. Ensure it is easy to understand, and include any links with descriptions. Keep the explanation simple and straightforward.
                    """  


agent_config = AgentConfig(
        env_id=env_id,  
        system_prompt=agent_sys_prompt,
        name="Leaf Disease Detector",
        agent_description='An agent which can detect disease in leafs and provide the treatment accordingly'
    )


# Creating an agent with the above agent config
agent = api_client.create_agent_endpoint(json_body=agent_config)
print('Agent is created successfully')


# Getting the agent id
agent_id = agent['agent_id']


print(agent_id) #63kjksdbxxxgkxxxx45