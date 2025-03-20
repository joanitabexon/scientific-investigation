
import numpy as np

def calculate_pi(n):
    inside = 0
    for i in range(n):
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside += 1
    return 4 * inside / n

print(calculate_pi(1000))