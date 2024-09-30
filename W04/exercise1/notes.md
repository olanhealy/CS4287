# Exercise 1
### Implement a perceptron with fixed weights w1 = w2 =1, and bias -0.5 to compute the OR logical gate

perceptron is an artifical neroun used in ml. This is for OR gate. 

We were given w1 and w2 both to 1 and the bias as -0.5. we can represent this as

```
output = w1 . x1 + w2 . x2 + bias
```
the choice of these values ensure the output will correctly showcase the behaviour of OR gate

the pereptron function computes the net input by performing the doy product between the weights and the input vector and then adding the bias

after this is calculted, it is passed to activation function to detemine the output (0, 1)
