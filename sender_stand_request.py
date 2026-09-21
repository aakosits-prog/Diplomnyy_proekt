import requests
import configuration
import data

# Функция для отправки POST-запроса на создание нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)

# Функция для создания заказа и извлечения его трек-номера
def get_order_track():
    response = post_new_order(data.order_body)
    return response.json()["track"]

# Функция для отправки GET-запроса и получения данных заказа по треку
def get_order_by_track(track):
    params = {"t": track}
    response = requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH,
        params=params
    )
    return response
