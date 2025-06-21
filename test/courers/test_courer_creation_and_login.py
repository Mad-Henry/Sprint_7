import allure
from methods.courer_methods import CourerMethods as CM
from data import COURER_CREATION_CREDS, COURER_NO_LOGIN_CREDS, COURER_NO_PASS_CREDS, COURER_CREATION_ERR_LGN_ALRD_EXIST_TXT, COURER_CREATION_ERR_REQUIERD_FLDS_TXT, COURER_CREATION_OK_TRUE_TXT
from data import COURER_LOGIN_CORRECT_CREDS, COURER_LOGIN_CREDS_ID, COURER_LOGIN_NO_LOGIN, COURER_LOGIN_NO_PASS, COURER_LOGIN_ERR_REQUIRED_FLDS_TXT, COURER_LOGIN_ERR_WRONG_FLDS_TXT


@allure.feature("Тесты создание курьеров")
class TestCourerCreation:

    @allure.title("Курьера можно создать")
    def test_courer_creation_avability(self):
        resp_state_and_creds = CM.register_new_courier_and_return_login_password()
        assert resp_state_and_creds[0] == 201 and resp_state_and_creds[1] != None, f'status code: {resp_state_and_creds[0]}, creds:{resp_state_and_creds[1]}'
    
    @allure.title("Нельзя создать двух одинаковых курьеров. Если создать пользователя с логином, который уже есть, возвращается ошибка")
    def test_courer_creation_dublicate_error(self):
        courier_1 = CM.register_new_courier_and_return_login_password(COURER_CREATION_CREDS)
        courier_2 = CM.register_new_courier_and_return_login_password(COURER_CREATION_CREDS)
        assert courier_2[0] == 409 and COURER_CREATION_ERR_LGN_ALRD_EXIST_TXT in courier_2[2], f'courier_2 status code:{courier_2[0]}, courier_2 message: {courier_2[1]}'
    
    @allure.title("Если не указан логин, запрос возвращает ошибку")
    def test_courer_creation_empty_login_returns_error(self):
        courier_no_login = CM.register_new_courier_and_return_login_password(COURER_NO_LOGIN_CREDS)      
        assert courier_no_login[0] == 400, \
            (f'courier_no_login status code: {courier_no_login[0]}')
        assert COURER_CREATION_ERR_REQUIERD_FLDS_TXT in courier_no_login[2], (f'courier_no_login status code: {courier_no_login[0]}')

    @allure.title("Если не указан пароль, запрос возвращает ошибку")
    def test_courer_creation_empty_password_returns_error(self):
        courier_no_pass = CM.register_new_courier_and_return_login_password(COURER_NO_PASS_CREDS)        
        assert courier_no_pass[0] == 400, \
            (f'courier_no_pass status code: {courier_no_pass[0]}')
        assert COURER_CREATION_ERR_REQUIERD_FLDS_TXT in courier_no_pass[2], (f'courier_no_pass status code: {courier_no_pass[0]}')

    @allure.title("Запрос возвращает правильный код ответа")
    def test_courer_creation_status_code_is_ok(self):
        creation_status_code = CM.register_new_courier_and_return_login_password()[0]
        assert creation_status_code == 201, f'creation_status_code is {creation_status_code}'

    @allure.title("Успешный запрос возвращает Ok-True")
    def test_courer_creation_status_text_is_ok(self):
        creation_status_text = CM.register_new_courier_and_return_login_password()[2]
        assert COURER_CREATION_OK_TRUE_TXT in creation_status_text, f'creation_status_text is {creation_status_text}'



@allure.feature("Тесты логона курьеров")
class TestCourerLogin:

    @allure.title("Курьер может авторизоваться. Успешный запрос возвращает id")
    def test_login_successful(self):
        courer_login = CM.login_courier(COURER_LOGIN_CORRECT_CREDS)
        courer_status, courer_status_txt = courer_login
        assert courer_status == 200 and courer_status_txt == COURER_LOGIN_CREDS_ID, f'Status code: {courer_status}, ID is: {courer_status_txt}'

    @allure.title("Для авторизации нужно передать все обязательные поля. Если какого-то поля нет, запрос возвращает ошибку")
    def test_login_test_required_fileds(self):
        courer_no_login_text = CM.login_courier(COURER_LOGIN_NO_LOGIN)[1]
        courer_no_pass_text = CM.login_courier(COURER_LOGIN_NO_PASS)[1]
        assert COURER_LOGIN_ERR_REQUIRED_FLDS_TXT in courer_no_login_text and COURER_LOGIN_ERR_REQUIRED_FLDS_TXT in courer_no_pass_text, \
            f'courer_no_login_text: {courer_no_login_text}, courer_no_pass_text: {courer_no_pass_text}'

    @allure.title("Система вернёт ошибку, если неправильно указать логин или пароль. Если авторизоваться под несуществующим пользователем, запрос возвращает ошибку;")
    def test_login_test_wrong_login_or_pass(self):
        wrong_login = CM.generate_random_string(10)
        wrong_pass = CM.generate_random_string(10)
        courer_wrong_login = CM.login_courier([wrong_login, COURER_LOGIN_CORRECT_CREDS[1]])[1]
        courer_wrong_pass = CM.login_courier([COURER_LOGIN_CORRECT_CREDS[0], wrong_pass])[1]
        assert COURER_LOGIN_ERR_WRONG_FLDS_TXT in courer_wrong_login and COURER_LOGIN_ERR_WRONG_FLDS_TXT in courer_wrong_pass, \
            f'courer_wrong_login: {courer_wrong_login}, courer_wrong_pass{courer_wrong_pass}'