import numpy as np
import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'gender': ['F', 'M', 'F']
}

df = pd.DataFrame(data)
print(df)
