from client import *
from client import AgentAPI
# from unittest.mock import patch, MagicMock

import pytest

@pytest.fixture
def client() -> AgentAPI:
    return AgentAPI(
        base_url="https://agent.api.lyzr.app",
        x_api_key="Lyzr-Agent-API-KEY",
        timeout=30.0,
    )

def test_chat_with_agent(client: AgentAPI) -> None:
    """Test case for chat_with_agent

    Chat with an agent.
    """
    json_body = ChatRequest(
        user_id="test",
        agent_id="test",
        message="Hello",
        session_id="123",
    )
    response = client.chat_with_agent(
        json_body=json_body,
    )
    assert response is not None


# def test_stream_chat_with_agent(client: AgentAPI) -> None:
#     """Test case for stream_chat_with_agent
#
#     Stream chat with an agent.
#     """
#     json_body = ChatRequest(
#         user_id="7422",
#         agent_id="66d6918ba06b3bfd70c747f7",
#         message="Hii",
#         session_id="123",
#     )
#     response = client.stream_chat_with_agent(
#         json_body=json_body,
#     )
#     assert response is not None


def test_create_chat_and_get_status(client: AgentAPI) -> None:
    """Test case for creating a chat task and getting its status"""

    # Create Chat Task
    json_body = ChatRequest(
        user_id="test",
        agent_id="test",
        message="hi",
        session_id="test",
    )
    response_create = client.create_chat_task(
        json_body=json_body,
    )

    # Ensure the chat task creation was successful
    assert response_create is not None
    assert response_create.task_id is not None  # Assuming the response contains a 'task_id'

    # Now get the status of the created task
    response_status = client.get_task_status(
        task_id=response_create.task_id,  # Use the task_id from the create response
    )

    # Ensure the task status retrieval was successful
    assert response_status is not None
    assert response_status.status is not None  # Assuming the response contains a 'status'

    # Additional asserts can be added here to check specific status or other properties


def test_create_environment_endpoint(client: AgentAPI) -> None:
    """Test case for create_environment_endpoint

    Create Environment Endpoint
    """
    json_body = EnvironmentConfig(
        name="Test Environment",
        features=[
            FeatureConfig(
                type="SHORT_TERM_MEMORY",
                config={},
                priority=0,
            )
        ],
        tools=[""],
        llm_config={"provider": "openai",
        "model": "gpt-4o-mini",
        "config": {
            "temperature": 0.5,
            "top_p": 0.9
        },
        "env": {
            "OPENAI_API_KEY": "OPENAI-API-KEY"
        }},
    )
    response = client.create_environment_endpoint(
        json_body=json_body,
    )
    assert response is not None


def test_get_environments_endpoint(client: AgentAPI) -> None:
    """Test case for get_environments_endpoint

    Get Environments Endpoint
    """
    response = client.get_environments_endpoint()
    assert response is not None


def test_update_environment_endpoint(client: AgentAPI) -> None:
    """Test case for update_environment_endpoint

    Update Environment Endpoint
    """
    json_body = EnvironmentConfig(
        name="TEST ENv",
        features=[
            FeatureConfig(
                type="SHORT_TERM_MEMORY",
                config={},
                priority=0,
            )
        ],
        tools=[""],
        llm_config={"provider": "openai",
        "model": "gpt-4o-mini",
        "config": {
            "temperature": 0.5,
            "top_p": 0.9
        },
        "env": {
            "OPENAI_API_KEY": "OPENAI-API-KEY"
        }},
    )
    response = client.update_environment_endpoint(
        env_id="env-id",
        json_body=json_body,
    )
    assert response is not None

def test_create_agent_endpoint(client: AgentAPI) -> None:
    """Test case for create_agent_endpoint

    Create an Agent Endpoint
    """
    json_body = AgentConfig(
        env_id="env-id",  # Example environment ID
        system_prompt="This is a system prompt.",
        name="Test Agent",
        agent_description="Description of the test agent",
    )
    response = client.create_agent_endpoint(
        json_body=json_body,
    )
    # Ensure the agent creation was successful
    assert response is not None # Assuming the response contains an 'agent_id'


def test_get_agents_endpoint(client: AgentAPI) -> None:
    """Test case for get_agents_endpoint

    Get Agents Endpoint
    """
    response = client.get_agents_endpoint()

    # Ensure the agent list retrieval was successful
    assert response is not None # Assuming the response contains a list of 'agents'


def test_update_agent_endpoint(client: AgentAPI) -> None:
    """Test case for update_agent_endpoint

    Update an Agent Endpoint
    """
    agent_id = "agent-id"  # Example agent ID to update
    json_body = AgentConfig(
        env_id="env-id",  # Same environment ID
        system_prompt="Updated system prompt.",
        name="Updated Agent Name",
        agent_description="Updated description for the test agent",
    )
    response = client.update_agent_endpoint(
        agent_id=agent_id,
        json_body=json_body
    )
    # Ensure the agent update was successful
    assert response is not None # Assuming the response contains a 'message'


def test_delete_agent_by_id(client: AgentAPI) -> None:
    """Test case for delete_agent_by_id

    Delete an Agent by ID
    """
    agent_id = "agent-id"  # Example agent ID to delete
    response = client.delete_agent_by_id(
        agent_id=agent_id
    )
    # Ensure the agent deletion was successful
    assert response is not None

def test_get_activities_by_user_session(client: AgentAPI) -> None:
    """
    Test case for get_activities_by_user_session

    Get all activities for a specific user and session.
    """
    user_id = "test"
    session_id = "test"

    response = client.get_activities_by_user_session(
        user_id=user_id,
        session_id=session_id,
    )

    assert response is not None

def test_create_user_endpoint(client: AgentAPI) -> None:
    """Test case for create_user_endpoint

    Create User Endpoint
    """
    # Adjust the UserCreate initialization based on the provided parameters
    json_body = UserCreate(
        user_id="test",
        email="testuser@example.com",
        first_name="Test",
        last_name="User",
        metadata={}
    )

    # Call the create_user_endpoint method on the client
    response = client.create_user_endpoint(
        json_body=json_body,
    )

    # Assertions to verify the response
    assert response is not None

def test_get_user_endpoint(client: AgentAPI) -> None:
    """Test case for get_user_endpoint

    Get User Endpoint
    """
    user_id = "test"

    response = client.get_user_endpoint(user_id=user_id)

    # Assertions to verify the response
    assert response is not None


def test_update_user_endpoint(client: AgentAPI) -> None:
    """Test case for update_user_endpoint

    Update User Endpoint
    """
    user_id = "test"

    json_body = UserUpdate(
        email="updateduser@example.com",
        first_name="Updated",
        last_name="User",
        metadata={"role": "admin"}  # Example metadata
    )

    response = client.update_user_endpoint(
        user_id=user_id,
        json_body=json_body,
    )

    # Assertions to verify the response
    assert response is not None

def test_get_user_sessions_endpoint(client: AgentAPI) -> None:
    """Test case for get_user_sessions_endpoint

    Get User Sessions Endpoint
    """
    user_id = "test"

    response = client.get_user_sessions_endpoint(user_id=user_id)

    # Assertions to verify the response
    assert response is not None

def test_create_session_endpoint(client: AgentAPI) -> None:
    """Test case for create_session_endpoint

    Create Session Endpoint
    """
    json_body = Session(
        user_id="testuser123",
        metadata={"description": "Test session"}
    )

    response = client.create_session_endpoint(
        json_body=json_body,
    )

    # Assertions to verify the response
    assert response is not None

def test_get_session_endpoint(client: AgentAPI) -> None:
    """Test case for get_session_endpoint

    Get Session Endpoint
    """
    session_id = "test"
    timeout = 30

    response = client.get_session_endpoint(session_id=session_id, timeout=timeout)

    # Assertions to verify the response
    assert response is not None


def test_update_session_endpoint(client: AgentAPI) -> None:
    """Test case for update_session_endpoint

    Update Session Endpoint
    """
    session_id = "test"

    json_body = Session(
        user_id="testuser123",
        metadata={"description": "Updated test session"}
    )

    response = client.update_session_endpoint(
        session_id=session_id,
        json_body=json_body,
    )

    # Assertions to verify the response
    assert response is not None

def test_get_session_payload_endpoint(client: AgentAPI) -> None:
    """Test case for get_session_payload_endpoint

    Get Session Payload Endpoint
    """
    session_id = "test"

    response = client.get_session_payload_endpoint(session_id=session_id)

    # Assertions to verify the response
    assert response is not None

def test_get_session_history_endpoint(client: AgentAPI) -> None:
    """Test case for get_session_history_endpoint

    Get Session History Endpoint
    """
    session_id = "test"
    unix = False

    response = client.get_session_history_endpoint(session_id=session_id, unix=unix)

    # Assertions to verify the response
    assert response is not None

def test_create_tools_endpoint(client: AgentAPI) -> None:
    """Test case for create_tools_endpoint

    Create new tools from an OpenAPI schema
    """
    user_id = "test"
    json_body = OpenAPISchema(
        {
            "openapi": "3.1.0",
            "info": {
                "title": "FastAPI",
                "description": "API for fetching webpage content.",
                "version": "0.1.0"
            },
            "paths": {
                "/fetch-content/": {
                    "post": {
                        "summary": "Fetch Content",
                        "description": "Fetches content from the specified webpage URL.",
                        "operationId": "fetch_content_fetch_content__post",
                        "parameters": [
                            {
                                "name": "webpage_url",
                                "in": "query",
                                "required": True,
                                "schema": {
                                    "type": "string",
                                    "title": "Webpage URL",
                                    "description": "The URL of the webpage from which to fetch content."
                                }
                            }
                        ],
                        "responses": {
                            "200": {
                                "description": "Content fetched successfully",
                                "content": {
                                    "application/json": {
                                        "schema": {
                                            "type": "object",
                                            "properties": {
                                                "content": {
                                                    "type": "string",
                                                    "description": "The content of the webpage."
                                                }
                                            }
                                        }
                                    }
                                }
                            },
                            "422": {
                                "description": "Validation Error",
                                "content": {
                                    "application/json": {
                                        "schema": {
                                            "$ref": "#/components/schemas/HTTPValidationError"
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "components": {
                "schemas": {
                    "HTTPValidationError": {
                        "type": "object",
                        "title": "HTTPValidationError",
                        "description": "Validation error response returned when the request fails validation.",
                        "properties": {
                            "detail": {
                                "type": "array",
                                "title": "Detail",
                                "description": "A list of validation errors.",
                                "items": {
                                    "$ref": "#/components/schemas/ValidationError"
                                }
                            }
                        }
                    },
                    "ValidationError": {
                        "type": "object",
                        "title": "ValidationError",
                        "description": "Details about a specific validation error.",
                        "properties": {
                            "loc": {
                                "type": "array",
                                "title": "Location",
                                "description": "The location of the error in the request data.",
                                "items": {
                                    "anyOf": [
                                        {
                                            "type": "string"
                                        },
                                        {
                                            "type": "integer"
                                        }
                                    ]
                                }
                            },
                            "msg": {
                                "type": "string",
                                "title": "Message",
                                "description": "A human-readable message describing the error."
                            },
                            "type": {
                                "type": "string",
                                "title": "Error Type",
                                "description": "The type of error encountered."
                            }
                        },
                        "required": ["loc", "msg", "type"]
                    }
                }
            },
            "servers": [
                {
                    "url": "https://fetch.example.com",
                    "description": "Fetch Content Server"
                }
            ]
        }

        # Add more components as needed
    )

    response = client.create_tools_endpoint(
        user_id=user_id,
        json_body=json_body,
    )

    # Assertions to verify the response
    assert response is not None