from typing import Any
import httpx


def fetch_api_response(url: str) -> dict[str, Any]:
    response = httpx.get(url)
    return response.json()
