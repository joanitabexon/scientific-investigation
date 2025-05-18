import numpy as np
import pandas as pd

def calculate_statistics(dataframe):
    """
    This function calculates statistical summary statistics such as mean,
    median, standard deviation, and min/max values of given DataFrame.
    
    Parameters:
    - dataframe: A pandas DataFrame containing the data to be analyzed
    
    Returns:
    - StatisticsDataFrame: A pandas DataFrame with calculated statistical summaries
    """

    # Calculate the mean, standard deviation, minimum value, and maximum value for each column
    statistics = dataframe.describe()
    
    return statistics

# Example usage
data = {
    'Column1': np.random.randn(10),
    'Column2': np.linspace(-5, 5, 10)
}
df = pd.DataFrame(data)

statistics_df = calculate_statistics(df)
print(statistics_df)
