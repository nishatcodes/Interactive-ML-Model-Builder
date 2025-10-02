# [Part 4] Interactive Model Building
# Group 10 - Nishat and Emmii Cui
# March/April, 2021
# Build an interactive model that accepts user inputs

import sklearn
import turtle
import bargraph
import datatraining
from sklearn.linear_model import LinearRegression

# User-friendly intro
print("""
~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~
WELCOME TO OUR INTERACTIVE APPLICATION!
Here, you will be able to run your dataset through our model-training AI,
compare its predictions to some of your output data and visualize it.
How cool is that?!

<<STEPS>>
1. Provide a csv file name,
2. Provide, separator character, input columns, and output column
3. Decide whether or not to apply a log transformation
4. Sit back and let our model do the training and predicting
5. Enjoy the beautiful visuals that show you how close our model's predictions
   are compared to your actual outputs via percentage errors.

Ready? HERE WE GO!
~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~
""")

print("**PLEASE NOTE: all column index start at 0, program takes CSV files "
      "with header on first or second row only**")
more_data = True
while more_data:
    try:
        # Ask user for file name
        file_name = input("Please provide your file name (include .csv): ")
        data_file = open(file_name, encoding="latin1")
    except (ValueError, FileNotFoundError, OSError, NameError):
        print("Sorry, invalid file name entered, please try again.")
        continue
    try:
        # Ask user whether or not headers are on first row
        row1_header = input("Are the headers on the first row? "
                            "(Yes/No): ").lower().strip(" .?!")
        if row1_header == "no":
            next(data_file)
        else:
            pass
        div_char = input("Is your data separated by commas (,) or semnicolons "
                         "(;)? (Please enter , or ;) ")
        # Ask if all input/predictor data columns continuous
        continuous = input("Are your predictor/input data columns continuous? "
                           "(Yes/No): ").lower().strip(" .?!")
        if continuous == "yes":
            # Ask user for input columns start and end
            print('{:s}'.format('\u0332'.join("Please provide THREE "
                                              "numbers:")))
            input_col_start, input_col_end, output_column \
                             = (input("""first input column index,
last input column index,
output column index,
*(separate each input with a comma): """)
                                ).split(",")
            # Convert input list interval to list of input columns
            input_columns = list(range(int(input_col_start),
                                       int(input_col_end)+1))
        elif continuous == "no":
            # Ask user for input columns
            columns = input("Please list all input column indices (separate "
                            "each input with a comma): ").split(",")
            output_column \
                = input("Please provide output column index: ")
            input_columns = [int(number) for number in columns]
        else:
            print("Sorry that was an invalid input")
            continue
        # Ask user to provide name for title
        Title = input("Please provide a title for your bargraph: ")
        # Ask if data needs to be transformed
        log_transform = input("Would you like to apply the log "
                              "transformation? (Yes/No): ")\
            .lower().strip(" .!?")
        actual_output, predict_input =\
               datatraining.dataprocess\
               (data_file, input_columns, int(output_column),
                div_char, log_transform)
    except (ValueError, OSError, NameError):
        print("Sorry, invalid input or error encountered, please start over.")
        continue
    # Create dictionary of predicted values and actual output values
    compare_dict = datatraining.training(predict_input, actual_output)

    # Step 4 - visualizing the performance of our model
    final_percent_dict = bargraph.percent_dict(compare_dict)

    # Create turtle
    buns = turtle.Turtle()

    # Populate x and y values
    xs, ys = bargraph.xy_values(final_percent_dict)

    # Set up turtle screen
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
    buns.goto(0, 0)
    # Title
    bargraph.title(buns, Title, ys)
    buns.hideturtle()

    process_data = input("Would you like to train and visualize another "
                         "set of data? (Yes/No): ").lower().strip(" .?!")
    if process_data == "yes":
        more_data = True
        # Reset turtle screen
        buns.reset()
    else:
        more_data = False

turtle.exitonclick()

input("Please press ENTER to exit")
