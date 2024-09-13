from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union

import httpx
@dataclass
class Session:
    user_id: str
    metadata: Any

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Session:
        return cls(
            user_id=data["user_id"],
            metadata=data["metadata"],
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "user_id": self.user_id,
            "metadata": self.metadata,
        }