import pytest
import urls
from urls import COURERS_REMOVE_COURER
from methods.courer_methods import CourerMethods as CM


@pytest.fixture
def create_and_remove_courer_fxtr():
    courer_creation_result = CM.register_new_courier_and_return_login_password()
    yield courer_creation_result
    courer_login_result = CM.login_courier(courer_creation_result[1][:2])
    courer_login_result_1 = courer_login_result[1]
    CM.remove_courer(courer_login_result_1)
