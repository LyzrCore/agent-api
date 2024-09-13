from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from .error_handling import HTTPValidationError
import httpx

@dataclass
class OpenAPISchema:
    openapi: Any

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> OpenAPISchema:
        return cls(
            openapi=data["openapi"],
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "openapi": self.openapi,
        }

def create_tools_endpoint(
        self,
        user_id: str,
        *,
        json_body: OpenAPISchema,
) -> Any:
    """Create new tools from an OpenAPI schema.

    Args:
        schema: The OpenAPI schema.
        user_id: The ID of the user creating the tools.

    Returns:
        tool_ids: IDs of the created tools.
    """
    url = f"{self._base_url}/v2/tool"
    params = {
        "user_id": user_id,
    }

    response = httpx.post(
        url=url,
        headers=self._headers,
        params=params,
        json=json_body.to_dict(),
        timeout=self._timeout,
    )

    if response.status_code == 200:
        return response.json()
    if response.status_code == 422:
        return HTTPValidationError.from_dict(response.json())
    response.raise_for_status()