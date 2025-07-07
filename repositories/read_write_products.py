import json
from utils.path_utils import get_data_path
from repositories import read_write_productID

def dump_to_file(data):
    user_data_path = get_data_path("products.json")
    with open(user_data_path, "w") as file:
        json.dump(data, file, indent=4)

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

def add_product(name, description, cost, weight):
    data = load_products_data()
    product_id = read_write_productID.increment_product_id(1) #--- this gets the new products ID and increments the ID counter so the next one will be one more
    data[str(product_id)] = {
        "name": name,
        "description": description,
        "cost": cost,
        "weight": weight,
        "product_id": product_id
    }
    dump_to_file(data)
    return "Success"

