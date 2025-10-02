# Machine Learning Final Project [Module 1]
# Group 10 - Nishat and Emmii Cui
# March/April, 2021
# Bar Graph Functions

import turtle


# Dictionary populating function for percentages used for bar graph
def percent_dict(compare_values_dict):
    percentages = []
    for predictedValue, actualValue in compare_values_dict.items():
        if actualValue != 0:
            percentageError = ((abs(actualValue - predictedValue)
                                )/actualValue)*100
            percentages.append(percentageError)

    percentages_dict = {"0 to 10": 0, "10 to 20": 0, "20 to 30": 0,
                        "30 to 40": 0, "40 to 50": 0, "50 to 60": 0,
                        "60 to 70": 0, "70 to 80": 0, "80 to 90": 0,
                        "90 to 100": 0, "Over 100": 0}
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
    return percentages_dict


# Create x and y values for bar graph
def xy_values(a_dict):
    x_vals = []
    y_vals = []
    for key, value in a_dict.items():
        x_vals.append(key)
        y_vals.append(value)
    return x_vals, y_vals


# Create turtle screen function
def screen(t, y_values):
    max_ht = max(y_values)
    numbars = len(y_values)
    border = 20
    wn = turtle.Screen()
    wn.setworldcoordinates(0-border, 0-border, 20*numbars+border,
                           max_ht+border+20)
    wn.bgcolor("lightsteelblue")
    t.speed(0)
    t.color("black", "slategray")
    t.begin_fill()
    t.forward(20*numbars+5)
    t.left(90)
    t.forward(max_ht+10)
    t.left(90)
    t.forward(20*numbars+10)
    t.left(90)
    t.forward(max_ht+10)
    t.left(90)
    t.forward(5)
    t.goto(0, 0)
    t.end_fill()


# Drawing bar graph function
def draw_bar(t, ht):
    t.speed(0)
    t.pensize(2)
    t.begin_fill()
    t.left(90)
    t.forward(ht)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(ht)
    t.left(90)
    t.end_fill()


# Height function for displaying number of outputs
def write_ht(t, ht):
    t.speed(0)
    t.forward(10)
    t.pensize(10)
    t.color("snow")
    t.left(90)
    t.forward(ht+1)
    t.write(str(ht), move=False, align="center",
            font=("Arial", 15, "bold"))
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(ht+1)
    t.left(90)


# Label function for percentage intervals
def label(t, percentage):
    t.speed(0)
    t.forward(10)
    t.color("darkslateblue")
    t.write(str(percentage), move=False, align="center",
            font=("Arial", 10, "bold"))
    t.forward(10)


# Title and x axis and y axis labels
def title(t, title_name, y_values):
    max_ht = max(y_values)
    numbars = len(y_values)
    border = 20
    t.speed(0)
    t.left(90)
    t.forward(max_ht+15)
    t.right(90)
    t.forward((20*numbars+border)/2)
    t.write(title_name, move=False, align="center",
            font=("Arial", 25, "bold", "underline"))
    t.right(90)
    t.forward(max_ht/15)
    t.goto(0, -10)
    t.color("slategray")
    t.write("x-axis: percentage error intervals (%)       "
            "y-axis: number of predicted outputs within "
            "a percentage interval", move=False, align="left",
            font=("Arial", 15, "bold"))
