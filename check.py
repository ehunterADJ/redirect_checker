import requests

responses = requests.get("https://google.com/")
print(responses.url)
if responses.url == "https://www.google1.com/":
    print("URL matches")
else:
    exit(1)
print("hello 2")
