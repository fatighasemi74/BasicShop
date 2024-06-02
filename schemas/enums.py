from enum import Enum, StrEnum

class UserRole(StrEnum):
    ADMIN = "admin"
    CUSTOMER = "customer"
    SELLER = "seller"

class OrderStatus(str, Enum):
    PENDING = 'pending'
    SHIPPED = 'shipped'
    DELIVERED = 'delivered'
    CANCELED = 'canceled'