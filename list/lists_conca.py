"""
📘 Python Example: List Concatenation

This script demonstrates two different ways to 
concatenate multiple lists into one:
1. Using the `+` operator
2. Using unpacking (`*`)
"""

# Define three lists
a = ['a', 'b', 'c']
b = ['d', 'e', 'f']
c = ['t', 'r', 'k']

# -----------------------------
# Method 1: Concatenate with +
# -----------------------------
abc1 = a + b + c
print("Using + operator:", abc1)

# -----------------------------
# Method 2: Concatenate with *
# -----------------------------
# The unpacking operator (*) expands each list
# so they merge into a single list.
abc2 = [*a, *b, *c]
print("Using * unpacking:", abc2)

# Original lists remain unchanged
print("Original list a:", a)
