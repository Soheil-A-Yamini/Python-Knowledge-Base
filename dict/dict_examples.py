# Basic Python Dictionary Examples

# Example 1: Creating a Dictionary
example_dict = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}
print('Example 1:', example_dict)

# Example 2: Accessing Values
print('Name:', example_dict['name'])
print('Age:', example_dict['age'])

# Example 3: Adding a Key-Value Pair
example_dict['job'] = 'Engineer'
print('Example 3:', example_dict)

# Example 4: Removing a Key-Value Pair
example_dict.pop('age')
print('Example 4:', example_dict)

# Example 5: Looping Through a Dictionary
for key, value in example_dict.items():
    print(f'{key}: {value}')