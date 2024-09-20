from lyzr_agent_api import AgentAPI, ChatRequest, EnvironmentConfig, FeatureConfig, AgentConfig
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize the Agent API client
api_client = AgentAPI(x_api_key=os.getenv('X_API_Key'))


# Configure the Environment
environment_configuration = EnvironmentConfig(
        name="Job Agent Environment",
        features=[
            FeatureConfig(
                type="HUMANIZER",
                config={"max_tries": 3},
                priority=0
            ),
            FeatureConfig(type="TOOL_CALLING",
                          config={"max_tries": 3},
                          priority=0)
        ],
        tools=["perplexity_search", "send_email"],
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
                    You are an expert job role, job matching, and email scraping agent.

                    Task 1 (Resume Parsing):
                    Given the following resume data: {resumeData}, extract the skills, experience, and other relevant information from it. After extraction, decide the most suitable job role for the candidate. 
                    
                    Task 2 (Job Matching):
                    If job search data is provided, analyze the following job search results and compare them with the extracted resume data.
                    Job Search Results (JSON): {searchJobData}

                    Please extract and filter the job listings where the job description or qualifications align with the candidate's resume data. 
                    [!Important] Make sure the required job experience and skills are matched with the candidate's experience based on their resume.

                    Task 3	
                    The output should contains the matched job with their title, description and apply link.

                    Task 4 (Email Scraping and Sending):
                    Scrape the candidate's email from the resume data: {resumeData}.
                    Once the email is scraped, draft an email message to the candidate informing them about the suitable job role you identified in Task 3.
                    Ensure the message is professional, concise, and personalized and have the output identified in Task 3. First greet the user and provide the jobs with their apply links in the mail.
                    [!Important] Once the email has been created then sent it to receiver email that you find from resume. 
                    """


agent_config = AgentConfig(
        env_id=env_id,  
        system_prompt=agent_sys_prompt,
        name="Job Agent",
        agent_description='An Agent for job search'
    )


# Creating an agent with the above agent config
agent = api_client.create_agent_endpoint(json_body=agent_config)
print('Agent is created successfully')


# Getting the agent id
agent_id = agent['agent_id']


print(agent_id) #63kjksdbxxxgkxxxx45