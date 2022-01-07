import pytest
import requests


class TestEx12:
    def test_header_method(self):
        url = "https://playground.learnqa.ru/api/homework_header"
        response = requests.get(url)
        header = response.headers['x-secret-homework-header']
        assert header == 'Some secret value', f"Header witn name 'x-secret-homework-header' and value 'Some secret value' doesn't find in response"