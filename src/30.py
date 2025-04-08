import numpy as np

def sample_data(size):
    """
    Generate an array with a given size.
    
    Parameters:
    - size: An integer representing the desired size of the generated array.
    
    Returns:
    - A NumPy array of the specified size filled with random values.
    """
    return np.random.rand(size)

# Example usage
sampled_data = sample_data(10)
print(sampled_data)
