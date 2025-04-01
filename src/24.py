import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Generate some sample data for demonstration
data = np.random.rand(100, 10)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data, data, test_size=0.2, random_state=42)

# Create a sequential model
model = Sequential([
    Dense(32, activation='relu', input_shape=(10,)),
    Dense(64, activation='relu'),
    Dense(1)
])

# Compile the model with an optimizer and loss function
model.compile(optimizer='adam', loss='mse')

# Train the model on the training data
history = model.fit(X_train, y_train, epochs=50, batch_size=32)

# Evaluate the model on the testing data
loss = model.evaluate(X_test, y_test)
print(f"Model accuracy: {loss * 100:.2f}%")
