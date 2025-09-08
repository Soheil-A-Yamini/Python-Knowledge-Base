
"""
General format for List Comprehension in Python

[expression for item in iterable if condition]

Each part of this syntax has a specific role:

Part	    Meaning
expression:	What you want to do with each item (e.g., modify, calculate, transform).
item:	    The variable representing each element in the iterable.
iterable:	The sequence of values to loop through (e.g., list, range(), dict, etc.).
condition:	(Optional) A filter to include only specific items.

e.g.: 
expression → x**2 (We square each number)
item → x (Takes values from range(5): 0, 1, 2, 3, 4)
iterable → range(5) (Gives numbers 0-4)
"""

# Squares
squares = [x**2 for x in range(5)]
print(squares)  

# Filtering 
even_nums = [x for x in range(10) if x % 2 == 0]
print(even_nums)

odd_nums = [x for x in range(10) if x % 2 !=0]
print(odd_nums)