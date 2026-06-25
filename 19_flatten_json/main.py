import json

JSON_DATA = json.loads("""{
    "name": "John Doe",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip": {
            "code": "12345",
            "country": "USA"
        }
    },
    "roles": ["admin", "user"]
}""")


def flatten_json(data, parent_key='', sep='.'):
    items = {}

    if isinstance(data, dict):
        for k, v in data.items():
            full_key = f"{parent_key}{sep}{k}" if parent_key else k
            items.update(flatten_json(v, full_key, sep=sep))

    elif isinstance(data, list):
        for idx, item in enumerate(data):
            full_key =f"{parent_key}{sep}{idx}" if parent_key else str(idx)
            items.update(flatten_json(item, full_key, sep=sep))
            
    else:
        items[parent_key] = data

    return items

print(flatten_json(JSON_DATA))
