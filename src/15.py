import numpy as np
def calculate_pi(n):
    radius = 1
    circle = np.random.uniform(-radius, radius, (n,)) ** 2 + np.random.uniform(-radius, radius, (n,)) ** 2
    return len(circle[circle <= radius ** 2]) / n
