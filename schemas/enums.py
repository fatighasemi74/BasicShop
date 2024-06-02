from enum import Enum

class StrEnum(str, Enum):
    def __str__(self):
        return str(self.value)

class UserRole(StrEnum):
    ADMIN = "admin"
    CUSTOMER = "customer"
    SELLER = "seller"

class OrderStatus(str, Enum):
    PENDING = 'pending'
    SHIPPED = 'shipped'
    DELIVERED = 'delivered'
    CANCELED = 'canceled'