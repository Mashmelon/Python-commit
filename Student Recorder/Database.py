import json
import os

DB_FILE = "data/records.json"


class Database:
    """Handles file reading/writing safely."""

    def __init__(self):
        if not os.path.exists("data"):
            print("Creating datafolder")
            os.makedirs("data")

        if not os.path.isfile(DB_FILE):
            with open(DB_FILE, "w") as f:
                json.dump({}, f)

    def read(self):
        with open(DB_FILE, "r") as f:
            return json.load(f)

    def write(self, data):
        with open(DB_FILE, "w") as f:
            json.dump(data, f, indent=4)
