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
    return f"Added product {name}"

def read_User_data():
    user_data_path = get_data_path("User_data.json")
    with open(user_data_path, "r") as user_info_file:
        data = json.load(user_info_file)
        return data
    
def dump_to_user_file(data):
    user_data_path = get_data_path("User_data.json")
    with open(user_data_path, "w") as file:
        json.dump(data, file, indent=4)

def delete_product_from_every_cart(product_id):
    user_data = read_User_data()

    for user_id in user_data:
        cart = user_data[user_id]["cart"]
        if str(product_id) in cart:
            del cart[str(product_id)]

    dump_to_user_file(user_data)
    return f"successfully deleted {product_id} from all users carts"

def delete_product_from_products(product_id):
    data = load_products_data()
    if str(product_id) in data:
        del data[str(product_id)]
        dump_to_file(data)
        return True
    return False

def delete_product(product_id):
    delete_product_from_every_cart(product_id)
    deleted_from_products = delete_product_from_products(product_id)
    return f"the product ID {product_id} is invalid" if not deleted_from_products else f"successfully deleted {product_id}"

def edit_product(product_id, name, description, cost, weight):
    products = load_products_data()
    product = products[str(product_id)]
    product["name"] = name
    product["description"] = description
    product["cost"] = cost
    product["weight"] = weight
    dump_to_file(products)
    return "success"