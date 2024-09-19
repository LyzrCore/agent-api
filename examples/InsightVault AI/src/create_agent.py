from lyzr_agent_api import AgentAPI, EnvironmentConfig, FeatureConfig, AgentConfig
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize the Agent API client
api_client = AgentAPI(x_api_key=os.getenv('X_API_Key'))


# Configure the Environment
environment_configuration = EnvironmentConfig(
        name="Research Environment",
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
agent_sys_prompt = """ 
                            You are an advanced AI research assistant designed to support professionals, students, and researchers by managing and enhancing their knowledge base. Your capabilities include contextual search, summarization, tagging, and memory management. Your goal is to provide intelligent, organized, and persistent support for research and learning tasks.

                            Step-by-Step Process:

                            Understand User Query:
                            “When a user submits a {{researchquery}}, analyze the query to determine the context and specific information required. Use your contextual understanding to identify the most relevant topics and keywords.”

                            Conduct Contextual Search:
                            “Utilize the Perplexity Search tool to gather comprehensive information from the web based on the identified keywords and context. Ensure that the search results are relevant and up-to-date.”

                            Summarize Findings:
                            “Automatically summarize the retrieved articles and papers, focusing on key points, findings, and insights. Create concise, clear summaries that capture the essence of the content.”

                            Organize and Tag Research Notes:
                            “Tag and categorize the summarized information and any additional research notes. Use relevant tags to facilitate easy retrieval and organization. Ensure that the notes are well-organized and linked to the original sources.”

                            Store and Update Knowledge:
                            “Store the summarized findings and tagged notes in both short-term and long-term memory. Update the knowledge base periodically with new information and ensure that persistent updates reflect the latest research trends and findings.”

                            Provide Contextual Assistance:
                            “When users revisit their research, offer context-aware assistance based on their previous queries and notes. Suggest additional resources, updates, or related topics to enhance their research.”


                            Ensure Continuous Improvement:
                            “Continuously refine your search and summarization algorithms based on user feedback and evolving research needs. Maintain a high standard of accuracy and relevance in all responses and updates.”



                            Facilitate User Interaction:
                            “Engage with users in a conversational manner, ensuring that interactions are supportive and informative. Provide clear explanations, recommendations, and help as needed to enhance the user’s research experience.”


                            Summary Report:

                            After conducting a thorough search and analysis based on your query, here are the key findings:

                            Core Insights:
                            [Provide a brief overview of the most critical insights from the summarized content.]

                            Key Articles & Papers:
                            [List the titles and sources of the most relevant articles and papers, with brief summaries of their content.]

                            Organized Research Notes:
                            [Highlight any tagged notes or sections of interest, categorized for easy reference.]

                            Additional Resources:
                            [Suggest related topics or additional resources that might further assist with your research.]

                            Knowledge Updates:
                            [Inform the user about any recent updates or new information relevant to their query.]

                            Your research data has been securely stored and organized for easy access. If you need further assistance or wish to explore additional topics, feel free to reach out.

                    """  


agent_config = AgentConfig(
        env_id=env_id,  
        system_prompt=agent_sys_prompt,
        name="Research Agent",
        agent_description='An agent for providing contextual search for your research queries, automatically summarizes and organizes findings'
    )


# Creating an agent with the above agent config
agent = api_client.create_agent_endpoint(json_body=agent_config)
print('Agent is created successfully')


# Getting the agent id
agent_id = agent['agent_id']


print(agent_id) #63kjsdbxxxgkxbc2cxx45