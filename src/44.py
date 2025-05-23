import numpy as np
from scipy.optimize import fsolve

def f(x):
    return 3*x**2 - x + 5

solution = fsolve(f, 1)
print(solution)
