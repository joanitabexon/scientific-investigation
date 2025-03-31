import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Example data: 100 rows, 2 columns
data = {
    'feature1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'feature2': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
}

df = pd.DataFrame(data)
