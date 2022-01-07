import requests
import time
import json

payload = {"token": ""}
response_create_task = requests.get(" https://playground.learnqa.ru/ajax/api/longtime_job")

obj = json.loads(response_create_task.text)
payload["token"] = obj['token']
seconds = obj['seconds']

first_response_with_token = requests.get(" https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)
obj = json.loads(first_response_with_token.text)
assert obj['status'] == 'Job is NOT ready', 'Значение поля "status" некорректно'
time.sleep(seconds)

second_response_with_token = requests.get(" https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)
obj = json.loads(second_response_with_token.text)
assert obj['status'] == 'Job is ready', 'Значение поля "status" некорректно'
assert 'result' in obj, 'Отсутствует поле "result"'
