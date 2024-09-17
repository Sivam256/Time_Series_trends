import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Function to load the dataset and automatically handle the time-series data
def load_dataset(file_path):
    # Load the dataset from the file
    df = pd.read_csv(file_path)
    
    # Automatically detect date and value columns
    # Assuming the first column is the time-series and the second column is the value
    df.columns = df.columns.str.lower()  # Convert all column names to lowercase
    date_column = df.columns[0]  # Assuming the first column is the date/time
    value_column = df.columns[1]  # Assuming the second column is the data values

    # Parse the date column and set it as the index
    df[date_column] = pd.to_datetime(df[date_column])
    df.set_index(date_column, inplace=True)

    return df[[value_column]]

# Function to perform decomposition and plot results
def plot_trend_seasonality(df, period):
    # Decomposition using seasonal_decompose
    decomposition = seasonal_decompose(df, model='additive', period=period)
    
    # Plotting the components
    plt.figure(figsize=(10, 8))
    
    plt.subplot(411)
    plt.plot(df, label='Original Data')
    plt.legend(loc='upper left')

    plt.subplot(412)
    plt.plot(decomposition.trend, label='Trend', color='orange')
    plt.legend(loc='upper left')

    plt.subplot(413)
    plt.plot(decomposition.seasonal, label='Seasonality', color='green')
    plt.legend(loc='upper left')

    plt.subplot(414)
    plt.plot(decomposition.resid, label='Residuals', color='red')
    plt.legend(loc='upper left')
    
    plt.tight_layout()
    plt.show()

# Main execution
file_path = "C:/Users/Admin/Downloads/winequality-red.csv"

# Load the dataset
df = load_dataset(file_path)

# Ask user for period of seasonality (e.g., 12 for monthly data over a year)
period = int(input("Enter the period for seasonality (e.g., 12 for monthly data with yearly seasonality): "))

# Plot trend and seasonality
plot_trend_seasonality(df, period)
