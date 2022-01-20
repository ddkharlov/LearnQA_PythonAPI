from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import json
import allure


@allure.epic('Testing functional of edit users data')
class TestUserEdit(BaseCase):
    @allure.description("This case testing functional of editing firstName of user")
    @allure.severity(allure.severity_level.NORMAL)
    def test_edit_just_created_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
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

        # EDIT
        new_name = "Changed name"

        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response3, 200)

        # GET

        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            "Wrong name of user after edit"
        )

    @allure.description("This case testing editing user data by unauthorized user")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_edit_user_no_auth(self):
        #  REGISTER OF NEW USER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        last_name = register_data['lastName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # EDIT USER NO AUTH
        new_first_name = "John"
        new_last_name = "Doe"

        response2 = MyRequests.put(
            f"/user/{user_id}",
            data={"firstName": new_first_name, "lastName": new_last_name}
        )

        # LOGIN AS REGISTERED USER
        login_data = {
            'email': email,
            'password': password
        }
        response3 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response3, "auth_sid")
        token = self.get_header(response3, "x-csrf-token")

        # GET INFO BY REGISTER USER AFTER EDIT WITH NO AUTH

        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            first_name,
            f"Wrong name of user after edit {first_name}"
        )

        Assertions.assert_json_value_by_name(
            response4,
            "lastName",
            last_name,
            f"Wrong name of user after edit {last_name}"
        )

    @allure.description("This case testing editing user data by some unauthorized user")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_edit_for_diff_user(self):
        #  REGISTER OF NEW USER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        username = register_data['username']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN AS NEW USER
        login_data = {
            'email': email,
            'password': password
        }

        response2 = MyRequests.post(
            "/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # GET INFO ABOUT DIFF USER

        diff_user_id = int(user_id) - 1

        response3 = MyRequests.get(
            f"/user/{diff_user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        diff_user_username = json.loads(response3.text)['username']

        # EDIT DIFF USER WITH NEW AUTH USER
        edited_username_for_diff_user = "Change username"

        response4 = MyRequests.put(
            f"/user/{diff_user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"username": edited_username_for_diff_user}
        )

        # GET USERNAME OF DIFF USER

        response5 = MyRequests.get(
            f"/user/{diff_user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_json_value_by_name(
            response5,
            'username',
            diff_user_username,
            f"Username can't be edited by different user"
        )

    @allure.description("This case testing editing user email from valid to invalid format")
    @allure.severity(allure.severity_level.NORMAL)
    def test_edit_user_email(self):
        # REGISTER NEW USER
        register_data = self.prepare_registration_data()

        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
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

        # EDIT USER EMAIL

        new_email = email.replace("@", "")
        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"email": new_email}
        )

        # GET

        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response4,
            "email",
            email,
            "Error: Invalid email format was accepted for editing"
        )

    @allure.description("This case testing editing username")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_edit_user_firstname_by_one_symbol(self):
        # REGISTER NEW USER
        register_data = self.prepare_registration_data()

        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
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

        # EDIT USER EMAIL

        new_firstname = first_name.replace("a", "")
        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_firstname}
        )

        # GET

        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            new_firstname,
            "Something goes wrong"
        )
