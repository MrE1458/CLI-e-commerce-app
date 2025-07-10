# Account class
import services.account_services

class Account:
    '''
    should have browse products, add_to_cart, view_cart, remove_from_cart, total_cart_price, order_history, buy
    '''
    def __init__(self, user_id, username, password, cart, order_history, balance):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.cart = cart
        self.order_history = order_history
        self.balance = balance

    def __str__(self):
        return f"User id: {self.user_id} Username: {self.username}"

    def browse_products(self):
        display = services.account_services.return_product_info()
        return display

    #CART
    def view_cart(self):
        return services.account_services.return_formatted_cart(self.user_id)

    def add_to_cart(self, product_to_add_id, amount_to_add):
        return services.account_services.add_to_cart(product_id=product_to_add_id, user_id=self.user_id, amount_to_add=amount_to_add)

    def remove_from_cart(self, product_id, quantity_to_remove):
        return services.account_services.remove_from_cart(self.user_id, product_id, quantity_to_remove)

    def buy_cart(self):
        return services.account_services.buy_cart(self.user_id)

    @property
    def total_cart_price(self):
        total = services.account_services.find_total_price_of_cart(self.user_id)
        return total

    #MONEY LOGIC
    @property
    def account_balance(self):
        return services.account_services.get_balance(self.user_id)

    def deposit(self, amount):
        return services.account_services.add_to_balance(self.user_id, amount)

    def buy(self, product_id):
        return services.account_services.buy(self.user_id, product_id)

    @property
    def view_order_history(self):
        return services.account_services.read_order_history(self.user_id)