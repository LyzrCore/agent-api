from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union

import httpx

@dataclass
class ChatRequest:
    user_id: str
    agent_id: str
    message: str
    session_id: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> ChatRequest:
        return cls(
            user_id=data["user_id"],
            agent_id=data["agent_id"],
            message=data["message"],
            session_id=data.get("session_id"),
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "user_id": self.user_id,
            "agent_id": self.agent_id,
            "message": self.message,
            "session_id": self.session_id,
        }