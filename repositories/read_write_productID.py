from utils.path_utils import get_data_path

def read_current_product_id():
    user_data_path = get_data_path("productID.txt")
    with open(user_data_path, "r") as productID_file:
        return int(productID_file.readline().strip())
    
def increment_product_id(incrementer_amount):
    user_data_path = get_data_path("productID.txt")

    with open(user_data_path, "r") as productID_file:
        new_product_id = int(productID_file.readline().strip()) + incrementer_amount

    with open(user_data_path, "w") as productID_file:
        productID_file.write(str(new_product_id) + "\n")

    return new_product_id

def reduce_product_id(reduction_amount):
    user_data_path = get_data_path("productID.txt")

    with open(user_data_path, "r") as productID_file:
        new_product_id = int(productID_file.readline().strip()) - reduction_amount

    with open(user_data_path, "w") as productID_file:
        productID_file.write(str(new_product_id) + "\n")

    return new_product_id