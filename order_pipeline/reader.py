import json
import os


def load_json_list(shoplink: str):

    file_path = os.path.abspath(shoplink)   # Gets Path

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File was not found at {file_path}")
    
    if os.path.getsize(file_path) == 0:
        raise ValueError("The file is empty")
                                                            # Reads data from JSON file.
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            shoplink = json.load(f)

        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format: {e}")
        


    if not isinstance(shoplink, list) or not all(isinstance(i, dict) for i in shoplink):
        raise ValueError(f"Expected a list of dictionaries in the JSON file. {file_path}")

    return shoplink          # Returns list of dictionaries.
                    

try: 
    shoplink = load_json_list("shoplink.json")

    print("File loaded successfully!\nItems in shoplink.json:")
    
    for item in shoplink:
        print(item)

# Catch and print errors if something goes wrong such as missing file or bad JSON
except (FileNotFoundError, ValueError) as e:
    print("Error:", e)