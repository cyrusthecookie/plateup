class Table:
    def __init__(self, number, budget = None, orders = [], needs_assistance = False, occupied = False):
        self.number = number
        self.budget = budget
        self.orders = orders
        self.needs_assistance = needs_assistance
        self.occupied = occupied