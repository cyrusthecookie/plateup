class Restaurant:
    def __init__(self, name, tables = [], menu = [], leaderboard = [], \
    manager = None, wait = None, kitchen = None):
        self.name = name
        self.tables = tables
        self.menu = menu
        self.leaderboard = leaderboard
        self.manager = manager
        self.wait = wait
        self.kitchen = kitchen