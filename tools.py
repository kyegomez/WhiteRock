import os
import requests
from whiterock.prompts import analyst_caller_agent


def call_api(
    phone_number: str = "+17866955339",
    prompt: str = None,
    max_duration: int = 160,
) -> None:
    """
    Makes an API call to create a new call using the Bland.ai API.
    """
    headers = {"Authorization": os.getenv("BLAND_API_KEY")}

    # Data
    data = {
        "phone_number": {phone_number},
        "from": None,
        "task": prompt,
        "model": "enhanced",
        "language": "en",
        "voice": "maya",
        "voice_settings": {},
        "local_dialing": False,
        "max_duration": max_duration,
        "answered_by_enabled": False,
        "wait_for_greeting": False,
        "record": True,
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
out = call_api(
    prompt=analyst_caller_agent(),
    phone_number=7866955339,
    max_duration=160,
)
print(out)
