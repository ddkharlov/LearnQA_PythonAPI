import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
first_response = response.history[0]
second_response = response

print(response.url)
print(response.history)
