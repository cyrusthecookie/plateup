class MenuItem:
    def __init__(self, name, cost, category, display = False, display_order = 0, desc = "", ingredients = "", tags = [], img = None):
        self.name = name
        self.cost = cost
        self.category = category
        self.display = display
        self.display_order = display_order
        self.desc = desc
        self.ingredients = ingredients
        self.tags = tags
        self.img = img