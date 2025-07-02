from utils.path_utils import get_data_path


def read_cur_userID():
    user_data_path = get_data_path("UserID.txt")
    with open(user_data_path, "r") as userID_file:
        return int(userID_file.readline().strip())


def increment_userID(incrementer_amount):
    user_data_path = get_data_path("UserID.txt")
    with open(user_data_path, "r") as userID_file:
        user_id = int(userID_file.readline().strip()) + incrementer_amount

    with open(user_data_path, "w") as userID_file:
        userID_file.write(str(user_id) + "\n")

    return user_id