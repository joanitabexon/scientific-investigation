import numpy as np
import pandas as pd

def calculate_average(data):
    """
    Calculates the average value of a given dataset.
    
    Parameters:
        data (list | numpy.ndarray): The dataset containing numerical values.
        
    Returns:
        float: The average value of the dataset.
    """
    if isinstance(data, pd.DataFrame):
        # Convert pandas DataFrame to NumPy array
        data = data.values
    elif isinstance(data, np.ndarray):
        pass  # No need to convert

    return np.mean(data)

# Example usage
data_points = [1.5, 2.5, 3.0, 4.5, 5.0]
average_value = calculate_average(data_points)
print("The average value is:", average_value)
