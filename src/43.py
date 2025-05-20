import numpy as np
import matplotlib.pyplot as plt

def plot_line(x_data, y_data):
    """
    Plots a line graph with given x and y data points.
    """
    plt.plot(x_data, y_data)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Line Graph')
    plt.show()

# Example usage:
x = np.linspace(0, 10, 100)  # Generate 100 points between 0 and 10
y = x ** 2

plot_line(x, y)
