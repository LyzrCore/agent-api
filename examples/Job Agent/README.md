# Job Agent Powered by [Lyzr Agent API](https://agent.api.lyzr.app/docs#overview) 

**Job Agent** is a Streamlit-based web application that allows users to upload their resume and search for jobs tailored to their skills. The app is powered by the [Lyzr Agent API](https://agent.api.lyzr.app/docs#overview) platform, and Serp API to provide AI-driven job search capabilities.

## Features

- Upload your resume (PDF format).
- Search for jobs based on your resume using AI.
- Got the Task status on display
- Get a mail with the matched jobs
- Powered by Lyzr, OpenAI, and Serp API.

## Prerequisites

Before running the application, make sure you have the following:

- Python 3.9+
- Required API keys from:
  - OpenAI
  - Lyzr X
  - Serp API
- Installed dependencies from `requirements.txt`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/job-agent.git
   ```

2. Navigate to the project directory:
   ```bash
   cd job-agent
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   X_API_Key=your_lyzr_x_key
   SERP_KEY=your_serp_api_key
   ```

## How to Utilize Agent API 
Reference: src/create_agent.py file

## 1. Install Agent API
   ```bash
   pip install lyzr-agent-api
   ```

## 2. Import all the necessary modules and create a client
   ```python
   from lyzr_agent_api import AgentAPI, ChatRequest, EnvironmentConfig, FeatureConfig, AgentConfig

   api_client = AgentAPI(x_api_key="lyzr-api-key")
   ```

## 3. Create Environment
#### Environment have all the resources, modules and tools which can be used by the Agent, before creating an agent we need to configure the environment first with the necessary `Modules` and `Tools`.

   ```python
   environment_configuration = EnvironmentConfig(
        name="Environment Name",
        features=[
            FeatureConfig(
                type="HUMANIZER",  
                config={"max_tries": 3},
                priority=0
            )
        ],
        tools=["perplexity_search", "send_email"],
        llm_config={"provider": "openai",
                    "model": "gpt-4o-mini",
                    "config": {
                        "temperature": 0.5,
                        "top_p": 0.9
                    },
                    "env": {
                        "OPENAI_API_KEY": 'openai-api-key'
                    }
                    }
    )

   environment = api_client.create_environment_endpoint(json_body=environment_configuration)

   env_id = environment['env_id']
   ```

## 4. Create Agent
#### Agent will use the Environment resources, you can create multiple agents in one environment as per your use case.
   ```python
      agent_config = AgentConfig(
            env_id=env_id,  # Environment ID
            system_prompt='You are an helpful agent', # You can define step by step approach for the task/processes.
            name="Agent Name",
            agent_description='Agent Description'
         )

      agent = api_client.create_agent_endpoint(json_body=agent_config)

      agent_id = agent['agent_id']
   ```

## 5. Chat with Agent
#### Once you created the `Environment` with some resources, and an `Agent` who can use those resouces within the environment, Now you can chat with the agent regarding your given task, with the help of `Chat` you can get the response of your query/task.

   ```python
   chat_json_body = ChatRequest(
        user_id=user_id, 
        agent_id=agent_id, # Agent ID
        message=message,   # Define your message
        session_id=session_id
    )

    response = api_client.chat_with_agent(json_body=chat_json_body)

    output = response['response']
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open the app in your browser at `http://localhost:8501`.

3. Upload your resume in PDF format using the file uploader.

4. Click the "Search Jobs" button to start the AI-powered job search.

5. View job results displayed in a card layout with details such as:
   - Job title
   - Company name
   - Job description
   - Apply link

6. Apply for jobs directly using the provided link.

## Project Structure

```
Job-Agent/
│
├── src/
│   │   ├── logo/                      # Folder for image assets like logos
│   │   ├── lyzr-logo-cut.png       # Lyzr logo asset (cropped)
│   │   └── lyzr-logo.png           # Lyzr logo asset (standard)
│   │
│   │
│   ├── utils/                      # Utility functions and helper scripts
│   │   │   ├── __init__.py             # Initialize the utils package
│   │   └── utils.py                # Utility functions for the application
│   │
│   ├── __init__.py                 # Initialize the src package
│   │   └── job_finder.py               # Logic for job searching and API interaction
│
├── app.py                          # Main Streamlit app entry point
│
├── .env                            # Environment file for API keys (not tracked in version control)
├── requirements.txt                # List of Python dependencies
└── README.md                       # Project description and setup instructions
```