import json

try:

    with open("shoplink.json") as f:
        shoplink = json.load(f)
    print(shoplink)
except json.JSONDecodeError as e:
    print("Invaild JSON format")
    print(e)
except FileNotFoundError:
    print("File not found ")    
   

with open("shoplink.json") as f:
    shoplink = json.load(f)
print(shoplink)


required_fields = {"order_id", "timestamp", "item", "quantity", "price", "payment_status", "total"}

#Iterate directly over each record
if isinstance(shoplink, list):
    if not shoplink:
        print("shoplink.json is empty — no records found.")
    else:
        for i, record in enumerate(shoplink, start=1):
            if isinstance(record, dict):
                missing = required_fields - record.keys()
                if missing:
                    print(f"Record {i} missing fields: {missing}")
                else:
                    print(f"Record {i} has all required fields.")
            else:
                print(f"Record {i} is not a dictionary (type: {type(record)})")

elif isinstance(shoplink, dict):
    # Single object, not a list
    missing = required_fields - shoplink.keys()
    if missing:
        print("Missing fields:", missing)
    else:
        print(" All required fields are present.")

else:
    print(f"Shoplink is of unexpected type: {type(shoplink)}")