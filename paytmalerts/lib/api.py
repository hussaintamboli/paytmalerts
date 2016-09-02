import requests
import json

base_url = "https://tickets.paytm.com/v2/"


class ApiError(Exception):
    pass


def api_call(url, method='GET', data={}, params={}, headers={'Content-type': 'application/json'}):
    api_response = requests.request(method, "{}{}".format(base_url, url), headers=headers, data=data, params=params)
    response = json.loads(api_response.text)
    if not response['error']:
        return response['body']

    raise ApiError(response['error'])