# Implement a perceptron with fixed weights w1 = w2 =1, and bias -0.5 to compute the OR logical gate.
import numpy as np

def orGate(x):
    w = np.array([1,1])
    bias = -0.5
    return perceptron(x, w, bias)

def perceptron(x, w, bias):
# preceptron should be w1 * x1 + w2 * x2 + bias

    place = np.dot(w,x) + bias
    act = activation(place)
    return act

def activation(act):
    if act >= 0:
        return 1
    else:
        return 0
    
# Now we need to do the tests for the OR gate
# 00
# 01
# 10
# 11

test_cases = [np.array([0, 0]), np.array([0, 1]), np.array([1, 0]), np.array([1, 1])]
print("Exercise 1: OR gate perceptron")
for i, test in enumerate(test_cases):
    result = orGate(test)
    print(f"Test case {i + 1}: Input {test} -> Output: {result}")






