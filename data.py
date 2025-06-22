# Переменные для тестирования создания курьера.
# Креды
COURER_CREATION_CREDS = ['ninja', '1234', 'saske']
COURER_NO_LOGIN_CREDS = ['', '1234', 'saske']
COURER_NO_PASS_CREDS = ['ninja', '', 'saske']

# Сообщения
COURER_CREATION_OK_TRUE_TXT = '"ok":true'
COURER_CREATION_ERR_LGN_ALRD_EXIST_TXT = 'Этот логин уже используется. Попробуйте другой.'
COURER_CREATION_ERR_REQUIERD_FLDS_TXT = 'Недостаточно данных для создания учетной записи'


# Переменные для тестирования логона курьера.
# Креды
COURER_LOGIN_CORRECT_CREDS = ['MadHenry', 'Qwerty!@']
COURER_LOGIN_NO_LOGIN = ['', 'Qwerty!@']
COURER_LOGIN_NO_PASS = ['MadHenry', '']
COURER_LOGIN_CREDS_ID = '{"id":546613}'

# Сообщения
COURER_LOGIN_ERR_REQUIRED_FLDS_TXT = "Недостаточно данных для входа"
COURER_LOGIN_ERR_WRONG_FLDS_TXT = "Учетная запись не найдена"


# Переменные для тестирования заказов
ORDER_REQUEST_ALL_CRRCT_FLDS = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}
ORDER_REQUEST_ALL_COLORS = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK", 'GREY'
    ]
}
ORDER_REQUEST_COLOR_IS_NONE = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": []
}