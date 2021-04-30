import requests

responses = requests.get("https://google.com/")
print(responses.url)
if responses.url == "https://www.google.com/":
    print("URL matches")
else:
    print("URL does not match")
print("hello")
