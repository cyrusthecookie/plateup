# need to check how to make this abstract

class Staff:
    def __init__(self, password, restaurant, role):
        self.password = password # probably needs encryption
        self.restaurant = restaurant
        self.role = role