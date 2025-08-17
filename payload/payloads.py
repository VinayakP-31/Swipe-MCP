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
    "party": {
        "id": "CUST123",
        "type": "customer",
        "name": "John Doe",
        "country_code": "91",
        "phone_number": "1234567890",
        "company_name": "Company Name",
        "email": "johndoe@example.com",
        "gstin": "27AARCS7202C1ZD",
        "shipping_address": {
            "addr_id": 1,
            "addr_id_v2": "addr1",
            "address_line1": "123 Street",
            "address_line2": "Apt 4B",
            "city": "Hyderabad City",
            "state": "TELANGANA",
            "country": "India",
            "pincode": "500032"
        },
        "billing_address": {
            "addr_id": 1,
            "addr_id_v2": "addr1",
            "address_line1": "123 Street",
            "address_line2": "Apt 4B",
            "city": "Hyderabad City",
            "state": "TELANGANA",
            "country": "India",
            "pincode": "500032"
        }
    },
    "due_date": "15-11-2024",
    "reference": "Reference Text",
    "notes": "Notes for the document",
    "terms": "Terms and Conditions",
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
            "discount_percent": 0,
            "discount_amount": 0,
            "description": "Item Description",
            "hsn_code": "1234",
            "item_type": "Product",
            "unit": "kg",
            "category": "Electronics"
        },
        {
            "id": "ITEM123fgd4vh5",
            "name": "Item Name12hfdfdf345",
            "quantity": 1,
            "unit_price": 200,
            "tax_rate": 18,
            "price_with_tax": 236,
            "net_amount": 200,
            "total_amount": 236,
            "discount_percent": 0,
            "discount_amount": 0,
            "description": "Item Description 12345",
            "hsn_code": "1234",
            "item_type": "Product",
            "unit": "kg",
            "category": "Electronics"
        }
    ],
    "payments": [
        {
            "amount": 100,
            "method": "upi",
            "notes": "Payment notes",
            "bank_details": {
                "account_number": "1234567890",
                "ifsc": "SBIN0000001",
                "bank_name": "State Bank of India",
                "branch": "Mumbai"
            }
        }
    ],
    "company_shipping_address": {
        "addr_id": 1,
        "addr_id_v2": "addr1",
        "address_line1": "123 Street",
        "address_line2": "Apt 4B",
        "city": "Hyderabad City",
        "state": "TELANGANA",
        "country": "India",
        "pincode": "500032"
    },
    "company_billing_address": {
        "addr_id": 1,
        "addr_id_v2": "addr1",
        "address_line1": "123 Street",
        "address_line2": "Apt 4B",
        "city": "Hyderabad City",
        "state": "TELANGANA",
        "country": "India",
        "pincode": "500032"
    }
}
