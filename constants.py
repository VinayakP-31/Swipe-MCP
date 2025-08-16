headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

bearer_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyMDczNTIyLCJuYW1lIjoiQVBJIFVzZXIiLCJjb21wYW55X2lkIjoyMDM1NzYyLCJjb21wYW55X25hbWUiOiJZT1VSIEJVU0lORVNTIE5BTUUiLCJwYXJ0bmVyIjp0cnVlLCJpYXQiOjE3NTUyNTU4NDAsInZlcnNpb24iOjJ9.lYQvpiB-kIvziKdbCPTXXF2X22kYriuGk1HTZP4sxlk"

new_invoice_api = "https://app.getswipe.in/api/partner/v2/doc"

get_invoice_api = "https://app.getswipe.in/api/partner/v2/doc/{doc_hash_id}"

get_invoice_pdf_api = "https://app.getswipe.in/api/partner/v2/doc/pdf/{doc_hash_id}"

add_new_customer_api = "https://app.getswipe.in/api/partner/v2/customer"

get_customer_api = "https://app.getswipe.in/api/partner/v2/customer/{customer_id}"

get_all_products_api = "https://app.getswipe.in/api/partner/v2/product/list"

get_product_api = "https://app.getswipe.in/api/partner/v2/product/{item_id}"