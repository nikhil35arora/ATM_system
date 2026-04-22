import json
from pathlib import Path


DATA_FILE = Path(__file__).resolve().parent / "atm_data.json"


def _default_data():
    return {"balance": 0.0, "transactions": []}


def load_data():
    if not DATA_FILE.exists():
        data = _default_data()
        save_data(data)
        return data

    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_data(data):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
