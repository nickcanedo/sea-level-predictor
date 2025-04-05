import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot from sea level rise data
    fig, ax = plt.subplots()
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='CSIRO Adjusted Sea Level Data')

    # Obtain the linear regression object
    linear_regression = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Get the slope and y-intercept of the line of best fit from our linear regression object
    slope = linear_regression[0]
    y_intercept = linear_regression[1]
    
    # Create a dataset from Year: [1880, 2050] that uses the linear regression with equation y_regression = slope*x + y_intercept
    x_regression = np.arange(1880, 2051)
    y_regression = slope * x_regression + y_intercept

    # Plot the first regression line extrapolating to 2050
    ax.plot(x_regression, y_regression, color='red', label='Linear Regression from 1880', linestyle='--')

    # Create a new linear regression using only the data from 2000 onwards and plot it
    df_2000 = df[df['Year'] >= 2000]
    linear_regression_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    
    # Get the slope and y-intercept of the second line of best fit from our linear regression object
    slope_2000 = linear_regression_2000[0]
    y_intercept_2000 = linear_regression_2000[1]
    
    # Create a dataset from Year: [2000, 2050] that uses the linear regression with equation y_regression = slope*x + y_intercept
    x_regression_2000 = np.arange(2000, 2051)
    y_regression_2000 = slope_2000 * x_regression_2000 + y_intercept_2000

    # Plot the second regression line extrapolating to 2050
    ax.plot(x_regression_2000, y_regression_2000, color='green', label='Linear Regression from 2000', linestyle='--')

    # Add legend, title, and labels to our plot
    ax.legend()
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()