from utils import password_security_utils
from repositories.read_write_userID import increment_userID
import repositories.read_write_User_data
from models.Account import Account
from models.Admin import Admin


def generate_userID():
    return increment_userID(1)

def signup(username, password):
    if not repositories.read_write_User_data.is_unique_user(username):
        return "Username already taken. Please choose another."
    return repositories.read_write_User_data.add_new_user(generate_userID(), username, password)

def is_unique_user(username):
    return repositories.read_write_User_data.is_unique_user(username)

def login(username, password):
    '''
    takes a username and password and if they are in the database
    it returns an Account object with their data or an Admin object
    if the Account has an admin: true key-value pair    
    '''
    data = repositories.read_write_User_data.read_User_data()
    for user_id, account in data.items():
        if username == account["username"]:
            if password_security_utils.compare_password(password, account["password"]):
                if account.get("admin"):
                    return_account = Admin(user_id, account["username"], account["password"], account["cart"], account["order history"], account["balance"])
                else:
                    return_account = Account(user_id, account["username"], account["password"], account["cart"], account["order history"], account["balance"])
                return return_account
            else:
                return "wrong password"
    return "wrong username"

