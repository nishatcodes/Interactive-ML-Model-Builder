# [Part 2] Building a Model Using Real Data
# Group 10: Nishat Islam and Emmii Cui
# March/April, 2021
# Build a model for SeoulBikeData.csv inlcuding training
# the model, making predictions, and visualizing the
# percentage errors

import sklearn
import turtle
from sklearn.linear_model import LinearRegression


# Turtle Bar Graph Function Definitions
# Draw bar graph function
def draw_bar(t, ht, clr):
    t.speed(0)
    t.pensize(2)
    t.color("pink", clr)
    t.begin_fill()
    t.left(90)
    t.forward(ht)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(ht)
    t.left(90)
    t.end_fill()


# Height function representing number of outputs
def write_ht(t, ht):
    t.speed(0)
    t.pensize(10)
    t.color("darkslategray")
    t.forward(10)
    t.left(90)
    t.forward(ht+2)
    t.write(str(ht), move=False, align="center",
            font=("Arial", 15, "bold"))
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(ht+2)
    t.left(90)


# Label function representing percentage intervals
def label(t, percentage):
    t.speed(0)
    t.forward(10)
    t.color("midnightblue")
    t.write(str(percentage), move=False, align="center",
            font=("Arial", 15, "bold"))
    t.forward(10)


# Title, x and y axis function
def title(t, title_name, y_values):
    max_ht = max(y_values)
    numbars = len(y_values)
    border = 10
    t.speed(0)
    t.left(90)
    t.forward(max_ht+10)
    t.right(90)
    t.forward((20*numbars+border)/2)
    t.write(title_name, move=False, align="center",
            font=("Arial", 30, "bold", "underline"))
    t.goto(0, -10)
    t.color("slategray")
    t.write("x-axis: percentage error intervals (%)       "
            "y-axis: number of predicted outputs within "
            "a percentage interval", move=False, align="left",
            font=("Arial", 15, "bold"))

# Part 2
datafile = open("SeoulBikeData.csv", encoding="latin1")
# Step 1 - Process the data
header = datafile.readline().split(",")
print("Predictors are:", header[2:11])
print("Output is:", header[1])
bike_output = []
bike_input = []
for line in datafile:
    data = line.strip().split(",")
    # Get column of rented bikes
    bike_output.append(float(data[1]))
    # Get columns of predictor information
    predict_info = []
    for i in data[2:11]:
        predict_info.append(float(i))
    bike_input.append(predict_info)

# Get length of training lists
data_len = len(bike_output)
training_len = int(data_len*.8)

# Create training output list
training_output = bike_output[:training_len]

# Create test output list
test_output = bike_output[training_len:]

# Create training input list
training_input = bike_input[:training_len]

# Create test input list
test_input = bike_input[training_len:]

# Step 2 - training the model
predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=training_input, y=training_output)

# Step 3 - using our model for prediction
outcome = predictor.predict(X=test_input)
coefficients = predictor.coef_
print("Prediction: " + str(outcome))
print("Coefficients: " + str(coefficients))

compare_dict = dict(zip(outcome, test_output))

# Step 4 - visualizing the performance of our model
percentages = []
for predictedValue, actualValue in compare_dict.items():
    if actualValue != 0:
        percentageError = ((abs(actualValue - predictedValue)
                            )/actualValue)*100
        percentages.append(percentageError)

# Initialize dictionary for keeping track of outputs
# that fit under each percentage error interval
percentages_dict = {"0 to 10": 0, "10 to 20": 0, "20 to 30": 0, "30 to 40": 0,
                    "40 to 50": 0, "50 to 60": 0, "60 to 70": 0, "70 to 80": 0,
                    "80 to 90": 0, "90 to 100": 0, "Over 100": 0}
for percentage in percentages:
    if percentage <= 10:
        percentages_dict["0 to 10"] += 1
    elif 10 < percentage <= 20:
        percentages_dict["10 to 20"] += 1
    elif 20 < percentage <= 30:
        percentages_dict["20 to 30"] += 1
    elif 30 < percentage <= 40:
        percentages_dict["30 to 40"] += 1
    elif 40 < percentage <= 50:
        percentages_dict["40 to 50"] += 1
    elif 50 < percentage <= 60:
        percentages_dict["50 to 60"] += 1
    elif 60 < percentage <= 70:
        percentages_dict["60 to 70"] += 1
    elif 70 < percentage <= 80:
        percentages_dict["70 to 80"] += 1
    elif 80 < percentage <= 90:
        percentages_dict["80 to 90"] += 1
    elif 90 < percentage <= 100:
        percentages_dict["90 to 100"] += 1
    elif percentage > 100:
        percentages_dict["Over 100"] += 1

# Bar Graphs
# Create Turtle
buns = turtle.Turtle()

# x and y values for bar graph
xs = []
ys = []
for key, value in percentages_dict.items():
    xs.append(key)
    ys.append(value)

# Setting up Turtle screen
max_ht = max(ys)
numbars = len(ys)
border = 10
wn = turtle.Screen()
wn.setworldcoordinates(0-border, 0-border, 20*numbars+border,
                       max_ht+border+20)
wn.bgcolor("lightsteelblue")

# Calling on Turtle Bar Graph functions
colours = ["lightcyan", "paleturquoise", "aquamarine", "turquoise",
           "mediumturquoise", "darkturquoise", "cadetblue",
           "lightseagreen", "darkcyan", "teal", "seagreen"]
clr_index = 0
for a in ys:
    draw_bar(buns, a, colours[clr_index])
    clr_index += 1
buns.penup()
buns.goto(0, 0)
for a in ys:
    write_ht(buns, a)
buns.penup()
buns.goto(0, 0)
for b in xs:
    label(buns, b)
buns.penup()
buns.goto(0, 0)

title(buns, "Rented Bikes in Seoul (Predictions vs Actual)", ys)
buns.hideturtle()

# Turtle screen exit
wn.exitonclick()

input("Please press ENTER to exit.")
