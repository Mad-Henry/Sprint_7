import requests
from urls import BASE_URL, COURERS_BASE_URL, COURERS_LOGIN_URL, COURERS_REMOVE_COURER
from methods.helpers import HelpersMethods as HM
import allure

class CourerMethods:

# Создание курьера

    @staticmethod
    @allure.step("Регистрация нового курьера и возврат логина, пароля и имени")
    def register_new_courier_and_return_login_password(creds=None):   
        login_pass = []
        if creds == None:    
            login = HM.generate_random_string(10)
            password = HM.generate_random_string(10)
            first_name = HM.generate_random_string(10)
        else:
            login, password, first_name = creds

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(f'{BASE_URL}{COURERS_BASE_URL}', data=payload)

        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        return response.status_code, login_pass, response.text


# Логин курьера

    @staticmethod
    @allure.step("Логин курьера")
    def login_courier(creds):

        payload = {
            "login": creds[0],
            "password": creds[1]
        }
        response = requests.post(f'{BASE_URL}{COURERS_LOGIN_URL}', data=payload)
        return response.status_code, response.text
    
# Удаление курьера

    @staticmethod
    @allure.step('Удаление курьера')
    def remove_courer(id):
        COURERS_REMOVE_COURER_N = COURERS_REMOVE_COURER + id
        response = requests.delete(f'{BASE_URL}{COURERS_REMOVE_COURER_N}')
        return response.status_code, response.text
