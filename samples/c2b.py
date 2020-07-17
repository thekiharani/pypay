import requests
from samples.helpers import generate_access_token
from samples import keys


def register_url():
    access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "ShortCode": keys.bill_number,
        "ResponseType": "Completed",
        "ConfirmationURL": "https://noriahub.com/confirmation",
        "ValidationURL": "https://noriahub.com/validation_url"
    }
    response = requests.post(api_url, json=request, headers=headers)
    print(response.json())


def c2b_simulation():
    access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "ShortCode": keys.bill_number,
        "CommandID": "CustomerPayBillOnline",
        "Amount": "5",
        "Msisdn": keys.test_msisdn,
        "BillRefNumber": "NoriaTec-05/2020"
    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.json())


c2b_simulation()
