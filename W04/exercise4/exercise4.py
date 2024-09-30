import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

# Perceptron implementation 
class CustomPerceptron(object):  
    def __init__(self, n_iterations=1000, random_state=1, learning_rate=0.001):  
        self.n_iterations = n_iterations  
        self.random_state = random_state  
        self.learning_rate = learning_rate  
        self.testScore = []  
        self.trainScore = [] 

    ''' 
    Stochastic Gradient Descent 
    1. Weights are updated based on each training example. 
    2. Learning of weights can continue for multiple iterations 
    3. Learning rate needs to be defined 
    ''' 
    def fit(self, X, y): 
        rgen = np.random.RandomState(self.random_state) 
        self.coef_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1]) 
        
        for _ in range(self.n_iterations): 
            for xi, expected_value in zip(X, y): 
                predicted_value = self.predict(xi) 
                self.coef_[1:] += self.learning_rate * (expected_value - predicted_value) * xi 
                self.coef_[0] += self.learning_rate * (expected_value - predicted_value) * 1 

    ''' 
    Net Input is the sum of weighted input signals 
    ''' 
    def net_input(self, X): 
        weighted_sum = np.dot(X, self.coef_[1:]) + self.coef_[0] 
        return weighted_sum 

    ''' 
    Activation function is fed the net input and the unit step function 
    is executed to determine the output. 
    ''' 
    def activation_function(self, X): 
        weighted_sum = self.net_input(X) 
        return np.where(weighted_sum >= 0.0, 1, 0) 

    ''' 
    Prediction is made on the basis of the output of the activation function 
    ''' 
    def predict(self, X): 
        return self.activation_function(X) 

    ''' 
    Model score is calculated based on the comparison of 
    expected value and predicted value 
    ''' 
    def score(self, X, y, switch): 
        misclassified_data_count = 0 
        for xi, target in zip(X, y): 
            output = self.predict(xi) 
            if target != output: 
                misclassified_data_count += 1 
                
        total_data_count = len(X) 
        self.score_ = (total_data_count - misclassified_data_count) / total_data_count 
        
        if switch == "train": 
            self.trainScore.append(self.score_) 
        else: 
            self.testScore.append(self.score_) 
        
        return self.score_


# Load the breast cancer dataset
bc = datasets.load_breast_cancer()
X = bc.data
y = bc.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# Initialize and fit the perceptron
prcptrn = CustomPerceptron()
prcptrn.fit(X_train, y_train)

# Get the scores for the test and training sets
test_score = prcptrn.score(X_test, y_test, "test")
train_score = prcptrn.score(X_train, y_train, "train")

print("Test Score:", test_score)
print("Train Score:", train_score)

