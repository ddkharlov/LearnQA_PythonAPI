import pytest
import requests


class TestEx11:
    def test_cookie_method(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        response = requests.get(url)
        cookie = dict(response.cookies)
        assert cookie == {"HomeWork": "hw_value"}, f"Cookie {cookie} doesn't exist in response"
