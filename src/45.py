import numpy as np
from scipy.optimize import fsolve

def f(x):
    # Define your function here
    return 5*x**2 - 3*x + 1

# Use fsolve to find roots of the function
roots = fsolve(f, [0])
print(roots)
