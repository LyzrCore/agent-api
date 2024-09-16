from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class AgentConfig:
    env_id: str
    system_prompt: str
    name: str
    agent_description: str

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> AgentConfig:
        return cls(
            env_id=data["env_id"],
            system_prompt=data["system_prompt"],
            name=data["name"],
            agent_description=data["agent_description"],
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "env_id": self.env_id,
            "system_prompt": self.system_prompt,
            "name": self.name,
            "agent_description": self.agent_description,
        }
