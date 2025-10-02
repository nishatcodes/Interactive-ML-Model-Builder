# Machine Learning Final Project [Module2]
# Group 10 - Nishat Islam and Emmii Cui
# March/April, 2021
# Data Training Module with functions to process data and predict output

import math
import sklearn
from sklearn.linear_model import LinearRegression


# Function for processing data with continuous predictor columns
def dataprocess(filename, input_start, input_end, output_col):
    day_dict = {"mon": 1, "tue": 2, "wed": 3, "thu": 4, "fri": 5,
                "sat": 6, "sun": 7}
    month_dict = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5,
                  "jun": 6, "jul": 7, "aug": 8, "sep": 9, "oct": 10,
                  "nov": 11, "dec": 12}
    datafile = open(filename, encoding="latin1")
    header = datafile.readline().split(",")
    print('{:s}'.format('\u0332'.join("Predictors:")))
    print(*header[input_start:input_end+1], sep=", ")
    print('{:s}'.format('\u0332'.join("Output(s):")))
    print(header[output_col])
    # Initialize input/output lists
    outputs = []
    inputs = []
    for line in datafile:
        data = line.strip().split(",")
        # Get column of output
        outputs.append(float(data[output_col]))
        # Get columns of predictor information
        predict_info = []
        for i in data[input_start:input_end+1]:
            for k, v in day_dict.items():
                if i == k:
                    i = v
            for key, value in month_dict.items():
                if i == key:
                    i = value
            predict_info.append(float(i))
        inputs.append(predict_info)
    return outputs, inputs


# Function definition includes a log transformation
def log_dataprocess(filename, input_start, input_end, output_col):
    day_dict = {"mon": 1, "tue": 2, "wed": 3, "thu": 4, "fri": 5,
                "sat": 6, "sun": 7}
    month_dict = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5,
                  "jun": 6, "jul": 7, "aug": 8, "sep": 9, "oct": 10,
                  "nov": 11, "dec": 12}
    datafile = open(filename, encoding="latin1")
    header = datafile.readline().split(",")
    print('{:s}'.format('\u0332'.join("Predictors (log transformed):")))
    print(*header[input_start:input_end+1], sep=", ")
    print('{:s}'.format('\u0332'.join("Output(s):")))
    print(header[output_col])
    # Initialize input/output lis
    outputs = []
    inputs = []
    for line in datafile:
        data = line.strip().split(",")
        # Get column of output
        outputs.append(float(data[output_col]))
        # Get columns of predictor information
        predict_info = []
        for i in data[input_start:input_end+1]:
            for k, v in day_dict.items():
                if i == k:
                    i = v
            for key, value in month_dict.items():
                if i == key:
                    i = value
            i = abs(float(i))
            if i > 0:
                i = math.log(float(i))
            predict_info.append(i)
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
