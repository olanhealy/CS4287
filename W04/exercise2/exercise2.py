# Implement a perceptron that uses the perceptron training rule to learn the logical AND ga
# perceptrong training rule: slide 10 W03 part 1. need to implement this
import numpy as np

# Random initialization of weights and theta
w = np.random.rand(1, 3) * 10
w_1 = np.round(w[0][0], 1)
w_2 = np.round(w[0][1], 1)
theta = np.round(w[0][2], 1)

# Inputs and expected outputs for the AND gate
inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
inputsArray = np.array(inputs)
expected_output = np.array([0, 0, 0, 1])  # AND gate outputs

# Activation function
def activation(act):
    if act > 0:
        return 1
    else:
        return 0
    



max_it = 1000
learning_rate = 0.1
errors = []

# Training loop
for t in range(max_it):
    total_error = 0
    for i in range(len(inputsArray)):
        # Calculate the weighted sum and apply the activation function
        f_net = activation(np.dot(np.array([w_1, w_2]), inputsArray[i]) - theta)
        error = expected_output[i] - f_net
        
        # Update weights and threshold
        w_1 += learning_rate * error * inputsArray[i][0]
        w_2 += learning_rate * error * inputsArray[i][1]
        theta -= learning_rate * error  # Decrement theta

        # Accumulate total error for this iteration
        total_error += abs(error)
    
    errors.append(total_error)
    
    # Stop if there are no errors
    if total_error == 0:
        print(f"Training completed in {t + 1} iterations.")
        break

print("Final weights:")
print("w_1:", w_1)
print("w_2:", w_2)
print("Final theta:", theta)

# Testing the trained perceptron
print("Testing the trained perceptron:")
for test_input in inputsArray:
    output = activation(np.dot(np.array([w_1, w_2]), test_input) - theta)
    print(f"LogicGate {test_input}: {output}")
