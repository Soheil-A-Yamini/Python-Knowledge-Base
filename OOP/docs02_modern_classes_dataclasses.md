name=docs/02_modern_classes_dataclasses_typing.md
# 🚀 Modern Python: `dataclasses`, `Enum`, Typing & Forward References

This guide shows how to build clean, type-safe models using:
```python
from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Dict, List, Optional
```

---

## 1) Why `from __future__ import annotations`?

- Postpones evaluation of type hints so you can reference classes **before** they’re defined (forward references) without quoting strings.
- Keeps annotations as strings at runtime → faster imports, fewer circular-import issues.

```python
from __future__ import annotations

@dataclass
class Node:
    value: int
    next: Optional[Node] = None  # forward reference works without quotes
```

*(Without `__future__`, you’d need `Optional["Node"]`.)*

---

## 2) Dataclasses: Less Boilerplate, More Clarity

```python
from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0
    tags: List[str] = field(default_factory=list)  # avoid mutable defaults

    def total(self) -> float:
        return self.price * self.quantity
```

**Benefits:**
- Auto `__init__`, `__repr__`, `__eq__`
- Optional: `order=True` for comparisons, `frozen=True` for immutability
- Validation goes in `__post_init__`

```python
@dataclass(frozen=True, order=True)
class SKU:
    code: str

@dataclass
class LineItem:
    product: Product
    qty: int

    def __post_init__(self):
        if self.qty <= 0:
            raise ValueError("qty must be positive")
```

---

## 3) `Enum` + `auto()` for Status & Constants

```python
from enum import Enum, auto

class OrderStatus(Enum):
    PENDING = auto()
    PAID = auto()
    SHIPPED = auto()
    DELIVERED = auto()
    CANCELLED = auto()
```

Usage:
```python
status = OrderStatus.PENDING
if status is OrderStatus.PENDING:
    ...
```

---

## 4) Typing: `Dict`, `List`, `Optional`

```python
from typing import Dict, List, Optional

Inventory = Dict[str, Product]  # mapping product name -> Product

@dataclass
class Order:
    items: List[LineItem]
    status: OrderStatus = OrderStatus.PENDING
    note: Optional[str] = None

    @property
    def subtotal(self) -> float:
        return sum(li.product.price * li.qty for li in self.items)
```

**Tip:** In Python 3.9+, you can use built-in generics: `dict[str, Product]`, `list[LineItem]`.

---

## 5) Small End-to-End Example

```python
from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Dict, List, Optional


class OrderStatus(Enum):
    PENDING = auto()
    PAID = auto()


@dataclass
class Product:
    name: str
    price: float
    stock: int = 0


@dataclass
class CartItem:
    product: Product
    qty: int

    @property
    def line_total(self) -> float:
        return self.product.price * self.qty


@dataclass
class Cart:
    items: List[CartItem] = field(default_factory=list)

    def add(self, product: Product, qty: int = 1) -> None:
        self.items.append(CartItem(product, qty))

    @property
    def subtotal(self) -> float:
        return sum(i.line_total for i in self.items)


@dataclass
class Order:
    items: List[CartItem]
    status: OrderStatus = OrderStatus.PENDING

    @property
    def total(self) -> float:
        return sum(i.line_total for i in self.items)


@dataclass
class User:
    name: str
    email: str
    cart: Cart = field(default_factory=Cart)
    orders: List[Order] = field(default_factory=list)

    def checkout(self) -> Order:
        if not self.cart.items:
            raise ValueError("Cart is empty.")
        order = Order(items=self.cart.items.copy(), status=OrderStatus.PAID)
        self.orders.append(order)
        self.cart.items.clear()
        return order
```

---

## 6) Practical Tips

- Prefer `dataclass` for **data-holding** models; use classic classes when you need heavy custom behavior.
- Use `field(default_factory=list/dict)` for **mutable defaults**.
- Use `__post_init__` for **validation**.
- Use `Enum` for controlled states instead of magic strings.
- Add type hints everywhere; they help IDEs and linters.

---

## 7) (Optional) Type-Checking Locally

If you use `mypy`:
```bash
pip install mypy
mypy .
```

---

## 8) TL;DR

- `__future__.annotations` → forward refs without quotes, faster imports
- `@dataclass` → less boilerplate, readable, safer defaults
- `Enum` → clean states/constants
- `typing` → clarity & tooling support

---
