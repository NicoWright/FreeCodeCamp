import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)
df.index = pd.to_datetime(df.index)

# Clean data
df = df = df[
    (df['value'] > df['value'].quantile(0.025)) &
    (df['value'] < df['value'].quantile(0.975))
]

def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(24,6))
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.plot(df.index, df.value);

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    months = {
    1:'January',
    2:'February',
    3:'March',
    4:'April',
    5:'May',
    6:'June',
    7:'July',
    8:'August',
    9:'September',
    10:'October',
    11:'November',
    12:'December'}
    hue_order = ['January','February','March','April','May','June','July','August','September','October','November','December']

    df_bar = df.copy()
    df_bar['Years'] = df.index.year
    df_bar['Months'] = df.index.month.map(months)
    df_bar = df_bar.groupby(['Years','Months'], as_index=False)['value'].mean()

    # Draw bar plot
    fig = plt.figure(figsize=(12,6))
    sns.barplot(data=df_bar, x='Years', y='value', hue='Months', hue_order=hue_order)
    plt.title('Daile freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.ylabel('Average Page Views')
    plt.xlabel('Years')
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1,2, figsize=(18,6))
    ax1 = axes[0]
    sns.boxplot(data=df_box, x='year', y='value', ax=ax1)
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    ax1.set_title('Year-wise Box Plot (Trend)')

    ax2 = axes[1]
    sns.boxplot(data=df_box, x='month', y='value', ax=ax2, order=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    ax2.set(xlabel='Month', ylabel='Page Views', title='Month-wise Box Plot (Seasonality)')





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
