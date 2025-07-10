# A CLI UI so obviously not too nice but it gets the job done for this project and for now
from models.UserGate import UserGate
from models.Account import Account
from models.Admin import Admin


def first_menu():
    def get_username_and_password():
        username = input("Please Enter your username: ")
        password = input("please Enter your password: ")
        return username, password
    
    login_or_signup = input("Hello this is the User Gate you will have to login or signup enter 1 or 2\n[1] login\n[2] signup\n")
    current_user = UserGate()

    if login_or_signup == "1":
        username, password = get_username_and_password()
        current_user = current_user.login(username, password)
        if isinstance(current_user, Account):
            return current_user
        else:
            print("Login failed due to wrong username or password try again")
            return False
        
    elif login_or_signup == "2":
        username, password = get_username_and_password()
        current_user = current_user.signup(username, password)
        if isinstance(current_user, Account):
            return current_user
        else:
            print("Signup failed this account already exists try again")
            return False

    else:
        print("Oops seems like you didn't enter 1 or 2 please try again")
        return False



# main menu helper functions
def cart_menu(account):
        print(account.view_cart())
        print(f"the total cart price is ${account.total_cart_price}")
        cart_choice = input("Would you like to do:\n[1] remove an item from your cart\n[2] buy your cart\n[3] buy a specific product\n[4] nothing I'm good\n")
        if cart_choice == "1":
            product_id = input("Enter the product id of the item you'd like to remove from your cart: ")
            quantity = input("Enter the number of this item you would like to remove from your cart: ")
            return account.remove_from_cart(product_id, quantity)
        elif cart_choice == "2":
            print(account.buy_cart())
            return f"current balance: {account.account_balance}"
        elif cart_choice == "3":
            product_id = input("Enter the product ID of the product you wanna buy: ")
            return account.buy(product_id)
        else:
            return "Did nothing"
        
def make_deposit(account):
        try:
            amount = float(input("Enter the amount you'd like to deposit: "))
        except ValueError:
            return "Invalid input enter a number"
        print(account.deposit(amount))
        return f"current balance: {account.account_balance}"

def balance_menu(account):
        print(account.account_balance)
        make_deposit_decision = input("Enter 1 if you'd like to make a deposit otherwise hit anything else: ")
        if make_deposit_decision == "1":
            return make_deposit(account)
        return "Did nothing"

def normal_account_browse_products(account):
    print(account.browse_products())
    browsing_products_choice = input("would you like to do:\n[1] add a product to your cart\n[2] buy a product\n[3] nothing I'm good")

    if browsing_products_choice == "1":
            product_id = input("Enter the product ID of the product you wanna add to your cart: ")
            amount_to_add = input("Enter the amount you'd like to add: ")

            if not amount_to_add.isdigit() or int(amount_to_add) <= 0:
                return "Please enter a valid positive number for quantity."
            
            return account.add_to_cart(product_id, int(amount_to_add))
    
    elif browsing_products_choice == "2":
        product_id = input("Enter the product ID of the product you wanna buy: ")
        return account.buy(product_id)
    return

#admin helper
def get_product_info():
        name = input("Enter product name: ")
        description = input("Enter product description: ")
        cost = float(input("Enter product cost: "))
        weight = float(input("Enter product weight: "))
        return name, description, cost, weight
    
def edit_product(account):
    product_id = input("Enter the product ID of the product you want to edit: ")
    try:
        name, description, cost, weight = get_product_info()
        return account.edit_product(product_id, name, description, cost, weight)
    except ValueError:
        return "Failed enter valid numbers where appropriate"

def add_product(account):
    try:
        name, description, cost, weight = get_product_info()
        return account.add_product(name, description, cost, weight)
    except ValueError:
        return "Failed enter valid numbers where appropriate"

def admin_browse_products(account):
        print(account.browse_products())
        browsing_products_choice = input("would you like to do:\n[1] add a product to your cart\n[2] buy a product\n[3] delete a product globally\n[4] Edit a product\n[5] add a product globally\n[6] nothing I'm good\n")
        if browsing_products_choice == "1":
            product_id = input("Enter the product ID of the product you wanna add to your cart: ")
            return account.add_to_cart(product_id)
        elif browsing_products_choice == "2":
            product_id = input("Enter the product ID of the product you wanna buy: ")
            return account.buy(product_id)
        elif browsing_products_choice == "3":
            product_id = input("Enter the product ID of the product you want to delete: ")
            return account.remove_product(product_id)
        elif browsing_products_choice == "4":
            return edit_product(account)
        elif browsing_products_choice == "5":
            return add_product(account)
        else:
            return "Did nothing"

        

def main_menu(account):
    print(f"Welcome {account.username}")
    print("[0] End Session / Log out")
    print("[1] Browse Products")
    print("[2] View Cart")
    print("[3] View Account Balance")
    print("[4] Make a Deposit")
    print("[5] View Order History")
    if isinstance(account, Admin):
        print("[6] Admin: add a product")
        print("[7] Admin: remove a product")
        print("[8] Admin: edit a product")
        print("[9] Admin: view users")
        print("[10] Admin: view number of users")
    choice = input("Select option: ")
    valid_choices = {"0", "1", "2", "3", "4", "5"}
    if isinstance(account, Admin):
        valid_choices.update({"6", "7", "8", "9", "10"})
    if choice not in valid_choices:
        print(f"Invalid option, please enter one of {', '.join(sorted(valid_choices))}")
        return

    
    if choice == "0":
        print("Logging out...")
        return True  # signal to main() to restart session
    
    elif choice == "1" and isinstance(account, Admin):
        print(admin_browse_products(account))
        return
    elif choice == "1" and isinstance(account, Account):
        print(normal_account_browse_products(account))
        return

    elif choice == "2":
        print(cart_menu(account))
        return 

    elif choice == "3":
        print(balance_menu(account))
        return
    
    elif choice == "4":
        print(make_deposit(account))
        return
    
    elif choice == "5":
        print(account.view_order_history)
        return
    
    # admin stuff
    elif choice == "6" and isinstance(account, Admin):
        print(add_product(account))
        return
    
    elif choice == "7" and isinstance(account, Admin):
        product_id = input("Enter the product ID of the product you want to delete")
        print(account.remove_product(product_id))
        return

    elif choice == "8" and isinstance(account, Admin):
        print(edit_product(account))
        return
    
    elif choice == "9" and isinstance(account, Admin):
        print(account.view_users())
        return
    
    elif choice == "10" and isinstance(account, Admin):
        print(account.user_count)
        return
    
def main():
    print("This is the CLI based e-commerce app! made by mr.e\n")
    
    while True:
        exit_choice = input("press q if you'd like to close the app otherwise hit anything else ")
        if exit_choice == "q":
            exit()

        user_account = False
        while user_account == False:
            user_account = first_menu()
        
        print("Alright, you're now inside the app!\n")

        while True:
            session_ended = main_menu(user_account)
            if session_ended:
                print("Session ended. Returning to login.")
                break

if __name__ == "__main__":
    main()