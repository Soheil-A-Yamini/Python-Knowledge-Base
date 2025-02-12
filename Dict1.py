"""Almost any operation is done by key which is mapped to value.
Dictionaries ;
Is another data structure provided by python in order to store collection of key/ value pairs. 
It is fast for deletion, replace and accessing value by its key. Key behaves like an index operator in a list. 
Each key maps to a specific value which has to be unique and hashable object item such as: string, integer, 
however, the value can be any sort of object. 

Iterate is possible with a for loop, which the key is called and key would return value. 

in/ not in operators are to check whether a key is in dict or not which return boolean value: key in dict_name. 

Equality test: is only possible with: == and != but other comparison operators such as (<, >) would not run through 
dictionaries as they are not inherent order of key-value pairs   

key.get() which is similar to dict_name[key], except the get would return a value regardless of existing key but the dict_name[key] will 
raise keyError by not existing key in dictionary. The other methods are: pop(), keys(), items(), values(), clear(), popitem()which returns  
a pair as a tuple and removes them from the dictionary.

dict_name.items() is a dictionary method which returns an object view of that display\ return a list of pairs for key: value. e.g. unsorted_dict = {'o':90, 'k':1, 'gg':12}
print(unsorted_dict.items()) ==>Obj viewed list:  dict_items([('a', 1), ('b', 66), ('k', 0)])
"""
# define dictionaries 
m_dict = {'apple':5, 'grape':6}
#in place(mutable)
m_dict['apple'] = 10

# Dict comprehensive: my_dict = {key: value for key, value in iterable}
# key --> shopping item, value-->its index 
item = ['veg', 'apple', 'milk']
shopping = {item: index for index, item in enumerate(item)}
print("Shopping list: ", shopping)
# Initialize variables
account_number, account_holder, balance = None, None, None # instead of 3 times None can use: [None] * 3
test1 = {"account number": account_number, "account holder": account_holder, "balance": balance}
print(test1)

# Loop to update values
for key in test1.keys():
    value = input(f"Enter value for {key}: ")
    test1[key] = value

print(test1)

#---------------------------------
"""Word Frequency Counter:
Write a program that takes a sentence as input and counts the frequency of each word in the sentence. 
Store the word frequencies in a dictionary where the keys are the words and the values are the corresponding frequencies."""

sentence = input("Enter a sentence: ")
sentence_split = sentence.split()
word_frequency = {}
for word in sentence_split:
    word_frequency[word] = word_frequency.get(word, 0)+1
print(word_frequency)
for word, count in word_frequency.items():
    print(f"{word}: {count}")