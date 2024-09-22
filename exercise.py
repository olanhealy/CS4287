import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# href https://machinelearningmastery.com/implement-perceptron-algorithm-scratch-python/

# Load csv for data ( just said make two lineraly seperable ones, could have generated did myself)
df = pd.read_csv('data.csv')

# Separate the features and labels from csv
X = df[['Feature1', 'Feature2']].values
y = df['Label'].values

# weights and bias
weights = np.zeros(X.shape[1])  
bias = 0
learning_rate = 0.1
num_epochs = 100

# training of perceptron
for epoch in range(num_epochs):
    for i in range(len(X)):
        
        linear_output = np.dot(X[i], weights) + bias
        prediction = 1 if linear_output >= 0 else 0
        error = y[i] - prediction
        weights += learning_rate * error * X[i]
        bias += learning_rate * error

print(f"Weights: {weights}")
print(f"Bias: {bias}")


# plot points from csv
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr', edgecolor='k')

# calculate decision boundary
x_vals = np.linspace(X[:, 0].min() - 1, X[:, 0].max() + 1, 100)
y_vals = -(weights[0] * x_vals + bias) / weights[1]

# plot decision boundary
plt.plot(x_vals, y_vals, '--', color='black')
plt.xlim(X[:, 0].min() - 1, X[:, 0].max() + 1)
plt.ylim(X[:, 1].min() - 1, X[:, 1].max() + 1)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Manual Perceptron Decision Boundary')
plt.grid()
plt.show()
