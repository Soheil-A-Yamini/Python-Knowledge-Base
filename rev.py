def reverse(x):
    # Initialze t,
    t = 0
    while x != 0:
        # Select last digit always,
        a = x % 10
        # Generate reverse mumber,
        t = t * 10 + a
        # Remove last digit from x.
        x = x // 10
    return t
