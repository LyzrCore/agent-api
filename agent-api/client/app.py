from client import AgentAPI
from models.chat import ChatRequest

api = AgentAPI(base_url="https://agent.api.lyzr.app", x_api_key="lyzr-V51VDLHozVHdcjJLXAjrzMvP")

response = api.chat_with_agent(
    json_body=ChatRequest(
        user_id="7422",
        agent_id="66d9385117901bc73565f022",
        message="Hello, agent!",
    )
)

print(response)



