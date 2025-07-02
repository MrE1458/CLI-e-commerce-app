from utils.path_utils import get_data_path
import json
from repositories import read_write_products

def read_User_data():
    user_data_path = get_data_path("User_data.json")
    with open(user_data_path, "r") as user_info_file:
        data = json.load(user_info_file)
        return data

def read_user(user_id):
    data = read_User_data()
    return data[str(user_id)]

def dump_to_file(data):
    user_data_path = get_data_path("User_data.json")
    with open(user_data_path, "w") as file:
        json.dump(data, file, indent=4)

def add_new_user(user_id, username, password):
    from models.Account import Account
    user_data_path = get_data_path("User_data.json")
    data = read_User_data()

    data[str(user_id)] = {
        "username": username,
        "password": password,
        "user ID": user_id,
        "cart": {},
        "order history": [],
        "balance": 0
    }
    with open(user_data_path, "w") as user_info_file:
        json.dump(data, user_info_file, indent=4)
    account = Account(user_id=str(user_id), username=username, password=password, cart={}, order_history=[{}], balance=0)
    return account

def is_unique_user(username):
    user_data_path = get_data_path("User_data.json")
    data = read_User_data()
    for account in data.values():
        if account["username"] == username:
            return False
    return True

def add_to_cart(product_id, user_id):
    data = read_User_data()
    user = data[str(user_id)]

    if str(product_id) in user["cart"]:
        user["cart"][str(product_id)] += 1
    else:
        user["cart"][str(product_id)] = 1

    dump_to_file(data)

def remove_from_cart(user_id, product_id, quantity_to_remove):
    data = read_User_data()
    user = data[str(user_id)]
    to_remove = user["cart"].get(str(product_id))
    current_quantity = user["cart"][str(product_id)]

    if to_remove is None:
        return f"Product ID {product_id} not found in cart."

    if quantity_to_remove < current_quantity:
        user["cart"][str(product_id)] -= quantity_to_remove
        dump_to_file(data)
        return f"Removed {quantity_to_remove}. Remaining quantity: {user["cart"][str(product_id)]}"
    elif quantity_to_remove == current_quantity:
        del user["cart"][str(product_id)]
        dump_to_file(data)
        return f"Removed all of product ID {product_id} from cart."
    else:
        del user["cart"][str(product_id)]
        dump_to_file(data)
        return f"Requested to remove {quantity_to_remove}, but only {current_quantity} existed. Removed all instead."


def get_cart(user_id):
    data = read_User_data()
    cart = data[str(user_id)]["cart"]
    return cart

def get_balance(user_id):
    data = read_User_data()
    user_data = data[str(user_id)]
    return user_data["balance"]

def add_to_balance(user_id, amount):
    data = read_User_data()
    user_data = data[str(user_id)]
    user_data["balance"] += amount
    dump_to_file(data)
    return "Done"

def take_away_from_balance(user_id, amount):
    data = read_User_data()
    user_data = data[str(user_id)]
    cur_balance = get_balance(user_id)
    if cur_balance >= amount > 0:
        user_data["balance"] -= amount
    else:
        return "Please enter a positive value that is smaller than your current balance"
    dump_to_file(data)
    return f"{amount} taken away from the balance of userID: {user_id}"


def buy(user_id, product_id):
    '''
    This function modifies the user balance, removes the product from cart
    if it's in the cart and adds it to order history
    '''
    data = read_User_data()  # Load once
    cost = read_write_products.get_product_value(product_id)
    user_balance = data[str(user_id)]["balance"]
    if user_balance >= cost:
        data[str(user_id)]["balance"] -= cost
    else:
        return f"The current balance of {user_balance} isn't enough"

    import datetime
    cur_date_time = datetime.datetime.now().strftime("on %d/%m/%y at %H:%M")
    to_append = {product_id:
                     [f"product name: {read_write_products.get_product_name(product_id)}",
                      f"purchased: {cur_date_time}",
                      f"cost: {cost}"
                      ]
                 }
    data[str(user_id)]["order history"].append(to_append)
    dump_to_file(data)
    return f"Bought product ID {product_id} at the price of £{cost}"

def add_to_order_history(user_id, product_id):
    data = read_User_data()
    cost = read_write_products.get_product_value(product_id)

    import datetime
    cur_date_time = datetime.datetime.now().strftime("on %d/%m/%y at %H:%M")
    to_append = {product_id:
                     [f"product name: {read_write_products.get_product_name(product_id)}",
                      f"purchased: {cur_date_time}",
                      f"cost: {cost}"
                      ]
                 }

    data[str(user_id)]["order history"].append(to_append)
    dump_to_file(data)

def return_order_history(user_id):
    data = read_User_data()
    user_data = data[str(user_id)]
    return user_data["order history"]

def empty_cart(user_id):
    cart = get_cart(user_id)
    for product_id, quantity in cart.items():
        remove_from_cart(user_id, product_id, quantity)
    return "success"

