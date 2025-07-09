from repositories import read_write_products


def add_product(name, description, cost, weight):
    return read_write_products.add_product(name, description, cost, weight)

def delete_product(product_id):
    return read_write_products.delete_product(product_id)

def edit_product(product_id, name, description, cost, weight):
    return read_write_products.edit_product(product_id, name, description, cost, weight)

def formatted_users():
    user_data = read_write_products.read_User_data()
    to_return = ""

    for user_id, info in user_data.items():
        to_return += f"userID: {user_id}    username: {info['username']}    user balance: {info['balance']}\n"
    
    return to_return.strip()

def number_of_users():
    user_data = read_write_products.read_User_data()
    return len(user_data)