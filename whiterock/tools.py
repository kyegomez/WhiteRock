import os
import requests
from typing import Dict, Any


def call_api(prompt: str = None) -> None:
    """
    Makes an API call to create a new call using the Bland.ai API.
    """
    headers = {"Authorization": os.getenv("BLAND_API_KEY")}

    # Data
    data: Dict[str, Any] = {
        "phone_number": "+",
        "from": None,
        "task": prompt,
        "model": "turbo",
        "language": "en",
        "voice": "maya",
        "voice_settings": {},
        "local_dialing": False,
        "max_duration": 12,
        "answered_by_enabled": False,
        "wait_for_greeting": False,
        "record": False,
        "amd": False,
        "interruption_threshold": 100,
        "temperature": None,
        "transfer_list": {"": ""},
        "metadata": {},
        "pronunciation_guide": [],
        "start_time": None,
        "request_data": {},
        "tools": [],
        "webhook": None,
        "calendly": {"url": "jdjd", "timezone": "America/Chicago"},
    }

    # API request
    response = requests.post(
        "https://api.bland.ai/v1/calls", json=data, headers=headers
    )
    # Handle the response here
    return response.json()


# Call the function
