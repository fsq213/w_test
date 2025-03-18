import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('temperature_data.csv', parse_dates=['timestamp'])

data['rolling_mean'] = data.groupby('city')['temperature'].transform(lambda x: x.rolling(window=30).mean())
data['rolling_std'] = data.groupby('city')['temperature'].transform(lambda x: x.rolling(window=30).std())
data['anomaly'] = (data['temperature'] > data['rolling_mean'] + 2 * data['rolling_std']) | \
                  (data['temperature'] < data['rolling_mean'] - 2 * data['rolling_std'])

def plot_temperature(city):
    city_data = data[data['city'] == city]
    plt.figure(figsize=(15, 7))
    plt.plot(city_data['timestamp'], city_data['temperature'], label='Temperature', color='blue')
    plt.plot(city_data['timestamp'], city_data['rolling_mean'], label='Rolling Mean', color='orange')
    plt.scatter(city_data[city_data['anomaly']]['timestamp'], city_data[city_data['anomaly']]['temperature'],
                color='red', label='Anomalies')
    plt.title(f'Temperature Analysis for {city}')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.show()



if __name__ == "__main__":
    df = open_data()
    X_df, y_df = preprocess_data(df)
    plot_temperature('Berlin')
