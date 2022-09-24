class MenuItem:
    def __init__(self, name, cost, category, display_order = 0, desc = "", ingredients = "", tags = []):
        self.name = name
        self.cost = cost
        self.category = category
        self.display_order = display_order
        self.desc = desc
        self.ingredients = ingredients
        self.tags = tags