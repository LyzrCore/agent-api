
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional

@dataclass
class TaskResponse:
    task_id: str

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> TaskResponse:
        return cls(
            task_id=data["task_id"],
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "task_id": self.task_id,
        }

@dataclass
class TaskStatus:
    task_id: str
    status: str
    result: Optional[Any] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> TaskStatus:
        return cls(
            task_id=data["task_id"],
            status=data["status"],
            result=data.get("result"),
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "task_id": self.task_id,
            "status": self.status,
            "result": self.result,
        }