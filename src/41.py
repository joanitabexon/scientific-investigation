import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def load_data(file_path):
    """
    Load and preprocess data from the given file path.
    
    Args:
        file_path (str): The path to the file containing the dataset.
        
    Returns:
        X (numpy.ndarray): Features matrix, shape (num_samples, num_features).
        y (numpy.ndarray): Target vector, shape (num_samples,)
    """
    # Read data from a file
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    features = []
    labels = []

    for line in lines[1:]:  # Skip the first line which contains column names
        values = line.split(',')
        features.append(np.array(values).astype(float))
        y = np.array([float(value) if value else 0] * len(values))  # Convert target to binary representation
        
    return np.array(features), np.array(labels)

# Example usage: Load data from 'data.csv'
features, labels = load_data('data.csv')

X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2)
