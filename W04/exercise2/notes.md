# Exercise 2
### Implement a perceptron that uses the perceptron training rule to learn the logical AND ga

The and is only true when inputs are 1 and 1

this time, we arent given the weights and we need to use threshold

w1 and w2 are initalised randomly and multipled by 10, roudned to one decimal place. This helps the learning as its random from inital conditions

The main body is a loop which goes of 1000 times, with a learning rate of 0.1

in each interation, the total error across all examples is accumulated, 

for every input, the weigjted sum is calculated with
fnet = activation(np.dot([w1, w2], input) - theta)

ten the erro is the difference between the expected output and the wighted sum

the weights and threshold are then updated using the perceptron training rule