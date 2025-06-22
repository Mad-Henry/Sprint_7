import allure
from methods.courer_methods import CourerMethods as CM
from methods.helpers import HelpersMethods as HM
from data import COURER_CREATION_CREDS, COURER_NO_LOGIN_CREDS, COURER_NO_PASS_CREDS, COURER_CREATION_ERR_LGN_ALRD_EXIST_TXT, COURER_CREATION_ERR_REQUIERD_FLDS_TXT, COURER_CREATION_OK_TRUE_TXT
from data import COURER_LOGIN_CORRECT_CREDS, COURER_LOGIN_CREDS_ID, COURER_LOGIN_NO_LOGIN, COURER_LOGIN_NO_PASS, COURER_LOGIN_ERR_REQUIRED_FLDS_TXT, COURER_LOGIN_ERR_WRONG_FLDS_TXT


@allure.feature("Тесты создание курьеров")
class TestCourerCreation:


    @allure.title("Нельзя создать двух одинаковых курьеров. Если создать пользователя с логином, который уже есть, возвращается ошибка")
    def test_courer_creation_dublicate_error(self, create_and_remove_courer_fxtr):
        courier_dublicate = CM.register_new_courier_and_return_login_password(create_and_remove_courer_fxtr)
        assert courier_dublicate[0] == 409 and COURER_CREATION_ERR_LGN_ALRD_EXIST_TXT in courier_dublicate[2], f'courier_2 status code:{courier_dublicate[0]}, courier_2 message: {courier_dublicate[1]}'
    
    @allure.title("Если не указан логин, запрос возвращает ошибку")
    def test_courer_creation_empty_login_returns_error(self, create_and_remove_courer_fxtr):
        courier_no_login_creds = ['']
        courier_no_login_creds.extend(create_and_remove_courer_fxtr[1:])
        courier_no_login_resp = CM.register_new_courier_and_return_login_password(courier_no_login_creds)
        assert courier_no_login_resp[0] == 400, \
            (f'courier_no_login status code: {courier_no_login_resp[0]}')
        assert COURER_CREATION_ERR_REQUIERD_FLDS_TXT in courier_no_login_resp[2], (f'courier_no_login status code: {courier_no_login_resp[0]}')

    @allure.title("Если не указан пароль, запрос возвращает ошибку")
    def test_courer_creation_empty_password_returns_error(self, create_and_remove_courer_fxtr):
        courer_no_pass_crds = list(create_and_remove_courer_fxtr)
        courer_no_pass_crds[1] = ''
        courier_no_pass = CM.register_new_courier_and_return_login_password(courer_no_pass_crds)        
        assert courier_no_pass[0] == 400, \
            (f'courier_no_pass status code: {courier_no_pass[0]}')
        assert COURER_CREATION_ERR_REQUIERD_FLDS_TXT in courier_no_pass[2], (f'courier_no_pass status code: {courier_no_pass[0]}')

    @allure.title("Запрос возвращает правильный код ответа")
    def test_courer_creation_status_code_is_ok(self, create_and_remove_courer_fxtr):
        status_code_from_fxtr = create_and_remove_courer_fxtr[0]
        assert status_code_from_fxtr == 201, f'status_code_from_fxtr is {status_code_from_fxtr}'

    @allure.title("Курьера можно создать, плюс успешный запрос возвращает Ok-True")
    def test_courer_creation_status_text_is_ok(self, create_and_remove_courer_fxtr):
        status_tezt_from_fxtr = create_and_remove_courer_fxtr[2]
        assert COURER_CREATION_OK_TRUE_TXT in status_tezt_from_fxtr, f'status_tezt_from_fxtr is {status_tezt_from_fxtr}'


@allure.feature("Тесты логона курьеров")
class TestCourerLogin:

    @allure.title("Курьер может авторизоваться. Успешный запрос возвращает id")
    def test_login_successful(self, create_and_remove_courer_fxtr):
        courer_login = CM.login_courier(create_and_remove_courer_fxtr)
        courer_status, courer_status_txt = courer_login
        assert courer_status == 200 and 'id' in courer_status_txt, f'Status code: {courer_status}, ID is: {courer_status_txt}'

    @allure.title("Для авторизации нужно передать все обязательные поля. Если какого-то поля нет, запрос возвращает ошибку")
    def test_login_test_required_fileds(self):
        courer_no_login_text = CM.login_courier(COURER_LOGIN_NO_LOGIN)[1]
        courer_no_pass_text = CM.login_courier(COURER_LOGIN_NO_PASS)[1]
        assert COURER_LOGIN_ERR_REQUIRED_FLDS_TXT in courer_no_login_text and COURER_LOGIN_ERR_REQUIRED_FLDS_TXT in courer_no_pass_text, \
            f'courer_no_login_text: {courer_no_login_text}, courer_no_pass_text: {courer_no_pass_text}'

    @allure.title("Система вернёт ошибку, если неправильно указать логин или пароль. Если авторизоваться под несуществующим пользователем, запрос возвращает ошибку;")
    def test_login_test_wrong_login_or_pass(self):
        wrong_login = HM.generate_random_string(10)
        wrong_pass = HM.generate_random_string(10)
        courer_wrong_login = CM.login_courier([wrong_login, COURER_LOGIN_CORRECT_CREDS[1]])[1]
        courer_wrong_pass = CM.login_courier([COURER_LOGIN_CORRECT_CREDS[0], wrong_pass])[1]
        assert COURER_LOGIN_ERR_WRONG_FLDS_TXT in courer_wrong_login and COURER_LOGIN_ERR_WRONG_FLDS_TXT in courer_wrong_pass, \
            f'courer_wrong_login: {courer_wrong_login}, courer_wrong_pass{courer_wrong_pass}'
        