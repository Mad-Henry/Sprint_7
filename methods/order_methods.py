import requests
import random
import string
from urls import BASE_URL, ORDERS_URL
import json


class OrderMethods:
 
    @staticmethod
    def order_creation(payload):
        payload_ser = json.dumps(payload)
        responce = requests.post(f'{BASE_URL}{ORDERS_URL}', data=payload_ser)
        return responce.status_code, responce.text


    @staticmethod
    def order_request(courierId='', nearestStation=None):
        courierId_payload = f'?courierId={courierId}'
        nearestStation_payload = ''
        if nearestStation != None:
            nearestStation_payload = f'&nearestStation={nearestStation}'
        responce = requests.get(f'{BASE_URL}{ORDERS_URL}{courierId_payload}{nearestStation_payload}')
        return responce.status_code, responce.text