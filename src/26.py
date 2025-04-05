import numpy as np
from scipy.optimize import minimize

def find_minima(f, bounds=(0, 10)):
    """
    Find the minimum of a function f in a given interval.
    
    Args:
    f (callable): The function to optimize. It should be a single-argument function that returns
                  a single number for each argument.
    bounds: A tuple of two elements representing the interval where the optimization is performed.

    Returns:
    float: The minimum value of the function.
    """
    # Define the constraint
    def constraint(point):
        return point[0] * (point[1]**2 + 1) - 3
    
    # Use scipy.optimize.minimize to find the minimum value
    result = minimize(fun=f, x0=[5, 1], method='Nelder-Mead', constraints=constraint)
    
    # Return the minimum value of the function
    return result.fun

# Define the objective function (for example, a quadratic function)
def quad_function(x):
    return x[0]**2 + x[1]**2

# Find the minimum of the quadratic function
minimum_value = find_minima(quad_function)

print("Minimum value:", minimum_value)
