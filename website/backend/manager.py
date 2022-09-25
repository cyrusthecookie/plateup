from staff import Staff
from helper import StaffRole

class Manager(Staff):
    def __init__(self, password, restaurant):
        Staff.__init__(self, password, restaurant, StaffRole.MANAGER)