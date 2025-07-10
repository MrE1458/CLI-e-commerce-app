import repositories.read_write_products
import repositories.read_write_User_data


def return_product_info():
    data = repositories.read_write_products.load_products_data()
    to_return = ""
    for product in data.values():
        for key, val in product.items():
            to_return += f"{key}: {val}\n"
        to_return += "\n"
    return to_return

def add_to_cart(product_id, user_id, amount_to_add):
    return repositories.read_write_User_data.add_to_cart(product_id, user_id, amount_to_add)

def get_product_name(product_id):
    name = repositories.read_write_products.get_product_name(product_id)
    return name

def return_formatted_cart(user_id):
    raw_cart = repositories.read_write_User_data.get_cart(user_id)
    to_return = "The cart is in the format name, product ID, quantity\n"
    if not raw_cart:
        return "Your cart is empty."

    for product_id, quantity in raw_cart.items():
        name = get_product_name(product_id=product_id)
        to_return += f"Name {name}, Product ID {product_id}, Quantity {quantity}\n"

    return to_return

def remove_from_cart(user_id, product_id, quantity_to_remove):
    repositories.read_write_User_data.remove_from_cart(user_id, product_id, quantity_to_remove)

def find_total_price_of_cart(user_id):
    cart = repositories.read_write_User_data.get_cart(user_id)
    total = 0
    for product_id, quantity in cart.items():
        total += quantity * repositories.read_write_products.get_product_value(product_id)
    return total

def add_to_balance(user_id, amount):
    return repositories.read_write_User_data.add_to_balance(user_id, amount)

def remove_from_balance(user_id, amount):
    return repositories.read_write_User_data.take_away_from_balance(user_id, amount)

def get_balance(user_id):
    return repositories.read_write_User_data.get_balance(user_id)

def buy(user_id, product_id):
    return repositories.read_write_User_data.buy(user_id, product_id)

def read_order_history(user_id):
    order_history = repositories.read_write_User_data.return_order_history(user_id) #--- returns a list of dictionaries which has product_id: [info]
    to_return = ""

    for dictt in order_history:
        for product_id, info in dictt.items():
            to_return += f"\nproductID: {product_id}\n"
            for item in info:
                to_return += f"{item}\n"
    return to_return

def empty_cart(user_id):
    return repositories.read_write_User_data.empty_cart(user_id)

def buy_cart(user_id):
    cart = repositories.read_write_User_data.get_cart(user_id)
    cart_price = find_total_price_of_cart(user_id)
    user_balance = get_balance(user_id)

    if not cart:
        return "Cart is empty"

    if user_balance >= cart_price:
        remove_from_balance(user_id, amount=cart_price)
        for product_id, quantity in cart.items():
            for i in range(quantity):
                repositories.read_write_User_data.add_to_order_history(user_id, product_id)
        empty_cart(user_id)
        return "bought cart"

    else:
        return "not enough funds available"