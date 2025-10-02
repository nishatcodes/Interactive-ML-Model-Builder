# Machine Learning Final Project [Module2]
# Group 10 - Nishat and Emmii Cui
# March/April, 2021
# Data Training Module with functions to process data and predict output

import math
import sklearn
from sklearn.linear_model import LinearRegression


# Function that processes the data
def dataprocess(filename, input_cols, output_col, divider_character,
                transform):
    # Get header
    header = filename.readline().split(divider_character)
    predictors = (header[i] for i in input_cols)
    print('{:s}'.format('\u0332'.join("Predictors:")))
    print(*predictors, sep=", ")
    print('{:s}'.format('\u0332'.join("Output:")))
    print(header[output_col])
    # Initialize lists
    outputs = []
    inputs = []
    for line in filename:
        data = line.strip().split(divider_character)
        # Get predictor information
        predict_info = []
        log_predict_info = []
        predict_inner = [data[i] for i in input_cols]
        for i in predict_inner:
            if i != "":
                predict_info.append(float(i))
        for i in predict_info:
            i = abs(i)
            if i > 0:
                i = math.log(float(i))
            log_predict_info.append(i)
        if transform == "yes":
            if len(log_predict_info) == len(input_cols):
                # Populate list of output
                outputs.append(float(data[output_col]))
                # Populate list of inputs
                inputs.append(log_predict_info)
        else:
            if len(predict_info) == len(input_cols):
                # Populate list of output
                outputs.append(float(data[output_col]))
                # Populate list of inputs
                inputs.append(predict_info)
    return outputs, inputs


# Function for training with sklearn module
def training(inputs, outputs):
    # Get length of training lists
    data_len = len(outputs)
    training_len = int(data_len*.8)
    # Create training output list
    training_output = outputs[:training_len]

    # Create test output list
    test_output = outputs[training_len:]

    # Create training input list
    training_input = inputs[:training_len]

    # Create test input list
    test_input = inputs[training_len:]

    # Step 2 - training the model
    predictor = LinearRegression(n_jobs=-1)
    predictor.fit(X=training_input, y=training_output)
    coefficients = predictor.coef_
    # Step 3 - using our model for prediction
    outcome = predictor.predict(X=test_input)
    coefficients = predictor.coef_
    print("Prediction: " + str(outcome))
    print("Coefficients: " + str(coefficients))

    # Make test output list
    test_output_list = []
    comparison_dict = dict(zip(outcome, test_output))
    return comparison_dict
