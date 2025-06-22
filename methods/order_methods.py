import requests
from urls import BASE_URL, ORDERS_URL, ORDER_CANCEL
import json
import allure


class OrderMethods:
 
    @staticmethod
    @allure.step("Создание заказа")
    def order_creation(payload):
        payload_ser = json.dumps(payload)
        responce = requests.post(f'{BASE_URL}{ORDERS_URL}', data=payload_ser)
        return responce.status_code, responce.text


    @staticmethod
    @allure.step("Запрос информации по заказу")
    def order_request(courierId='', nearestStation=None):
        courierId_payload = f'?courierId={courierId}'
        nearestStation_payload = ''
        if nearestStation != None:
            nearestStation_payload = f'&nearestStation={nearestStation}'
        responce = requests.get(f'{BASE_URL}{ORDERS_URL}{courierId_payload}{nearestStation_payload}')
        return responce.status_code, responce.text

    @staticmethod
    @allure.step("Отмена заказа")
    def order_cancalation(ord_track):
        payload = {
    "track": {ord_track}
}
        responce = requests.put(f'{BASE_URL}{ORDER_CANCEL}')
        return responce.status_code, responce.text