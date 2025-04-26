import numpy as np
from scipy.integrate import odeint

def logistic_map(x, t):
    """ Logistic map function """
    y = 1 / (1 + np.exp(-x))
    return y * x - y

t_span = (0, 5)
y0 = 2.8
sol = odeint(logistic_map, y0, t_span)

print(sol)
