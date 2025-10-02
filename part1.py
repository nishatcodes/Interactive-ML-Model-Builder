# [Part 1] Building our first Machine Learning Model
# Group 10: Nishat Islam and Emmii Cui
# March/April, 2021
# Build our first Machine Learning Model using random
# numbers for x values (inputs) to calculate y values
# (outputs). Train the model and predict outputs

import random
import sklearn
from sklearn.linear_model import LinearRegression
import turtle
# Step 1
# c1 = 1
# c2 = 2
# c3 = 3

# Step 2 - generating a training set
# Initialize input list
input_list = []

# Initialize output list
output_list = []
for i in range(100):
    # Use random to generate integers between 1 and 1000, inclusive
    x1 = random.randint(1, 1001)
    x2 = random.randint(1, 1001)
    x3 = random.randint(1, 1001)
    c1 = 1
    c2 = 2
    c3 = 3
    x_values = [x1, x2, x3]
    input_list.append(x_values)
    # Calculate y-values
    y_value = (x1*c1 + x2*c2 + x3*c3)
    output_list.append(y_value)

# Step 3 - training the machine learning model
train_input = input_list
train_output = output_list

predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=train_input, y=train_output)

# Step 4 - using out model for prediction
X_test = [[10, 20, 30]]
outcome = predictor.predict(X=X_test)
coefficients = predictor.coef_
print("Prediction: " + str(outcome))
print("Coefficients: " + str(coefficients))

input("Please press ENTER to exit")
