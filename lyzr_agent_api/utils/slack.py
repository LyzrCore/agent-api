from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk import WebClient
from slack_bolt import App
import os
from lyzr_agent_api.client import AgentAPI
from lyzr_agent_api.models.chat import ChatRequest


class SlackLyzrBot:
    def __init__(self, slack_bot_token, slack_app_token, lyzr_api_key, agent_id):
        # Initialize Slack App and WebClient
        self.app = App(token=slack_bot_token)
        self.client = WebClient(slack_bot_token)

        # Initialize Lyzr Agent API
        self.lyzr_client = AgentAPI(x_api_key=lyzr_api_key)
        self.agent_id = agent_id

        # Register event handlers
        self.app.event("app_mention")(self.handle_app_mention)

    def handle_app_mention(self, body, logger):
        """Handles 'app_mention' events."""
        try:
            # Extract the prompt from the Slack message
            prompt = str(body["event"]["text"]).split(">")[1].strip()

            # Chat with the Lyzr agent
            response = self.lyzr_client.chat_with_agent(
                json_body=ChatRequest(
                    user_id=body["event"]["user"],
                    agent_id=self.agent_id,
                    message=prompt,
                    session_id=body["event"]["channel"],
                )
            )

            # Post the agent's response back to Slack
            self.client.chat_postMessage(
                channel=body["event"]["channel"],
                thread_ts=body["event"]["event_ts"],
                text=f"{response['response']}"
            )
        except Exception as e:
            logger.error(f"Error handling app mention: {e}")
            self.client.chat_postMessage(
                channel=body["event"]["channel"],
                thread_ts=body["event"]["event_ts"],
                text="Sorry, something went wrong while processing your request. :cry:"
            )

    def start(self, slack_app_token):
        """Starts the Slack bot."""
        handler = SocketModeHandler(self.app, slack_app_token)
        handler.start()