# Write a Python function that takes two numpy arrays
#  `arr1` and `arr2` as input and returns the element-wise product of these arrays.
# 
import numpy as np
def funcy():
    arr1 = np.array(input("Enter a numpy arr: ").split(), dtype=float)
    arr2 = np.array(input("Enter second arr: ").split(), dtype=float)
    arr3 = np.multiply(arr1, arr2)
    return arr3
test = funcy()
print(test)