import requests
import json

url = "https://jsonplaceholder.typicode.com"

response = requests.get(url)
if response.status_code == 200:
    try:
        data = response.json()
        print("GET request successful")
        print(data)
    except json.decoder.JSONDecodeError as e:
        print("Failed to decode response content as JSON:", e)
        print("Response content:", response.text)
else:
    print("GET request failed:", response.status_code)
