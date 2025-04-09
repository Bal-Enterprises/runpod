import runpod
import time
import requests
import os
from openai import OpenAI

url = os.environ["BAL_ENT_SERVER_URL"]
port = os.environ["BAL_ENT_SERVER_PORT"]
api_key = os.environ["BAL_ENT_API_KEY"]
model_version = os.environ["BAL_ENT_MODEL"]

def sendGetRequest():
    try:
        fullpath = f"{url}:{port}/get"
        response = requests.get(fullpath)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        print("Request successful!")
        print("Status code:", response.status_code)
        print("Response body:", response.text)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


def sendPostRequest():
    # URL to send the POST request to
    try:
        fullpath = f"{url}:{port}/post"
        data = {"key1": "value1", "key2": "value2"}

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer YOUR_ACCESS_TOKEN",
        }

        response = requests.post(fullpath, data=data, headers=headers)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    # Check the status code and response content
    if response.status_code == 200:
        print("Request was successful.")
        print("Response content:", response.text)
    else:
        print(f"Request failed with status code: {response.status_code}")


def queryModel(prompt):

    fullpath = f"{url}:{port}/v1"
    client = OpenAI(
        base_url=fullpath,
        api_key="token-abc123",
    )

    completion = client.chat.completions.create(
        model=model_version,
        messages=[
            {"role": "user", "content": "Hello!"}
        ]
    )

    print(completion.choices[0].message)
    return completion.choices[0].message

def handler(event):
    input = event["message"]
    result = queryModel(input)
    return result


    result = instruction.replace(instruction.split()[0], "created", 1)
    return result


if __name__ == "__main__":
    runpod.serverless.start({"handler": handler})

