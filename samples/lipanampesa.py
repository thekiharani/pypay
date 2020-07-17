from datetime import datetime
import requests
from samples import keys
from samples.helpers import generate_access_token, generate_password


def lipa_na_mpesa():
    date_time_str = datetime.now().strftime("%Y%m%d%H%M%S")
    access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": keys.till_number,
        "Password": generate_password(date_time_str),
        "Timestamp": date_time_str,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": keys.phone_number,
        "PartyB": keys.till_number,
        "PhoneNumber": keys.phone_number,
        "CallBackURL": "https://geekforhumans.com/api/cashy/expresscbu/",
        "AccountReference": "NTC-002/2020",
        "TransactionDesc": "Sales Commission"
    }

    response = requests.post(api_url, json=request, headers=headers)
    print(response.json())


lipa_na_mpesa()
