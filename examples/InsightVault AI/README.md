# InsightVault AI Powered by [Lyzr Agent API](https://agent.api.lyzr.app/docs#overview) 

**InsightVault AI** is your intelligent research companion leverages the `Lyzr Agent API`, which seamlessly integrating web search with powerful memory management. It provides contextual search for your research queries, automatically summarizes and organizes findings, and maintains a persistent knowledge base to enhance your learning and productivity. Perfect for professionals, students, and researchers who need a smart, organized approach to managing information.


## Prerequisites

Before running the application, make sure you have the following:

- Python 3.9+
- Required API keys from:
  - OpenAI
  - Lyzr X
- Installed dependencies from `requirements.txt`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/InsightVault-AI.git
   ```

2. Navigate to the project directory:
   ```bash
   cd InsightVault-AI
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   X_API_Key=your_lyzr_x_key
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

### Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```