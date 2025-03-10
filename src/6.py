import random

def generate_random_code(length=10):
    """Generate a random string of letters and digits.

    Parameters:
        length (int): The desired length of the string.

    Returns:
        str: A random string of letters and digits.
    """
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(length))
