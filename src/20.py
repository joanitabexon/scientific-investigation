import numpy as np
from scipy.optimize import minimize

def f(x):
    """
    Define the function to be minimized.
    :param x: Input vector of dimensions (n,)
    :return: Gradient and Hessian of the function at point x
    """
    return np.array([-2*x[0] * np.cos(x[1]), -x[0], -np.sin(x[0])])

def minimize_f(func, args):
    """
    Minimizes a given function using Nelder-Mead method.
    
    :param func: The objective function to be minimized
    :param args: Optional arguments for the minimization process
    
    :return: Minimum value of the objective function and coordinates of the minimum point
    """
    result = minimize(func, args, options={'disp': False})
    return result.fun, np.array(result.x)

if __name__ == "__main__":
    # Example usage:
    initial_guess = [0.5, 1.2]
    min_value, min_point = minimize_f(f, initial_guess)
    
    print("Minimum point:", min_point)
    print("Minimum value:", min_value)
