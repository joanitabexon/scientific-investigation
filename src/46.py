import numpy as np

def process_data(data):
    """
    Process data using NumPy.
    
    Parameters:
    - data: A 2D NumPy array representing the dataset.
    
    Returns:
    - processed_data: The processed data after applying transformations.
    """
    # Example of transforming a part of the dataset
    transformed = np.random.choice([0, 1], size=data.shape)
    return transformed

# Example usage
data = np.random.rand(2, 3) * 4 - 2
processed_data = process_data(data)
print(processed_data)
