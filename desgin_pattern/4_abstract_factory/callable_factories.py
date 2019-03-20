import json
from decimal import Decimal


def build_decimal(string):
    return Decimal(string)


text = '{"total": 9.61, "items": ["Americano", "Omelet", "123"]}'
print(json.loads(text, parse_float=build_decimal))
