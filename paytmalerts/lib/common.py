import requests

base_url = "https://tickets.paytm.com/v2/"


def api_call(url, method='GET', data={}, headers = {'Content-type': 'application/json'}):
    return requests.request(method, url, headers, data)