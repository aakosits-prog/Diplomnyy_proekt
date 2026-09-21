import requests
import configuration
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)
def get_order_track():
    response = post_new_order(data.order_body)
    return response.json()["track"]

def get_order_by_track(track):
    params = {"t": track}
    response = requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH,
        params=params
    )
    return response