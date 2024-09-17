import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

def load_dataset(file_path):
    df = pd.read_csv(file_path)
    
    df.columns = df.columns.str.lower()  
    date_column = df.columns[0]  
    value_column = df.columns[1]  
    df[date_column] = pd.to_datetime(df[date_column])
    df.set_index(date_column, inplace=True)

    return df[[value_column]]

def plot_trend_seasonality(df, period):
    decomposition = seasonal_decompose(df, model='additive', period=period)
    
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

file_path = "C:/Users/Admin/Downloads/winequality-red.csv"

df = load_dataset(file_path)

# Ask user for period of seasonality (e.g., 12 for monthly data over a year)
period = int(input("Enter the period for seasonality (e.g., 12 for monthly data with yearly seasonality): "))

# Plot trend and seasonality
plot_trend_seasonality(df, period)
