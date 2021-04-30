import requests

responses = requests.get("http://google.com")

for response in responses.history:
    print(response.url)
