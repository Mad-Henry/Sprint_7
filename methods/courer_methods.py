import requests
import random
import string
from urls import BASE_URL, COURERS_BASE_URL, COURERS_LOGIN_URL

class CourerMethods:

# Создание курьера
    
    @staticmethod   
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def register_new_courier_and_return_login_password(creds=None):   
        login_pass = []
        if creds == None:    
            login = CourerMethods.generate_random_string(10)
            password = CourerMethods.generate_random_string(10)
            first_name = CourerMethods.generate_random_string(10)
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
    def login_courier(creds):

        payload = {
            "login": creds[0],
            "password": creds[1]
        }
        response = requests.post(f'{BASE_URL}{COURERS_LOGIN_URL}', data=payload)
        return response.status_code, response.text
    
