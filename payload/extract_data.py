import pandas as pd
from payloads import invoice_payload
# Path to your Excel file
file_path = r"C:\Users\admin\Downloads\VTECH.xlsx"

# Read Excel
df = pd.read_excel(file_path)

print(df["DATE"])

invoice_payload["document_date"] = df["DATE"][0]
invoice_payload["due_date"] = df["DATE"][0]
invoice_payload["reference"] = str(df["DC NO"][0])
print(invoice_payload)


