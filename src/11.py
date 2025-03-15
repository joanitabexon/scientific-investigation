import numpy as np

def calculate_pi(n):
    """
    Calculates the value of pi using the Monte Carlo method.

    Args:
        n (int): The number of random points to generate.

    Returns:
        float: The estimated value of pi.
    """
    xy = np.random.rand(n, 2)  # Generate n random points in the unit square
    in_circle = np.sum((xy ** 2).sum(axis=1) <= 1)  # Count the number of points inside the circle
    return 4 * in_circle / n  # Estimate pi using the Monte Carlo method

print(calculate_pi(10000))