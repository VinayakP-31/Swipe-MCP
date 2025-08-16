import requests
from constants import *
from payload.invoice_payload import *

def new_invoice():
    response = requests.post(new_invoice_api, json=invoice_payload, headers=headers)
    print(response.json())

def get_invoice():
    response = requests.get(get_invoice_api, headers=headers)
    print(response.json())

def get_invoice_pdf():
    response = requests.get(get_invoice_pdf_api, headers=headers)
    print(response.json())

def add_customer():
    response = requests.post(add_new_customer_api, json=customer_payload, headers=headers)
    print(response.json())

def get_customer():
    response = requests.get(get_customer_api, headers=headers)
    print(response.json())

def update_customer():
    response = requests.get(add_new_customer_api, json=customer_payload, headers=headers )

def get_product():
    response = requests.get(get_product_api, headers=headers)
    print(response.json())

def get_all_products():
    response = requests.get(get_all_products_api, headers=headers)
    print(response.json())