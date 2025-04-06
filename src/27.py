import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = {
    'x': [1, 2, 3, 4, 5],
    'y': [2, 4, 7, 9, 10]
}

df = pd.DataFrame(data)
X = df[['x']]
y = df['y']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)
