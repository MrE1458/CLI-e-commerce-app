from models.Account import Account
from services import admin_services

class Admin(Account):

    def __init__(self, user_id, username, password, cart, order_history, balance):
        super().__init__(user_id, username, password, cart, order_history, balance)
        self.admin = True

    def add_product(self, name, description, cost, weight):
        return admin_services.add_product(name, description, cost, weight)

    def remove_product(self, product_id):
        return admin_services.delete_product(product_id)

    def edit_product(self, product_id, name, description, cost, weight):
        return admin_services.edit_product(product_id, name, description, cost, weight)

    def view_users(self):
        return admin_services.formatted_users()
    
    @property
    def user_count(self):
        return admin_services.number_of_users()


