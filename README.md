# Lyzr Agent API
[![Discord](https://img.shields.io/badge/Discord-join%20now-blue.svg?style=flat&logo=Discord)](https://discord.gg/uaHrgJQxAv)
![version](https://img.shields.io/badge/version-0.1.0-green.svg)
[![PyPI - License](https://img.shields.io/pypi/l/langchain-core?style=flat-square)](https://opensource.org/licenses/MIT)
[![GitHub star chart](https://img.shields.io/github/stars/LyzrCore/agent-api?style=flat-square)](https://github.com/LyzrCore/agent-api)
[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/LyzrAI.svg?style=social&label=%40LyzrAI)](https://x.com/LyzrAI)
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/LyzrCore/agent-api)

The Lyzr Agent API provides a modular and universal API framework for creating LLM-based agents. It simplifies the development of intelligent agents by offering three main components: Environment, Agent, and Inference. Each component is designed to streamline the setup, configuration, and execution of tasks and conversations.
## 📄 Documentation

Full documentation can be found here: [Lyzr Agent API Documentation](https://docs.lyzr.ai/agent-api/introduction)

Please check it out for the most up-to-date tutorials, how-to guides, references, and other resources!

# 💻 Example Usage
## 1. Installation

First, install the `lyzr-agent-api` package:
```bash
pip install lyzr-agent-api
```
For more detailed installation instructions, refer to the [installation guide on PyPI](https://pypi.org/project/lyzr-agent-api/).
## 2. Initializing the Client

To start using the API, initialize the `AgentAPI` client with your Lyzr API key:

> **Tip:** You can generate your API key from the [Lyzr Agent API Studio](https://agent.lyzr.app).
> 
```python
from lyzr_agent_api.client import AgentAPI

client = AgentAPI(x_api_key="your-lyzr-api-key")
```


## 3. Creating an Environment
The environment is a fundamental building block of the Lyzr Agent API. It defines the modules, features, tools available, and other configurations for your agent. Let's break down the components of the environment:



1. **Features/Modules**: These can be sync modules (which can mutate the message stream) or background modules (which have read-only access).
   
   - #### Sync Modules

     | Module Type                    | Description                                                                 |
     |--------------------------------|-----------------------------------------------------------------------------|
     | `SELF_REFLECTION`              | Enables self-reflection capabilities for the agent, either by using the same model or a different model. |
     | `OPEN_AI_RETRIEVAL_ASSISTANT`  | Offers retrieval capabilities using OpenAI's retriever.                     |
     | `TOOL_CALLING`                 | Allows API tool calling. The agent can call any registered OpenAPI schema-supported API. |
     | `KNOWLEDGE_BASE`               | Provides Lyzr RAG capabilities with fully customizable retriever configurations. |
     | `LONG_TERM_MEMORY`             | Provides long contextual memory using multiple retrieval and summarization strategies. |
     | `SHORT_TERM_MEMORY`            | Provides short contextual memory for a configurable number of messages (n), determining how many messages to fetch per inference. |
     | `HUMANIZER`                    | Humanizes the output of the agent.                                          |

   - #### Background Modules
  
     | Module Type             | Description                                                                 |
     |-------------------------|-----------------------------------------------------------------------------|
     | `STRUCTURED_MEMORY`     | Acts as a structured JSON memory collector, storing structured information during conversations or task processes. |
     | `LOGGING`               | Acts as a structured JSON memory collector, storing structured information during conversations or task processes. |

2. **Tools**: External APIs that an agent can utilize.

3. **llm_api_key**: The key for the language model being used.
Define the configuration for your environment. In this example, we're creating an environment with short-term memory capabilities and configuring it to use an OpenAI model:

```python
from lyzr_agent_api.models.environment import EnvironmentConfig, FeatureConfig

environment_config = EnvironmentConfig(
    name="Test Environment",
    features=[
        FeatureConfig(
            type="SHORT_TERM_MEMORY",
            config={},
            priority=0,
        )
    ],
    tools=[],
    llm_config={
        "provider": "openai",
        "model": "gpt-4o-mini",
        "config": {
            "temperature": 0.5,
            "top_p": 0.9,
        },
        "env": {
            "OPENAI_API_KEY": "your-openai-api-key"
        }
    },
)
environment = client.create_environment_endpoint(json_body=environment_config) 
print(environment)
# The response will include the environment ID, e.g. {'environment_id': '6wjbwhekndjxxxxx'}
```

## 4. Creating an Agent

Once the environment is set up, create an agent within that environment. The agent uses the environment ID to operate and can be customized with a system prompt and a description:

```python
from lyzr_agent_api.models.agents import AgentConfig

agent_config = AgentConfig(
    env_id="environment-id",  # Replace with the actual environment ID
    system_prompt="This is a system prompt.",
    name="Test Agent",
    agent_description="Description of the test agent",
)
agent = client.create_agent_endpoint(json_body=agent_config)
print(agent)
# The response will include the agent ID, e.g. {'agent_id': '66fcghvhxxxxxx'}
```

## 5. Interact with the Agent

After creating the agent, you can initiate a chat session with it. Provide the user ID, agent ID, and a message to start the conversation:

```python
from lyzr_agent_api.models.chat import ChatRequest

response = client.chat_with_agent(
    json_body=ChatRequest(
        user_id="user-id",
        agent_id="agent-id",  # Replace with the actual agent ID
        message="Hello",
        session_id="session-id",
    )
)

print(response)
```

## Support

If you have any questions or need further assistance, please open an issue in this repository or contact support.

## Contact
For queries, reach us at contact@lyzr.ai