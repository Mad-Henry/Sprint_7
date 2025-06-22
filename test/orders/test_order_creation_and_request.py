import allure
import requests
from methods.order_methods import OrderMethods as OM
from data import ORDER_REQUEST_ALL_CRRCT_FLDS, ORDER_REQUEST_ALL_COLORS, ORDER_REQUEST_COLOR_IS_NONE
import pytest


@allure.feature("Тесты создания заказа")
class TestOrderCreation:

    @allure.title('Параметризованный тест: 1.Указать один из цветов, 2.Оба цвета, 3.Не указывать цвета')
    @pytest.mark.parametrize("payload", [ORDER_REQUEST_ALL_CRRCT_FLDS, ORDER_REQUEST_ALL_COLORS, ORDER_REQUEST_COLOR_IS_NONE])
    def test_order_creation_responce_include_track(self, payload):
        order_resp_txt = OM.order_creation(payload)[1]
        order_resp_track = order_resp_txt.split(':')
        OM.order_cancalation(order_resp_track[1])
        assert 'track' in order_resp_txt, f'order_resp_txt is: {order_resp_txt}, payload is {payload}'



@allure.feature("Тесты получения заказа")
class TestOrderRequest:

    @allure.title('В тело ответа возвращается список заказов.')
    def test_order_request_check_for_orders_list(self):
        resul_status_code, resul_text = OM.order_request()[0], OM.order_request()[1]
        assert resul_text and resul_status_code == 200, f'Status_code is: {resul_status_code}, Text start with: {resul_text[:10]}'

