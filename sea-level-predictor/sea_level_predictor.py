import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    line1 = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    # y = mx + c
    line1_x = df['Year']
    line1_y = line1.slope * line1_x + line1.intercept
    plt.scatter(line1_x, line1_y)
    
    # Create second line of best fit
    df2 = df[df['Year']>=2000]
    line2 = linregress(x=df2['Year'], y=df2['CSIRO Adjusted Sea Level'])
    # y = mx + c
    line2_x = df2['Year']
    line2_y = line2.slope * line2_x + line2.intercept
    plt.scatter(line2_x, line2_y)
    
    # Add labels and title
    plt.figure(figsize=(12,9))
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)') 
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
