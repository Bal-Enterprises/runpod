import requests
import os

url = os.environ["BAL_ENT_SERVER_URL"]
port = os.environ["BAL_ENT_SERVER_PORT"]


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


sendGetRequest()
sendPostRequest()
