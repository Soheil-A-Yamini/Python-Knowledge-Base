def letter_frequency(text):
    """
    Count how many times each letter appears in a string.

    Args:
        text (str): The input string.

    Returns:
        dict: A dictionary with lowercase letters as keys and their counts as values.

    Notes:
        - Case-insensitive.
        - Non-letter characters are ignored.
    """
    freq = {}
    text = text.lower()

    for char in text:
        if char.isalpha():
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

    return freq


# Execute:
if __name__ == "__main__":
    test = letter_frequency('Ssoohei!@lll')
    print(test)
