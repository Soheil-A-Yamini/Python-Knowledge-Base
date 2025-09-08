# 🔁 Python For Loops

A **for loop** in Python is used to iterate over a sequence (such as a **list, tuple, string, or range**) and execute a block of code for each element in that sequence.  

---

## 🔹 Basic Syntax
```python
for variable in sequence:
    # Code to execute for each item
```

**Example:**
```python
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
```

**Output:**
```
apple
banana
cherry
```

---

## 🔹 Using `range()`

The `range()` function generates a sequence of numbers, which is commonly used with for loops.

```python
for i in range(5):
    print(i)
```

**Output:**
```
0
1
2
3
4
```

---

## 🔹 Looping Through Strings

You can iterate through each character in a string:

```python
for char in "hello":
    print(char)
```

**Output:**
```
h
e
l
l
o
```

---

## 🔹 Looping with Index

To get both the **index and value**, use `enumerate()`:

```python
colors = ['red', 'green', 'blue']
for index, color in enumerate(colors):
    print(index, color)
```

**Output:**
```
0 red
1 green
2 blue
```

---

## 🔹 Nested For Loops

A **for loop inside another for loop** is called a nested loop:

```python
for i in range(2):
    for j in range(3):
        print(f"i={i}, j={j}")
```

**Output:**
```
i=0, j=0
i=0, j=1
i=0, j=2
i=1, j=0
i=1, j=1
i=1, j=2
```

---

## 🔹 Breaking and Continuing

- **`break`** → exit the loop early.  
- **`continue`** → skip the rest of the current iteration.  

```python
for num in range(5):
    if num == 3:
        break
    print(num)
# Output: 0, 1, 2

for num in range(5):
    if num == 3:
        continue
    print(num)
# Output: 0, 1, 2, 4
```

---

## 🔹 The `else` Clause

A `for` loop can have an **`else` clause**, which runs if the loop **completes normally** (without hitting `break`).

```python
for n in range(3):
    print(n)
else:
    print("Loop finished without break")
```

**Output:**
```
0
1
2
Loop finished without break
```

---

## ✅ Summary
- Use **for loops** to iterate over sequences or ranges.  
- Use **`enumerate()`** to
