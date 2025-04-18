def alternate_case(text):
    """
    Modify a string so that characters at even indices are lowercase 
    and characters at odd indices are uppercase.

    Args:
        text (str): The input string.

    Returns:
        str: A new string with alternating cases.
    
    Notes:
        - All characters (including spaces and punctuation) are counted in the index.
        - Only alphabetic characters will be case-transformed.
    """
    result = []

    for index, char in enumerate(text):
        if index % 2 == 0:
            result.append(char.lower())
        else:
            result.append(char.upper())

    return ''.join(result)


# Execute:
if __name__ == "__main__":
    ss = alternate_case('soheil')
    print(ss)

