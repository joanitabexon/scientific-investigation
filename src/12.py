import numpy as np

def explore_science(n):
    # Generate n random numbers between 1 and 10
    nums = np.random.randint(1, 10, n)
    # Calculate the sum of the squares of the first half of the numbers
    first_half_sum = np.sum(nums[:n//2]**2)
    # Calculate the sum of the squares of the second half of the numbers
    second_half_sum = np.sum(nums[n//2:]**2)
    # If the sums are equal, return "Equal"
    if first_half_sum == second_half_sum:
        return "Equal"
    # Otherwise, return "Not Equal"
    else:
        return "Not Equal"
