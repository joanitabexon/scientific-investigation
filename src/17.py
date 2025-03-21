import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_data(data):
    """
    Plots data using a scatter plot.
    
    Parameters:
    - data: A 2D numpy array containing the data points.
    """
    fig, ax = plt.subplots()
    ax.scatter(data[:, 0], data[:, 1])
    plt.show()

if __name__ == "__main__":
    # Example usage
    x = np.random.rand(10)
    y = np.random.rand(10)
    plot_data(x.reshape(-1, 1))  # Use .reshape(-1, 1) to create a column vector for scatter plot
    
    """
    # Or you can directly use this line of code if you want:
    plt.scatter(x, y)
    plt.show()
    
    This line creates a scatter plot using the x and y values in your data.
    
    For more complex datasets or specific requirements, consider using the 'scatter' function
    from matplotlib's pyplot module which is easier to use with 'numpy' arrays. You can refer to:
    https://matplotlib.org/api/pyplot_api.html?highlight=scatter#matplotlib.pyplot.scatter
    """
