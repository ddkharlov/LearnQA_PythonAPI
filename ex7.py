import requests

# Первая часть задания
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")

print(response.text)

# Вторая часть задания
response2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")

print(response2.text)

# Третья часть задания
payload = {"method": "GET"}
response3 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload)

print(response3.text)

# Четвертая часть задания
payload_get = {"method": "GET"}
payload_post = {"method": "POST"}
payload_delete = {"method": "DELETE"}
payload_put = {"method": "PUT"}
payload_head = {"method": "HEAD"}
payload_options = {"method": "OPTIONS"}
payload_patch = {"method": "PATCH"}

payloads_dictionary = payload_get, payload_post, payload_patch, payload_head, payload_options, payload_put, payload_delete
for key in payloads_dictionary:

    response_get = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=key)
    print(f"Значение параметра - {key} , Тип запроса - GET, Ответ сервера: {response_get.text}")

    response_post = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=key)
    print(f"Значение параметра - {key} , Тип запроса - POST, Ответ сервера: {response_post.text}")

    response_patch = requests.patch("https://playground.learnqa.ru/ajax/api/compare_query_type", data=key)
    print(f"Значение параметра - {key} , Тип запроса - PATCH, Ответ сервера: {response_patch.text}")

    response_head = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data=key)
    print(f"Значение параметра - {key} , Тип запроса - HEAD, Ответ сервера: {response_head.text}")

    response_options = requests.options("https://playground.learnqa.ru/ajax/api/compare_query_type", data=key)
    print(f"Значение параметра - {key} , Тип запроса - OPTIONS, Ответ сервера: {response_options.text}")

    response_put = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=key)
    print(f"Значение параметра - {key} , Тип запроса - PUT, Ответ сервера: {response_put.text}")

    response_delete = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=key)
    print(f"Значение параметра - {key} , Тип запроса - DELETE, Ответ сервера: {response_delete.text}")
