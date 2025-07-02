import json
from utils.path_utils import get_data_path


def load_products_data():
    user_data_path = get_data_path("products.json")
    with open(user_data_path, "r") as products_file:
        data = json.load(products_file)
        return data

def get_product_name(product_id):
    data = load_products_data()
    return data[str(product_id)]["name"]

def get_product_value(product_id):
    data = load_products_data()
    return int(data[str(product_id)]["cost"])

