from typing import Any
from lib import fetch_api_response


def incrememnt_response(response) -> dict[str, Any]:
    if response.get("id"):
        response["id"] += 1
    else:
        response["id"] = 1
    return response


def main():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    response = fetch_api_response(url)
    return incrememnt_response(response)


if __name__ == "__main__":
    main()
