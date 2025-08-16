customer_payload = {
    "customer_id": "123",
    "name": "TATA RATAN",
    "phone": "1234567890",
    "email": "reddi@reddi.reddi",
    "discount": 10,
    "gstin": "27AARCS7202C1ZD",
    "company_name": "GSTN",
    "opening_balance": "1245",
    "credit_limit": 200,
    "billing_address": [
        {
            "addr_id": -1,
            "addr_id_v2": "addr1",
            "address_line1": "",
            "address_line2": "",
            "pincode": "500075",
            "city": "",
            "state": "State Name",
            "country": "India"
        }
    ],
    "shipping_address": [
        {
            "addr_id": -1,
            "addr_id_v2": "addr1",
            "address_line1": "",
            "address_line2": "",
            "pincode": "500075",
            "city": "",
            "state": "State Name",
            "country": "India"
        }
    ],
    "opening_balance_type": 1,
    "dial_code": "91",
    "profile_image": "",
    "pan": "ABCD1234F",
    "notes": "Testing api",
    "cc_emails": "reddi@reddi.reddi,acb.a@bcd.con",
    "tags": ["<string>"],
    "custom_fields": [
        {
            "label": "Custom Field 1",
            "value": "Value 1"
        }
    ]
}

invoice_payload = {
    "document_type": "invoice",
    "document_date": "15-11-2024",
    "due_date": "15-11-2024",
    "party": {
        "id": "CUST123",
        "type": "customer",
        "name": "John Doe"
    },
    "items": [
        {
            "id": "ITEM123455667ghg",
            "name": "Item Namgergggree",
            "quantity": 1,
            "unit_price": 200,
            "tax_rate": 18,
            "price_with_tax": 236,
            "net_amount": 200,
            "total_amount": 236,
            "item_type": "Product"
        }
    ]
}