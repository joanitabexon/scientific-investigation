import random

def get_random_number(minimum: int, maximum: int) -> int:
    """Returns a random number between minimum and maximum."""
    return random.randint(minimum, maximum)

get_random_number(1, 10)
