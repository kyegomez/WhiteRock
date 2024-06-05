import time
import os
from typing import Optional

import requests
from dotenv import load_dotenv

from whiterock.prompts import analyst_caller_agent

load_dotenv()


def fetch_bank_statements():
    url = "https://api.mercury.com/api/v1/account/id/statements"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.getenv('MERCURY_API_TOKEN')}",
    }

    response = requests.get(url, headers=headers)

    return response.text


def fetch_data_to_file(
    file_path: str, token: Optional[str] = None
) -> None:
    url = "https://api.mercury.com/api/v1/accounts"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token or os.getenv('MERCURY_API_TOKEN')}",
    }

    response = requests.get(url, headers=headers)
    print(response)

    if response.status_code == 200:
        with open(file_path, "w") as file:
            file.write(response.text)
        print("Data fetched and saved successfully.")
    else:
        print(
            f"Failed to fetch data. Status code: {response.status_code}"
        )


# # Example usage
# fetch_data_to_file("mercury_accounts.json")
# fetch_data_to_file("mercury_accounts.json")


def call_api(
    phone_number: str = "+17866955339",
    prompt: str = analyst_caller_agent(),
    max_duration: int = 160,
) -> None:
    """
    Makes an API call to create a new call using the Bland.ai API.
    """
    headers = {"Authorization": os.getenv("BLAND_API_KEY")}

    # Data
    # Data
    data = {
        "phone_number": phone_number,  # "+16693249705",
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
        "record": False,
        "amd": False,
        "interruption_threshold": 100,
        "temperature": None,
        "transfer_list": {},
        "metadata": {},
        "pronunciation_guide": [],
        "start_time": None,
        "request_data": {},
        "tools": [],
        "webhook": None,
        "calendly": {},
    }

    # API request
    response = requests.post(
        "https://api.bland.ai/v1/calls", json=data, headers=headers
    )

    output = response.json()
    return output.get("call_id")


def fetch_transcription(
    call_id: str, max_duration: int = None
) -> str:
    time.sleep(max_duration)
    headers = {"Authorization": os.getenv("BLAND_API_KEY")}

    # Fetch the transcript
    url = f"https://api.bland.ai/v1/calls/{call_id}"

    response = requests.get(url, headers=headers)

    output = response.json()

    # Get the transcript from the output
    # "transcripts": [
    #     {
    #         "id": 7395694,
    #         "created_at": "2024-04-27T23:51:28.568385+00:00",
    #         "text": "Hello?",
    #         "user": "user",
    #         "c_id": "d9cce3f3-23cf-4fa7-b62c-8be8119b8715",
    #         "status": null,
    #         "transcript_id": null
    #     },
    transcript = output.get("transcripts")

    # Create a loop to get all the transcripts
    if transcript:
        return "\n".join([t.get("text") for t in transcript])
    else:
        return "No transcripts found."


# # Call the function
# out = call_api(
#     prompt=analyst_caller_agent(),
#     phone_number="+17866955339",
#     max_duration=160,
# )

# # Transcription
# transcription = fetch_transcription(out)
# print(transcription)
