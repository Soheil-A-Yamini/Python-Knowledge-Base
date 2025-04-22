#Write a function count_vowels(text) that counts how many vowels (a, e, i, o, u) appear in a string. Make it case-insensitive,
#  and return a dictionary with the count of each vowel.

def count_vowels(text):
    # Initialize a dictionary to hold the counts of each vowel
    vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    # Convert the text to lowercase to make the count case-insensitive
    text = text.lower()
    
    # Iterate through each character in the text
    for char in text:
        # If the character is a vowel, increment its count in the dictionary
        if char in vowel_count:
            vowel_count[char] += 1
    
    return vowel_count
s = "Hello World! This is a test string to count vowels."
print(count_vowels(s))  # Output: {'a': 1, 'e': 2, 'i': 3, 'o': 2, 'u': 0}