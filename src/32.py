import pandas as pd

def calculate_average(dataframe):
    """
    Calculate the average values across all columns in the given dataframe.
    
    Args:
    - dataframe (pd.DataFrame): The input DataFrame containing numeric data.

    Returns:
    - float: Average value of all columns combined.
    """
    # Calculate the average using pandas
    total_sum = dataframe.sum()
    return total_sum.mean()

# Example usage:
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 45],
    "Salary": [60000, 70000, 80000]
}

df = pd.DataFrame(data)

average_salary = calculate_average(df)
print(f"The average salary is: {average_salary}")
