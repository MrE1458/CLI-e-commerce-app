from models.UserGate import UserGate
from models.Account import Account
import services.user_services
from repositories import read_write_userID
import repositories.read_write_User_data


def first_menu():
    decision = input("[1] Login\n[2] Signup\n[3] Exit\n")
    cur_user = UserGate()
    if decision == "1":
        while True:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            result = cur_user.login(username, password)
            if not isinstance(result, str):
                return result #--- returns the account object created at login
            else:
                print(result)  # prints the error message string


acc1 = UserGate()
acc1 = acc1.login("coolguy123", "pass123")
#print(isinstance(acc1, Account))
#print(acc1.deposit(1000))
#print(acc1.buy(1001))
#print(acc1.view_order_history)
#print(acc1.account_balance)
#print(acc1.add_to_cart(1006))
