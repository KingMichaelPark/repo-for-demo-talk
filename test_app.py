from unittest.mock import patch

from app import main


@patch("lib.fetch_api_response", return_value={"id": 100})
def test_main_and_increment(mock_fetch_api_response):
    match main():
        case {"id": actual}:
            assert actual == 101
            mock_fetch_api_response.assert_called_once()
        case _:
            raise KeyError("Couldn't find id in the response")
