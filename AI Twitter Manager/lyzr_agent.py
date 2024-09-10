import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
LYZR_URL = os.getenv("LYZR_URL")

class LyzrAgent:
    def __init__(self, api_key, llm_api_key):
        self.url = str(LYZR_URL)
        self.headers = {
            "accept": "application/json",
            "x-api-key": api_key
        }
        self.llm_api_key = llm_api_key

    def create_environment(self, name, features, tools):
        payload = json.dumps({
            "name": name,
            "features": features,
            "tools": tools,
            "llm_api_key": self.llm_api_key
        })

        url = self.url + "environment"

        response = requests.post(url, headers=self.headers, data=payload)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None

    def create_agent(self, env_id, system_prompt, name):
        payload = json.dumps({
            "env_id": env_id,
            "system_prompt": system_prompt,
            "name": name,
            "agent_persona": "",
            "agent_instructions": "",
            "agent_description": ""
        })

        url = self.url + "agent"

        response = requests.post(url, headers=self.headers, data=payload)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None

    def send_message(self, agent_id, user_id, session_id, message):
        payload = json.dumps({
            "user_id": user_id,
            "agent_id": agent_id,
            "session_id": session_id,
            "message": message
        })

        url = self.url + "chat/"

        response = requests.post(url, headers=self.headers, data=payload)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None

    def create_task(self, agent_id, session_id, input_message):
        payload = json.dumps({
            "agent_id": agent_id,
            "session_id": session_id,
            "input": input_message
        })

        url = self.url + "task"

        response = requests.post(url, headers=self.headers, data=payload)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None