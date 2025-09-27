
# 🧱 Python Classes (Classic/OOP Style)

This guide shows how to create and use classes in **plain Python** (without extra libraries). You’ll learn `__init__`, methods, properties, class/static methods, inheritance, dunder methods, and common pitfalls.

---

## 1) Defining a Class

```python
class Product:
    def __init__(self, name, price, quantity):
        # instance attributes
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def total_value(self):
        return self.price * self.quantity
```

**Use:**
```python
p = Product("Water", 1.0, 20)
print(p.total_value())  # 20.0
```

---

## 2) String Representations

```python
class Product:
    def __init__(self, name, price, quantity):
        self.name, self.price, self.quantity = name, float(price), int(quantity)

    def __repr__(self):
        # unambiguous/dev-friendly
        return f"Product(name={self.name!r}, price={self.price}, quantity={self.quantity})"

    def __str__(self):
        # user-friendly
        return f"{self.name} (${self.price}) x {self.quantity}"
```

---

## 3) Properties (Validation & Readability)

```python
class Product:
    def __init__(self, name, price, quantity):
        self._name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = float(value)
```

---

## 4) Class Methods & Static Methods

```python
class Product:
    tax_rate = 0.2  # class attribute

    def __init__(self, name, price, quantity):
        self.name, self.price, self.quantity = name, float(price), int(quantity)

    @classmethod
    def from_string(cls, s: str):
        # "Name,Price,Qty" -> Product
        name, price, qty = s.split(",")
        return cls(name, float(price), int(qty))

    @staticmethod
    def with_tax(amount: float) -> float:
        return amount * (1 + Product.tax_rate)
```

---

## 5) Inheritance

```python
class Item:
    def __init__(self, name):
        self.name = name

class Food(Item):
    def __init__(self, name, calories):
        super().__init__(name)  # call parent init
        self.calories = calories
```

---

## 6) Equality & Ordering

```python
class Product:
    def __init__(self, name, price, quantity):
        self.name, self.price, self.quantity = name, float(price), int(quantity)

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return (self.name, self.price, self.quantity) == (other.name, other.price, other.quantity)

    def __lt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price < other.price
```

---

## 7) Immutability (Pattern)

```python
class SKU:
    __slots__ = ("_code",)

    def __init__(self, code):
        self._code = code

    @property
    def code(self):
        return self._code

    def __setattr__(self, key, value):
        if hasattr(self, key):
            raise AttributeError("SKU is immutable.")
        super().__setattr__(key, value)
```

---

## 8) Common Pitfalls

- Don’t use **mutable defaults** in `__init__` (e.g., `def __init__(..., tags=[])`). Use `None` and create inside.
- Implement `__repr__` for better debugging.
- Use properties to validate inputs.

---
