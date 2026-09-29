import json
import os

FILE = "attendance.json"


def load_data():
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            pass

    return {"required": 75, "subjects": {}}


def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)