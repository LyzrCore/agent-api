from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional



@dataclass
class UserCreate:
    user_id: Optional[str] = None
    email: Optional[str] = "default@example.com"
    first_name: Optional[str] = "First Name"
    last_name: Optional[str] = "Last Name"
    metadata: Optional[Any] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> UserCreate:
        return cls(
            user_id=data.get("user_id"),
            email=data.get("email", "default@example.com"),
            first_name=data.get("first_name", "First Name"),
            last_name=data.get("last_name", "Last Name"),
            metadata=data.get("metadata"),
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "user_id": self.user_id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "metadata": self.metadata,
        }

@dataclass
class UserUpdate:
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    metadata: Optional[Any] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> UserUpdate:
        return cls(
            email=data.get("email"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            metadata=data.get("metadata"),
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "metadata": self.metadata,
        }