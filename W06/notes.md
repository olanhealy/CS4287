# Lab
So seems want you to understand certain stuff used in the labs
# CIFAR-10
 https://www.cs.toronto.edu/~kriz/cifar.html
- 60,000 32x32 colour images in 10 classes, with 6000 images per class. 
- 50000 training, 10000 test
- test batch contains 1000 randomly selected images from each class
- classes are mutally exclusive. No overlap between automobiles and tricks
# Dropout
https://www.baeldung.com/cs/ml-relu-dropout-layers#:~:text=In%20this%20tutorial,%20we%E2%80%99ll%20study%20two%20fundamental

- Is a mask that nullifies the contribution of some neurons towards the next layer and leaves unmodified all others
- Can apply dropout layer to the input vector,v in which case it nullifies some its features; but we can also apply it to hidden layer, in which case it nullifies some hidden neurons
- Important in CNNs because prevent overfitting on the training data. If they aren't present, first bathc of training samples influences the learning in a disproportionatley high manner.
- This in turn would prevent the learning of features that appear only in later samples or batches

# Batch Normalisation
https://www.baeldung.com/cs/batch-normalization-cnn

- is a normalisation technique done between the layers of a Neural Network instead of in the raw data. 
- Its done along mini-batches instead of the full data set. It serves to speed up training and use higher learning rate, which makes learning easier
- Z^N = (z - mz / Sz)
- mz = mean of the nuerons output,   sz = standard deviation of the neurons output

## How its applied?
3.2 in link, images so cant really write

## Batch Normalisation in Convolutional Neural Networks
- In convolutions, we have shared filters that go along the feature maps of the input(in images, the feature map ins generally the height and width)
- These filters are the same on every feature map. It is then reasonable to normalise the output, in the same way sharing it over the feature maps
- This means the parameters used to normalise are calculated along with each entier feature map. 
- In regular Batch norm, each feature would have a different mean and SD
- Here, each feature map *will have a single mean and SD* used on all the features it contains

# Softmax
https://www.analyticsvidhya.com/blog/2021/04/introduction-to-softmax-for-neural-network/
- It is an activation function. NN needs activation function, otherwise just linear regression

**CHARACTERISTICS**
- *NORMALISATION:* The softmax function normalises the input values into a probability distribution, ensuring the sum of all output values is 1
- Makes it suitable for classification problems where output needs to represent probabilites over multiple classes
- *Exponentation:* By exponentiating the inputs, softmax amplifies the differences in the input values, making the largest value more pronounced in output probabilites
- *Differentiability:* Softmax function is differentiable and is essential for **BACKPROPOGATION** in neural Netwroks



## Why Softmax is used in CNN
transfroms the logits into a probability distribution. This method is cucial in determining the loss function during model training and optimisation. CNNs aility to make precise predictions hinges on these fundamental principles

How softmax function in ml is used in CNN:
- *CNN PROCESSES IMAGE** the cnn takes an image as an input and performs various convolutional and pooling operations to extract features
- *FINAL LAYER GENERATES LOGITS:* After processing, the final layer of the CNN outputs a set of numners called logits. These logits represent the raw scores or activation levels for each class the CNN can classify. There will be one logit for each class
- *SOFTMAX TAKES OVER* The softmax function takes these logits as input
- *EXPONENTIATION* softmax function applies an exponenet function (often exex) to each logit value. This emphasizes the differences between the logits, making higher scoring classes stand out more
- *NORMALISATION* softmax function then divides each exponentiated value by the sum of all the exponentiated values, ensuring the final output adds up to 1
- *PROBABILITY DISTRIBUTION* The result is a vector of numbers between 0 and 1, representing probabilites. Each value corresponds to the probability of the image belonging to a specific class
- *DECISION AND INTERPRETATION* The class with the highest probabilty value is CNNS predicted class, This probability value also reflects CNNs confidence level in its prediction
