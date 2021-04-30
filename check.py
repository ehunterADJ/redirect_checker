import requests

responses = requests.get("http://google.com")
print(responses.url)
for response in responses.history:
    print(response.url)
