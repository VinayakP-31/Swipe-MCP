import requests
from constants import *

def new_customer():
    response = requests.post(customer_url, json=customer_payload, headers=headers)

    print(response.json())

def new_invoice():
    response = requests.post(invoice_url, json=invoice_payload, headers=headers)

    print(response.json())