from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure

@allure.epic('Testing DELETE method')
class TestUserDelete(BaseCase):
    @allure.description('This case testing delete user that cant be deleted')
    @allure.severity(allure.severity_level.NORMAL)
    def test_user_delete_with_id_2(self):

        # LOGIN
        user_id = '2'
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")

        # DELETE

        response2 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response2, 400)
        Assertions.assert_response_text(response2, 'Please, do not delete test users with ID 1, 2, 3, 4 or 5.')

    @allure.description('This case testing functional of delete')
    @allure.severity(allure.severity_level.NORMAL)
    def test_user_delete_verify(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # DELETE

        response3 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response3, 200)

        # GET INFO ABOUT DELETED USER

        response4 = MyRequests.get(
            f"/user/{user_id}"
        )
        Assertions.assert_code_status(response3, 200)
        Assertions.assert_response_text(response4, 'User not found')

    @allure.description("This negative case testing impossibility of deleting other user by some authorized user")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_delete_diff_user(self):

        # LOGIN FIRST USER

        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        second_user_id = '23200'

        response1 = MyRequests.post(
            "/user/login",
            data=login_data
        )

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")

        # DELETE SECOND USER

        response2 = MyRequests.delete(
            f"/user/{second_user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        # GET INFO ABOUT SECOND USER

        response3 = MyRequests.get(
            f"/user/{second_user_id}"
        )

        Assertions.assert_json_has_key(response3, 'username')
