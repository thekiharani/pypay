import base64
import requests
from requests.auth import HTTPBasicAuth
from samples import keys


def generate_access_token():
    consumer_key = keys.consumer_key
    consumer_secret = keys.consumer_secret
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    json_response = r.json()
    return json_response['access_token']


def generate_password(date_time_str):
    data_req = keys.till_number + keys.pass_key + date_time_str
    encoded_pass = base64.b64encode(data_req.encode())
    decoded_pass = encoded_pass.decode('utf-8')
    return decoded_pass
