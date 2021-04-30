import requests

responses = requests.get("https://google.com/")
if responses.url == "https://www.google1.com/":
    print("URL matches")
else:
    exit(1)
