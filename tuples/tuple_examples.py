# Tuple Examples

# Creating a tuple
my_tuple = (1, 2, 3)
print("Tuple:", my_tuple)

# Accessing elements
print("First element:", my_tuple[0])

# Immutability demonstration
try:
    my_tuple[0] = 10
except TypeError as e:
    print("Error:", e)

# Tuple unpacking
a, b, c = my_tuple
print("Unpacked:", a, b, c)