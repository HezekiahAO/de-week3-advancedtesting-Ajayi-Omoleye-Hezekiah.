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


required_fields = json.load(shoplink)

missing = required_fields - shoplink.keys()

if missing:
    print("Missing Field: ", missing)
else:
    print("No field is missing")