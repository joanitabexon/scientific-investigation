import numpy as np

def generate_random_data(n):
    """
    Generate a list of n random numbers between 0 and 1.
    
    Parameters:
        n (int): Number of random numbers to generate.
        
    Returns:
        np.ndarray: A numpy array containing the generated random data.
    """
    return np.random.rand(n)

# Example usage
random_data = generate_random_data(5)
print(random_data)
