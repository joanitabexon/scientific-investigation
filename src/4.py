import numpy as np

def calculate_pi(n):
    """
    Calculates the value of pi using the Monte Carlo method.
    The method generates 'n' random points inside and outside of a circle,
    and returns the ratio of the number of points inside the circle to the total number of points.
    This ratio is then multiplied by 4 to give an estimate of pi.
    """
    inside = 0
    for i in range(n):
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        if (x**2 + y**2) <= 1:
            inside += 1
    return 4 * (inside / n)
