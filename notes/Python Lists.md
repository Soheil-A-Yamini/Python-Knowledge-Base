# 🐍 Python Lists

A **list** in Python is an **ordered, mutable sequence** of elements.  
Lists can store **any type of object** (integers, strings, floats, even other lists), and elements do not need to be the same type.

---

## 🔹 Creating Lists

```python
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, 'apple', 3.14, True]
```

---

## 🔹 Accessing Elements

- **Indexing** (zero-based):
  ```python
  print(numbers[0])    # Output: 1
  print(mixed[1])      # Output: 'apple'
  ```

- **Negative Indexing** (from the end):
  ```python
  print(numbers[-1])   # Output: 5
  ```

---

## 🔹 Modifying Lists

- **Appending** (add to the end):
  ```python
  numbers.append(6)
  ```

- **Inserting** (at a specific index):
  ```python
  numbers.insert(2, 99)  # Insert 99 at index 2
  ```

- **Updating** (overwrite an element):
  ```python
  numbers[0] = 100
  ```

---

## 🔹 Removing Elements

- **pop()** → remove & return by index (default: last):
  ```python
  numbers.pop()      # Removes last element
  numbers.pop(1)     # Removes element at index 1
  ```

- **remove()** → remove the first matching value:
  ```python
  numbers.remove(99)
  ```

- **del** → delete by index or slice:
  ```python
  del numbers[0]
  del numbers[1:3]   # delete multiple elements
  ```

---

## 🔹 Slicing

Retrieve portions of a list:
```python
sub = numbers[1:4]    # Elements at index 1, 2, 3
```

---

## 🔹 Common List Methods

| Method | Description |
|--------|-------------|
| `append(x)` | Add item to the end |
| `extend(iterable)` | Add all items from another iterable |
| `insert(i, x)` | Insert at position `i` |
| `remove(x)` | Remove first occurrence of `x` |
| `pop([i])` | Remove item at index `i` (default: last) |
| `clear()` | Remove all items |
| `index(x[, start[, end]])` | Return index of first occurrence |
| `count(x)` | Count occurrences of `x` |
| `sort(key=None, reverse=False)` | Sort in place |
| `reverse()` | Reverse the list |
| `copy()` | Shallow copy |

### Example: `extend` vs `append`
```python
a = [1, 2]
a.append([3, 4])   # [1, 2, [3, 4]]
a.extend([3, 4])   # [1, 2, 3, 4]
```

---

## 🔹 Iterating Over Lists

```python
for item in numbers:
    print(item)
```

---

## 🔹 Nesting Lists

Lists can contain other lists (e.g., matrices):
```python
matrix = [[1, 2], [3, 4]]
print(matrix[0][1])  # Output: 2
```

---

## ✅ Summary

- Lists are **mutable**, **ordered**, and allow **duplicates**.  
- Use them when you need to store a sequence of items that can change.  
- Very versatile for everyday programming tasks.  

---

## 📚 More Resources

- [Python Lists (Official Docs)](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
