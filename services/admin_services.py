from repositories import read_write_products

def add_product(name, description, cost, weight):
    return read_write_products.add_product(name, description, cost, weight)

def delete_product(product_id):
    return read_write_products.delete_product(product_id)