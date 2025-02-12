"""Merge Dictionaries:
Write a function that takes two dictionaries as input and merges them into a single dictionary. 
If there are common keys, the values from the second dictionary
 should overwrite the values from the first dictionary."""

def merging_dictionaries(dic1, dic2):
    merg = dic1.copy()
    merg.update(dic2)
    return merg

keys = ['a', 'b', 'c']
dict1 = {keys: idx for idx, keys in enumerate(keys, start=1)}
keys2 = ['d', 'e', 't']
dict2 = {keys2: value for value, keys2 in enumerate(keys2)} # therefore, the keys2 are local varable which doent make any difference to use any other variable name for it, t
# the only global varibable is keys that is being used as argument for the enumerate function. 
print(dict2) #{'d': 0, 'e': 1, 'a': 2}
merg1 = merging_dictionaries(dict1, dict2)
print("Merging Dictionaries are: ", merg1)

#---------------------
"""Dictionary Comprehension:
Rewrite an existing list-based code using dictionary comprehension. 
For example, if you have a list of tuples representing key-value pairs, 
convert it into a dictionary using dictionary comprehension."""
list_based = [('a',1), ('b',2)]
print(type(list_based[0]))
converted_list = {keys: value for value, keys in list_based}# in this version the keys and values are swaped, thus {key: value for key, value in iterable obj}
print(converted_list)

k2 = {key: value for key, value in list_based}
print(f"K2: ", k2)

"""Dictionary Sorting:
Write a function to sort a dictionary based on its values. You can choose whether to sort in ascending or descending order."""

unsorted_dict = {'o':90, 'k':1, 'gg':12}
sorted_dict = dict(sorted(unsorted_dict.items(), key=lambda item : item[1]))
print(sorted_dict)

def sorted_dict(x):
    x_sorted = dict(sorted(x.items(), key=lambda item:item[1])) # # key = lambda: is inline function to extract key from each element
    return x_sorted
sorted1 = sorted_dict(unsorted_dict)
print("Sorted dictionary: ", sorted1)