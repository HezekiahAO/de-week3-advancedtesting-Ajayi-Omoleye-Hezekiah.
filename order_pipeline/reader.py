import json
with open("shoplink.json", "r") as f:   # so open shoplink as readable and stire it in f
    shoplink = json.load(f)

print(shoplink)