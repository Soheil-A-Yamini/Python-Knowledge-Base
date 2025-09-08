# 🔄 Python While Loops

A **while loop** in Python is used to repeatedly execute a block of code **as long as a condition is true**.  
It is especially useful when the number of iterations is not known in advance.

---

## 🔹 Key Steps for a While Loop
1. **Initialize a counter (or control variable).**  
   Example: `c = 0`

2. **Define a condition** (the loop continues *while* this is `True`).  
   - If the counter increments, use `<` (less than).  
   - If the counter decrements, use `>` (greater than).  

3. **Update the counter** inside the loop body (increment or decrement).  
   Otherwise, you risk creating an **infinite loop**.

---

## 🔹 Basic Example
```python
c = 0  # Step 1: initialize

while c < 5:  # Step 2: condition
    print("Iteration:", c)
    c += 1     # Step 3: increment
```

**Output:**
```
Iteration: 0
Iteration: 1
Iteration: 2
Iteration: 3
Iteration: 4
```

👉 The loop runs **5 times** (from `c = 0` to `c = 4`), then stops once `c < 5` is no longer true.

---

## 🔹 Decrement Example
```python
c = 5

while c > 0:   # loop until counter reaches 0
    print("Countdown:", c)
    c -= 1     # decrement
```

**Output:**
```
Countdown: 5
Countdown: 4
Countdown: 3
Countdown: 2
Countdown: 1
```

---

## 🔹 Using `!=` Condition
You can also use `!=` ("not equal to"):

```python
c = 3

while c != 0:
    print("Looping... c =", c)
    c -= 1
```

**Output:**
```
Looping... c = 3
Looping... c = 2
Looping... c = 1
```

👉 The loop stops once `c == 0`.

---

## ✅ Summary
- A **while loop** repeats code while a condition is true.  
- Always remember to **update your counter** to avoid infinite loops.  
- Useful when you **don’t know in advance** how many times you’ll loop.  

---

## 📚 More Resources
- [Python Loops (Official Docs)](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
