# [Part 3] Building Another Model for Different Data
# Group 10 - Nishat and Emmii Cui
# March/April, 2021
# Build another model for forestfire.csv with the incorporation of
# log tranformation

import sklearn
import turtle
import math
import bargraph
import datatraining
from sklearn.linear_model import LinearRegression

# The UCI Machine Learning Repository mentions that:
# "this output variable is very skewed towards 0.0, thus it may make
# sense to model with the logarithm transform", therefore we are
# showing here the results with and without a log transformation

print("The Forest Fires data will be visualized first, "
      "with the application of log transformation on inputs.")
# Source: https://archive.ics.uci.edu/ml/datasets/Forest+Fires
actual_output, predict_input = datatraining.log_dataprocess(
        "forestfires.csv", 4, 11, 12)

# Create dictionary of predicted values
compare_dict = datatraining.training(predict_input, actual_output)

# Visualizing the performance of our model
final_percent_dict = bargraph.percent_dict(compare_dict)
# Create turtle named "buns"
buns = turtle.Turtle()
# Get x and y values for graph
xs, ys = bargraph.xy_values(final_percent_dict)
# Set up screen
bargraph.screen(buns, ys)
# Draw bars
for a in ys:
    # Distinguish max height by using a different color
    if a == max(ys):
        buns.color("steelblue", "skyblue")
    # Distinguish min height with a different color
    elif a == min(ys):
        buns.color("palevioletred", "lightcoral")
    # Color for the rest of the bars
    else:
        buns.color("powderblue", "lightcyan")
    bargraph.draw_bar(buns, a)
buns.penup()
buns.goto(0, 0)
# Label height (i.e. the number of outputs)
for a in ys:
    bargraph.write_ht(buns, a)
buns.penup()
buns.goto(0, 0)
# Label percentage intervals
for b in xs:
    bargraph.label(buns, b)
# Title, x-axis and y-axis
buns.goto(0, 0)
bargraph.title(buns, "Forest Fire Areas Log-Transformed "
               "(Predicted vs Actual)", ys)
buns.hideturtle()

# Resetting Turtle Screen and move on to next visualization
input("Please press ENTER to see the graph for data without "
      "log transformation.")
buns.reset()

# Log transformed data
actual_output, predict_input = datatraining.dataprocess(
        "forestfires.csv", 0, 11, 12)

# Create dictionary of predicted values
compare_dict = datatraining.training(predict_input, actual_output)

# Step 4 - visualizing the performance of our model
final_percent_dict = bargraph.percent_dict(compare_dict)

# Get x and y values for graph
xs, ys = bargraph.xy_values(final_percent_dict)
# Set up screen
bargraph.screen(buns, ys)
# Draw bars
for a in ys:
    if a == max(ys):
        buns.color("steelblue", "skyblue")
    elif a == min(ys):
        buns.color("palevioletred", "lightcoral")
    else:
        buns.color("powderblue", "lightcyan")
    bargraph.draw_bar(buns, a)
buns.penup()
buns.goto(0, 0)
# Label height
for a in ys:
    bargraph.write_ht(buns, a)
buns.penup()
buns.goto(0, 0)
# Label percentage intervals
for b in xs:
    bargraph.label(buns, b)
# Title x-axis and y-axis
buns.goto(0, 0)
bargraph.title(buns, "Forest Fire Areas (Predicted vs Actual)", ys)
buns.hideturtle()

# Conclusion
print("There are 8 less predictions that are more than 100% away "
      "from the actual value for log-transformed data vs data "
      "with no transformation")
# Exit turtle screen
turtle.exitonclick()

# Program exit
input("Please press ENTER to exit")
