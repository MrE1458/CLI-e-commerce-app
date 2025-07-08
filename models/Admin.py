from models.Account import Account
from services import admin_services

class Admin(Account):

    def __init__(self, user_id, username, password, cart, order_history, balance):
        super().__init__(user_id, username, password, cart, order_history, balance)

    def add_product(self, name, description, cost, weight):
        return admin_services.add_product(name, description, cost, weight)

    def remove_product(self, product_id):
        return admin_services.delete_product(product_id)

    def edit_product(self):
        pass

    def view_users(self):
        pass

    def view_number_of_users(self):
        pass

#admin1 = Admin(1000, "Admin", "bridge8", {}, [], 1970)
#print(admin1.remove_product(1005))
#print(admin1.add_product("cool chair #2", "so comfy bro", 20, 7000))