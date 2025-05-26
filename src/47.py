import numpy as np
import pandas as pd

def calculate_average(data):
    """
    Calculate the average value of a given dataset.
    
    Parameters:
    - data: A list or array containing numerical values.
    
    Returns:
    - The mean (average) value of the input data.
    """
    if len(data) == 0:
        return None
    else:
        return np.mean(data)

# Example usage
data = [1, 2, 3, 4, 5]
average_value = calculate_average(data)
print("Average:", average_value)
