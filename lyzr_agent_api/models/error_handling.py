from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union


@dataclass
class HTTPValidationError:
    detail: Optional[List[ValidationError]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> HTTPValidationError:
        return cls(
            detail=[ValidationError.from_dict(item) for item in data.get("detail", [])],
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "detail": [item.to_dict() for item in self.detail] if self.detail else None,
        }

@dataclass
class ValidationError:
    loc: List[Union[str, int]]
    msg: str
    type: str

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> ValidationError:
        return cls(
            loc=data["loc"],
            msg=data["msg"],
            type=data["type"],
        )


        return {
            "loc": self.loc,
            "msg": self.msg,
            "type": self.type,
        }