from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, ValidationError

import httpx

@dataclass
class EnvironmentConfig:
    name: str
    features: List[FeatureConfig]
    tools: List[str]
    llm_config: Any

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> EnvironmentConfig:
        return cls(
            name=data["name"],
            features=[FeatureConfig.from_dict(item) for item in data["features"]],
            tools=data["tools"],
            llm_config=data["llm_config"],
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "features": [item.to_dict() for item in self.features],
            "tools": self.tools,
            "llm_config": self.llm_config,
        }

@dataclass
class FeatureConfig:
    type: str
    config: []
    priority: int = 0

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> FeatureConfig:
        return cls(
            type=data["type"],
            config=data.get("config", {}),
            priority=data.get("priority", 0),
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": self.type,
            "config": self.config,
            "priority": self.priority,
        }