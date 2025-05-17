import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Generate some sample data
data = np.random.rand(100, 5)
labels = data * 2 + 1

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2)

# Define a basic neural network model
model = Sequential()
model.add(Dense(32, activation='relu', input_shape=(5,)))
model.add(Dense(1))

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Train the model
model.fit(X_train, y_train, epochs=10)

# Evaluate the model on the testing set
score = model.evaluate(X_test, y_test)
print(f'Test score: {score}')
