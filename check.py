import requests

responses = requests.get("https://google.com/")
if responses.url == "https://www.google.com/":
    print("URL matches")
else:
    print("URL does not match)
print("hello")
