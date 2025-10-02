# ML Pipeline

Machine learning applications for predictive modeling with Python and scikit-learn.

## Datasets

- **Part 2: Seoul Bike Sharing Demand**
  - Source: UCI Machine Learning Repository
  - Time Period: 2017-2018
  - Variables: Hourly bike rentals, temperature, humidity, rainfall, seasons, etc.
  - Preprocessing: Selected 9 numeric features, 80/20 train-test split

- **Part 3: Forest Fires**
  - Source: UCI Machine Learning Repository
  - Variables: Spatial and temporal data, weather conditions, burned area
  - Preprocessing: Applied log transformation to address skewness (as recommended by dataset source)

- **Part 1: Synthetic Data**
  - Generated 100 samples of 3 random integers (1-1000) and output y = 1*x1 + 2*x2 + 3*x3

## Key Features

- **Data Processing:** Automated CSV parsing, configurable input/output columns, log transformation
- **Model Development:** Linear regression for numerical prediction
- **Model Validation:** Percentage error analysis across prediction intervals
- **Visualization:** Custom bar charts showing prediction accuracy distribution
- **Interactive Application:** User-friendly CLI for processing custom datasets

## Projects

### Part 1: Synthetic Data Model
- Built a linear regression model on synthetic data to verify the algorithm
- Model successfully learned the coefficients (1,2,3) and made accurate predictions

### Part 2: Bike Sharing Demand Prediction
- Linear regression model trained on 9 features to predict hourly bike rentals
- Visualized prediction accuracy with custom bar charts

### Part 3: Forest Fire Area Prediction
- Compared model performance with and without log transformation
- Log transformation improved predictions (reduced number of high-error predictions)

### Part 4: Interactive Model Building
- Modular application that allows users to upload CSV files and configure the model
- Supports custom input/output columns, data transformations, and visualization

## Technologies Used

- **Programming Language:** Python
- **Machine Learning:** scikit-learn, Linear Regression
- **Visualization:** Python Turtle graphics
- **Data Processing:** CSV handling, feature selection, log transformation

## Key Findings

- Linear regression effectively captures relationships in various datasets
- Log transformation can improve model performance on skewed data
- Modular application design enables rapid prototyping with new datasets
- Custom visualization provides intuitive model performance assessment

## How to Run

1. Install required packages: `pip install scikit-learn`
2. Run each part individually:
   - Part 1: `python part1.py`
   - Part 2: `python part2.py`
   - Part 3: `python part3.py`
   - Part 4: `python part4.py`

## Results

The pipeline successfully processes real-world data, trains predictive models, and visualizes accuracy. The interactive application extends functionality to handle custom datasets with flexible configuration.

## Authors

Nishat Islam, Emmii Cui

## Course Context

This project was completed as part of CMPT 120 - Introduction to Programming at Simon Fraser University, Spring 2021.

## References

- Seoul Bike Sharing Dataset: UCI Machine Learning Repository
- Forest Fires Dataset: UCI Machine Learning Repository
- scikit-learn: Machine Learning in Python
