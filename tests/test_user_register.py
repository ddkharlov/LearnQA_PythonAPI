from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import pytest
import allure


@allure.epic('This cases are testing functionality of registry')
class TestUserRegister(BaseCase):
    required_fields = [
        ('username'),
        ('password'),
        ('firstName'),
        ('lastName'),
        ('email')
    ]

    @allure.description('Happy path of registration')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.description('Negative case with existing email')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user_with_existing_email(self):
        email = "vinkotov@example.com"
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    @allure.description('Negative case with invalid email')
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_with_incorrect_email(self):
        email = "vinkotovexample.com"
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"Invalid email format", f"Incorrect email without symbol '@' was accepted. Email: {email}"

    @allure.description('Negative case without filling required field')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("fields", required_fields)
    def test_create_user_without_required_fields(self, fields):
        data = self.prepare_registration_data()
        data[fields] = None

        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)

    @allure.description('Negative case with short username')
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_with_short_username(self):
        data = self.prepare_registration_data()
        data['username'] = 'a'

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"The value of 'username' field is too short", f"Short username was accepted." \
                                                                       f" Username: '{data['username']}'"

    @allure.description('Negative case with long username')
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_with_long_username(self):
        data = self.prepare_registration_data()
        data['username'] = 'a' * 251

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"The value of 'username' field is too long", f"Long username was accepted." \
                                                                      f" Username: '{data['username']}'"
