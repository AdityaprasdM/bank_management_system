import json
import os

file = "data.json"

def load_data():
    if not os.path.exists(file):
        return {}

    try:
        with open(file, "r") as f:
            return json.load(f)

    except:
        return {}

def save_data(data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)
