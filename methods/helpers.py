import random
import string
import allure


class HelpersMethods:

    @staticmethod
    @allure.step("Генерация строки")   
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string