import numpy as np
import matplotlib.pyplot as plt

def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    :param numbers: List of numbers to be averaged.
    :return: The average of the given list of numbers.
    """
    return np.mean(numbers)

# Example usage:
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("Average:", average)

plt.plot(numbers)
plt.show()
