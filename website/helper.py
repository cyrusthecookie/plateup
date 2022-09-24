from enum import Enum

# need to check enum values

class OrderStatus(Enum):
    ORDERED = 1
    COOKING = 2
    SERVING = 3
    COMPLETED = 4

class StaffRole(Enum):
    WAIT = 1
    KITCHEN = 2
    MANAGER = 3