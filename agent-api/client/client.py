from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union

import httpx
from .models.agents import AgentConfig
from .models.chat import ChatRequest
from .models.environment import EnvironmentConfig,FeatureConfig
from .models.error_handling import HTTPValidationError, ValidationError
from .models.session import Session
from .models.task import TaskResponse,TaskStatus
from .models.user import UserCreate,UserUpdate
from .models.tools import OpenAPISchema


class AgentAPI:
    def __init__(
        self,
        *,
        base_url: str = "https://agent.api.lyzr.app",
        x_api_key: str,
        timeout: Optional[float] = None,
    ) -> None:
        self._base_url = base_url
        self._timeout = timeout
        self._headers = {
            "accept": "application/json",
            "x-api-key": x_api_key,
        }

    def chat_with_agent(
        self,
        *,
        json_body: ChatRequest,
    ) -> Any:
        """Chat with an agent.

        Args:
            json_body (ChatRequest): Details of the chat request including user ID,
                agent ID, session ID, and the message.

        Returns:
            Any: The agent's response to the chat message.
        """
        url = f"{self._base_url}/v2/chat/"

        response = httpx.post(
            url=url,
            headers=self._headers,
            json=json_body.to_dict(),
            timeout=self._timeout,
        )

        if response.status_code == 200:
            return response.json()
        if response.status_code == 422:
            return HTTPValidationError.from_dict(response.json())
        response.raise_for_status()

    def stream_chat_with_agent(
        self,
        *,
        json_body: ChatRequest,
    ) -> Any:
        """Stream chat with an agent.

        Args:
            json_body (ChatRequest): Details of the chat request including user ID,
                agent ID, session ID, and the message.

        Returns:
            Any: The agent's response to the chat message.
        """
        url = f"{self._base_url}/v2/stream/"

        response = httpx.post(
            url=url,
            headers=self._headers,
            json=json_body.to_dict(),
            timeout=self._timeout,
        )

        if response.status_code == 200:
            return response.json()
        if response.status_code == 422:
            return HTTPValidationError.from_dict(response.json())
        response.raise_for_status()

    def create_chat_task(
        self,
        *,
        json_body: ChatRequest,
    ) -> TaskResponse:
        """Create Chat Task"""
        url = f"{self._base_url}/v2/task/"

        response = httpx.post(
            url=url,
            headers=self._headers,
            json=json_body.to_dict(),
            timeout=self._timeout,
        )

        if response.status_code == 200:
            return TaskResponse.from_dict(response.json())
        if response.status_code == 422:
            return HTTPValidationError.from_dict(response.json())
        response.raise_for_status()

    def get_task_status(
        self,
        task_id: str,
    ) -> TaskStatus:
        """Get Task Status"""
        url = f"{self._base_url}/v2/task/{task_id}"

        response = httpx.get(
            url=url,
            headers=self._headers,
            timeout=self._timeout,
        )

        if response.status_code == 200:
            return TaskStatus.from_dict(response.json())
        if response.status_code == 422:
            return HTTPValidationError.from_dict(response.json())
        response.raise_for_status()

    def create_environment_endpoint(
        self,
        *,
        json_body: EnvironmentConfig,
    ) -> Any:
        """Create Environment Endpoint

        ### Environment Structure

        ### 1. Features/Modules
        Modules can be classified into two types: sync and background.

        #### Sync Modules
        - **Execution**: Runs in series during the message processing pipeline.
        - **Capabilities**: Can mutate the message stream.
        - **Access**: Read/Write access to the message stream.

        #### Background Modules
        - **Execution**: Runs in the background during the message processing pipeline.
        - **Capabilities**: Cannot mutate the message stream.
        - **Access**: Read-only access to the message stream.

        #### Available Modules

        |Module                       | Type        | Description                                                                 |
        |-----------------------------|-------------|-----------------------------------------------------------------------------|
        | SELF_REFLECTION             | SYNC        | Enables self-reflection capabilities for the agent, either by using the same model or a different model. |
        | OPEN_AI_RETRIEVAL_ASSISTANT | SYNC        | Offers retrieval capabilities using OpenAI's retriever.                      |
        | TOOL_CALLING                | SYNC        | Allows API tool calling. The agent can call any registered OpenAPI schema-supported API. |
        | KNOWLEDGE_BASE              | SYNC        | Provides Lyzr RAG capabilities with fully customizable retriever configurations. |
        | LONG_TERM_MEMORY            | SYNC        | Provides long contextual memory using multiple retrieval and summarization strategies. |
        | SHORT_TERM_MEMORY           | SYNC        | Provides short contextual memory for a configurable number of messages (n), determining how many messages to fetch per inference. |
        | STRUCTURED_MEMORY           | Background  | Acts as a structured JSON memory collector, storing structured information during conversations or task processes. |
        | LOGGING                     | Background  | Acts as a structured JSON memory collector, storing structured information during conversations or task processes. |
        | HUMANIZER                   | SYNC        | Humanizes the output of the agent.       |


        ### 2. Tools
        Tools are external APIs that an agent can utilize. To register a tool, provide an
        OpenAPI schema. The generated API ID can be used to configure tools for the agent.
        - **Note:** Tools are only accessible if the tool calling module is enabled.

        ### 3. llm_api_key
        The standard OpenAI API key.
        """
        url = f"{self._base_url}/v2/environment"

        response = httpx.post(
            url=url,
            headers=self._headers,
            json=json_body.to_dict(),
            timeout=self._timeout,
        )

        if response.status_code == 200:
            return response.json()
        if response.status_code == 422:
            return HTTPValidationError.from_dict(response.json())
        response.raise_for_status()

    def get_environments_endpoint(
        self,
    ) -> Any:
        """Get the environment details for a given agent.

        Args:
            agent_id: ID of the agent.

        Returns:
            environment: Details of the environment.
        """
        url = f"{self._base_url}/v2/environments"

        response = httpx.get(
            url=url,
            headers=self._headers,
            timeout=self._timeout,
        )

        if response.status_code == 200:
            return response.json()
        response.raise_for_status()

    def update_environment_endpoint(
        self,
        env_id: str,
        *,
        json_body: EnvironmentConfig,
    ) -> Any:
        """Update an existing environment.

        Args:
            env_id: ID of the environment to update.
            env_config: Updated configuration details for the environment.

        Returns:
            message: Confirmation message.
        """
        url = f"{self._base_url}/v2/environment/{env_id}"

        response = httpx.put(
            url=url,
            headers=self._headers,
            json=json_body.to_dict(),
            timeout=self._timeout,
        )

        if response.status_code == 200:
            return response.json()
        if response.status_code == 422:
            return HTTPValidationError.from_dict(response.json())
        response.raise_for_status()

    def get_environment_by_id(
        self,
        env_id: str,
    ) -> Any:
        """Get the environment details by environment ID.

        Args:
            env_id: ID of the environment.

        Returns:
            EnvironmentResponse: The environment details.
        """
        url = f"{self._base_url}/v2/environment/{env_id}"

        response = httpx.get(
            url=url,
            headers=self._headers,
            timeout=self._timeout,
        )

        if response.status_code == 200:
            return response.json()
        if response.status_code == 422:
            return HTTPValidationError.from_dict(response.json())
        response.raise_for_status()

    def delete_environment_by_id(
        self,
        env_id: str,
    ) -> Any:
        """Delete the environment by environment ID.

        Args:
            env_id: ID of the environment.

        Returns:
            Message indicating the environment has been deleted.
        """
        url = f"{self._base_url}/v2/environment/{env_id}"

        response = httpx.delete(
            url=url,
            headers=self._headers,
            timeout=self._timeout,
        )

        if response.status_code == 200:
            return response.json()
        if response.status_code == 422:
            return HTTPValidationError.from_dict(response.json())
        response.raise_for_status()

    def create_agent_endpoint(
        self,
        *,
        json_body: AgentConfig,
    ) -> Any:
        """Create a new agent.

        Args:
            agent_config: Configuration details for the agent.

        Returns:
            agent_id: ID of the created agent.
        """
        url = f"{self._base_url}/v2/agent"

        response = httpx.post(
            url=url,
            headers=self._headers,
            json=json_body.to_dict(),
            timeout=self._timeout,
        )

        if response.status_code == 200:
            return response.json()
        if response.status_code == 422:
            return HTTPValidationError.from_dict(response.json())
        response.raise_for_status()

    def get_agents_endpoint(
        self,
    ) -> Any:
        """Get the details of a specific agent.

        Args:
            agent_id: ID of the agent.

        Returns:
            agent_data: Details of the agent.
        """
        url = f"{self._base_url}/v2/agents"

        response = httpx.get(
            url=url,
            headers=self._headers,
            timeout=self._timeout,
        )

        if response.status_code == 200:
            return response.json()
        response.raise_for_status()

    def update_agent_endpoint(
        self,
        agent_id: str,
        *,
        json_body: AgentConfig,
    ) -> Any:
        """Update an existing agent.

        Args:
            agent_id: ID of the agent to update.
            agent_config: Updated configuration details for the agent.

        Returns:
            message: Confirmation message.
        """
        url = f"{self._base_url}/v2/agent/{agent_id}"

        response = httpx.put(
            url=url,
            headers=self._headers,
            json=json_body.to_dict(),
            timeout=self._timeout,
        )

        if response.status_code == 200:
            return response.json()
        if response.status_code == 422:
            return HTTPValidationError.from_dict(response.json())
        response.raise_for_status()

    def get_agent_endpoint(
        self,
        agent_id: str,
    ) -> Any:
        """Get the details of a specific agent.

        Args:
            agent_id: ID of the agent.

        Returns:
            agent_data: Details of the agent.
        """
        url = f"{self._base_url}/v2/agent/{agent_id}"

        response = httpx.get(
            url=url,
            headers=self._headers,
            timeout=self._timeout,
        )

        if response.status_code == 200:
            return response.json()
        if response.status_code == 422:
            return HTTPValidationError.from_dict(response.json())
        response.raise_for_status()

    def delete_agent_by_id(
        self,
        agent_id: str,
    ) -> Any:
        """Delete the agent by agent ID.

        Args:
            agent_id: ID of the agent.

        Returns:
            Message indicating the agent has been deleted.
        """
        url = f"{self._base_url}/v2/agent/{agent_id}"

        response = httpx.delete(
            url=url,
            headers=self._headers,
            timeout=self._timeout,
        )

        if response.status_code == 200:
            return response.json()
        if response.status_code == 422:
            return HTTPValidationError.from_dict(response.json())
        response.raise_for_status()

    def create_tools_endpoint(
        self,
        user_id: str,
        *,
        json_body: OpenAPISchema,
    ) -> Any:
        """Create new tools from an OpenAPI schema.

        Args:
            schema: The OpenAPI schema.
            user_id: The ID of the user creating the tools.

        Returns:
            tool_ids: IDs of the created tools.
        """
        url = f"{self._base_url}/v2/tool"
        params = {
            "user_id": user_id,
        }

        response = httpx.post(
            url=url,
            headers=self._headers,
            params=params,
            json=json_body.to_dict(),
            timeout=self._timeout,
        )

        if response.status_code == 200:
            return response.json()
        if response.status_code == 422:
            return HTTPValidationError.from_dict(response.json())
        response.raise_for_status()

    def get_activities_by_user_session(
        self,
        user_id: str,
        session_id: str,
    ) -> List[Any]:
        """Get all activities for a specific user and session.

        Args:
            user_id: ID of the user.
            session_id: ID of the session.

        Returns:
            List of activities.
        """
        url = f"{self._base_url}/v2/activities"
        params = {
            "user_id": user_id,
            "session_id": session_id,
        }

        response = httpx.get(
            url=url,
            headers=self._headers,
            params=params,
            timeout=self._timeout,
        )

        if response.status_code == 200:
            return response.json()
        if response.status_code == 422:
            return HTTPValidationError.from_dict(response.json())
        response.raise_for_status()

    def create_user_endpoint(
        self,
        *,
        json_body: UserCreate,
    ) -> Any:
        """Create User Endpoint"""
        url = f"{self._base_url}/v1/users/"

        response = httpx.post(
            url=url,
            headers=self._headers,
            json=json_body.to_dict(),
            timeout=self._timeout,
        )

        if response.status_code == 200:
            return response.json()
        if response.status_code == 422:
            return HTTPValidationError.from_dict(response.json())
        response.raise_for_status()

    def get_user_endpoint(
        self,
        user_id: str,
    ) -> Any:
        """Get User Endpoint"""
        url = f"{self._base_url}/v1/users/{user_id}"

        response = httpx.get(
            url=url,
            headers=self._headers,
            timeout=self._timeout,
        )

        if response.status_code == 200:
            return response.json()
        if response.status_code == 422:
            return HTTPValidationError.from_dict(response.json())
        response.raise_for_status()

    def update_user_endpoint(
        self,
        user_id: str,
        *,
        json_body: UserUpdate,
    ) -> Any:
        """Update User Endpoint"""
        url = f"{self._base_url}/v1/users/{user_id}"

        response = httpx.put(
            url=url,
            headers=self._headers,
            json=json_body.to_dict(),
            timeout=self._timeout,
        )

        if response.status_code == 200:
            return response.json()
        if response.status_code == 422:
            return HTTPValidationError.from_dict(response.json())
        response.raise_for_status()

    def get_user_sessions_endpoint(
        self,
        user_id: str,
    ) -> Any:
        """Get User Sessions Endpoint"""
        url = f"{self._base_url}/v1/users/{user_id}/sessions"

        response = httpx.get(
            url=url,
            headers=self._headers,
            timeout=self._timeout,
        )

        if response.status_code == 200:
            return response.json()
        if response.status_code == 422:
            return HTTPValidationError.from_dict(response.json())
        response.raise_for_status()

    def create_session_endpoint(
        self,
        *,
        json_body: Session,
    ) -> Any:
        """Create Session Endpoint"""
        url = f"{self._base_url}/v1/sessions/"

        response = httpx.post(
            url=url,
            headers=self._headers,
            json=json_body.to_dict(),
            timeout=self._timeout,
        )

        if response.status_code == 200:
            return response.json()
        if response.status_code == 422:
            return HTTPValidationError.from_dict(response.json())
        response.raise_for_status()

    def get_session_endpoint(
        self,
        session_id: str,
        timeout: Optional[int] = 30,
    ) -> Any:
        """Get Session Endpoint"""
        url = f"{self._base_url}/v1/sessions/{session_id}"
        params = {
            "timeout": timeout,
        }

        response = httpx.get(
            url=url,
            headers=self._headers,
            params=params,
            timeout=self._timeout,
        )

        if response.status_code == 200:
            return response.json()
        if response.status_code == 422:
            return HTTPValidationError.from_dict(response.json())
        response.raise_for_status()

    def update_session_endpoint(
        self,
        session_id: str,
        *,
        json_body: Session,
    ) -> Any:
        """Update Session Endpoint"""
        url = f"{self._base_url}/v1/sessions/{session_id}"

        response = httpx.put(
            url=url,
            headers=self._headers,
            json=json_body.to_dict(),
            timeout=self._timeout,
        )

        if response.status_code == 200:
            return response.json()
        if response.status_code == 422:
            return HTTPValidationError.from_dict(response.json())
        response.raise_for_status()

    def get_session_history_endpoint(
        self,
        session_id: str,
        unix: Optional[bool] = False,
    ) -> Any:
        """Get Session History Endpoint"""
        url = f"{self._base_url}/v1/sessions/{session_id}/history"
        params = {
            "unix": unix,
        }

        response = httpx.get(
            url=url,
            headers=self._headers,
            params=params,
            timeout=self._timeout,
        )

        if response.status_code == 200:
            return response.json()
        if response.status_code == 422:
            return HTTPValidationError.from_dict(response.json())
        response.raise_for_status()

    def get_session_payload_endpoint(
        self,
        session_id: str,
    ) -> Any:
        """Get Session Payload Endpoint"""
        url = f"{self._base_url}/v1/sessions/{session_id}/summary"

        response = httpx.get(
            url=url,
            headers=self._headers,
            timeout=self._timeout,
        )

        if response.status_code == 200:
            return response.json()
        if response.status_code == 422:
            return HTTPValidationError.from_dict(response.json())
        response.raise_for_status()

    def cors_(
        self,
        full_path: str,
    ) -> Any:
        """Cors"""
        url = f"{self._base_url}/{full_path}"

        response = httpx.options(
            url=url,
            headers=self._headers,
            timeout=self._timeout,
        )

        if response.status_code == 200:
            return response.json()
        if response.status_code == 422:
            return HTTPValidationError.from_dict(response.json())
        response.raise_for_status()

    def health_check(
        self,
    ) -> Any:
        """Health Check"""
        url = f"{self._base_url}/health"

        response = httpx.get(
            url=url,
            headers=self._headers,
            timeout=self._timeout,
        )

        if response.status_code == 200:
            return response.json()
        response.raise_for_status()