from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Dict, List, Optional


# ---------------------------
# Domain Models
# ---------------------------

@dataclass
class Product:
    name: str
    price: float
    quantity: int
    category: str

    def __post_init__(self) -> None:
        if self.price < 0:
            raise ValueError("Price cannot be negative.")
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative.")


@dataclass
class CartItem:
    product_name: str
    unit_price: float
    quantity: int

    @property
    def line_total(self) -> float:
        return self.unit_price * self.quantity


class OrderStatus(Enum):
    PENDING = auto()
    PAID = auto()
    SHIPPED = auto()
    DELIVERED = auto()
    CANCELLED = auto()


@dataclass
class Order:
    order_id: int
    items: List[CartItem]
    subtotal: float
    discount: float
    total: float
    status: OrderStatus = OrderStatus.PENDING

    def set_status(self, status: OrderStatus) -> None:
        self.status = status


# ---------------------------
# Inventory / Shopping Cart
# ---------------------------

class Inventory:
    """In-memory product inventory."""

    def __init__(self) -> None:
        self._products: Dict[str, Product] = {}

    def add_product(self, product: Product) -> None:
        """Add or update a product (by name). Quantities are overwritten unless you call `increase_stock`."""
        self._products[product.name] = product

    def increase_stock(self, name: str, amount: int) -> None:
        self._require(name)
        if amount < 0:
            raise ValueError("Increase amount must be non-negative.")
        self._products[name].quantity += amount

    def decrease_stock(self, name: str, amount: int) -> None:
        self._require(name)
        if amount < 0:
            raise ValueError("Decrease amount must be non-negative.")
        if self._products[name].quantity < amount:
            raise ValueError(f"Insufficient stock for '{name}'.")
        self._products[name].quantity -= amount

    def remove_product(self, name: str) -> None:
        self._require(name)
        del self._products[name]

    def get(self, name: str) -> Product:
        self._require(name)
        return self._products[name]

    def has_stock(self, name: str, amount: int) -> bool:
        p = self._products.get(name)
        return bool(p and p.quantity >= amount)

    def _require(self, name: str) -> None:
        if name not in self._products:
            raise KeyError(f"Product '{name}' not found in inventory.")

    def __repr__(self) -> str:
        return f"Inventory({list(self._products.values())})"


class ShoppingCart:
    """A simple shopping cart bound to a user (but not requiring it)."""

    def __init__(self) -> None:
        self._items: Dict[str, CartItem] = {}

    def add(self, product: Product, quantity: int = 1) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if product.name in self._items:
            self._items[product.name].quantity += quantity
        else:
            self._items[product.name] = CartItem(
                product_name=product.name,
                unit_price=product.price,
                quantity=quantity,
            )

    def remove(self, product_name: str, quantity: Optional[int] = None) -> None:
        """Remove a product entirely or decrease its quantity."""
        if product_name not in self._items:
            return
        if quantity is None or quantity >= self._items[product_name].quantity:
            del self._items[product_name]
        else:
            self._items[product_name].quantity -= quantity

    def clear(self) -> None:
        self._items.clear()

    @property
    def items(self) -> List[CartItem]:
        return list(self._items.values())

    @property
    def subtotal(self) -> float:
        return sum(i.line_total for i in self._items.values())

    def __repr__(self) -> str:
        return f"ShoppingCart(items={self.items}, subtotal={self.subtotal:.2f})"


# ---------------------------
# Payments / Discounts
# ---------------------------

class PaymentProcessor:
    """Mock payment processor—always succeeds."""

    @staticmethod
    def charge(amount: float, user_email: str) -> bool:
        # In real life: call a gateway (Stripe/Adyen/PayPal), handle failures, retries, etc.
        if amount < 0:
            raise ValueError("Charge amount cannot be negative.")
        return True


def discount_engine(subtotal: float) -> float:
    """
    Example rule:
    - 10% off if subtotal >= 100
    - Otherwise, no discount
    """
    return 0.1 * subtotal if subtotal >= 100 else 0.0


# ---------------------------
# User / Order Placement
# ---------------------------

@dataclass
class User:
    name: str
    email: str
    shipping_address: str
    cart: ShoppingCart = field(default_factory=ShoppingCart)
    orders: List[Order] = field(default_factory=list)

    def place_order(self, inventory: Inventory, payment: PaymentProcessor) -> Order:
        """
        Validate stock, reserve inventory, charge payment,
        create an order, and clear the cart.
        """
        if not self.cart.items:
            raise ValueError("Cart is empty.")

        # Check stock first (fail fast before any mutations)
        for item in self.cart.items:
            if not inventory.has_stock(item.product_name, item.quantity):
                raise ValueError(f"Insufficient stock for '{item.product_name}'.")

        # Reserve inventory
        for item in self.cart.items:
            inventory.decrease_stock(item.product_name, item.quantity)

        # Compute totals & discounts
        subtotal = self.cart.subtotal
        discount = discount_engine(subtotal)
        total = round(subtotal - discount, 2)

        # Charge payment
        charged = payment.charge(total, self.email)
        if not charged:
            # If payment fails, return stock (not implemented in this mock)
            raise RuntimeError("Payment failed.")

        # Create and save order
        order_id = len(self.orders) + 1
        order = Order(
            order_id=order_id,
            items=[CartItem(i.product_name, i.unit_price, i.quantity) for i in self.cart.items],
            subtotal=round(subtotal, 2),
            discount=round(discount, 2),
            total=total,
            status=OrderStatus.PAID,
        )
        self.orders.append(order)

        # Clear cart after successful purchase
        self.cart.clear()
        return order

    def order_history(self) -> List[Order]:
        return self.orders


# ---------------------------
# Demo (safe to run)
# ---------------------------

if __name__ == "__main__":
    # Seed an inventory
    inventory = Inventory()
    inventory.add_product(Product(name="Water", price=1.00, quantity=20, category="Drinks"))
    inventory.add_product(Product(name="Ice", price=2.50, quantity=5, category="Frozen"))
    inventory.add_product(Product(name="Chocolate", price=3.75, quantity=40, category="Snacks"))

    # Create a user
    user = User(name="Sina", email="sina@g.com", shipping_address="Altstadt 11, 4600 Wels")

    # Build a cart
    user.cart.add(inventory.get("Water"), quantity=10)      # 10 x 1.00 = 10.00
    user.cart.add(inventory.get("Chocolate"), quantity=30)  # 30 x 3.75 = 112.50
    # Subtotal = 122.50 → Discount 10% = 12.25 → Total = 110.25

    print("🧺 Cart:", user.cart)
    print("📦 Inventory before order:", inventory)

    # Place an order
    payment = PaymentProcessor()
    order = user.place_order(inventory, payment)

    print(f"\n✅ Order #{order.order_id} placed:")
    print("  Status  :", order.status.name)
    print("  Subtotal:", order.subtotal)
    print("  Discount:", order.discount)
    print("  Total   :", order.total)

    print("\n📦 Inventory after order:", inventory)
    print("🧾 Order history:", [o.order_id for o in user.order_history()])