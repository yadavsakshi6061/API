import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

response = requests.post(url, json=data)
if response.status_code == 201:
    print("POST request successful")
    print("Response data")
    print(response.json())
else:
    print("POST request failed", response.status_code)
