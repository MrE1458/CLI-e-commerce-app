# User class acts as the initializer/gate to the program, using the program makes you a User while signin/login makes you an Account who can do stuff

import services.user_services


class UserGate:

    def __init__(self):
        pass


    def signup(self, username, password):
        result = services.user_services.signup(username=username, password=password)
        return result

    def login(self, username, password):
        result = services.user_services.login(username, password)
        return result #--- The return is an account object created at login with the logged-in id, username and password
