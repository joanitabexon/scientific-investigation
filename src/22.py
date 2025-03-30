import numpy as np
from scipy.optimize import minimize

def f(x):
    return np.sum(np.sin(x)**2) + 10*x[0]

result = minimize(f, [0.5])
print(result.x)
