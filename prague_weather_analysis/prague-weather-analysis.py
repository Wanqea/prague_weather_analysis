import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os

# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)

# Format dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# Get Prague weather for past week
url = f"https://api.open-meteo.com/v1/forecast?latitude=50.07&longitude=14.43&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()

# Extract the daily data
daily_data = data['daily']

# Create a DataFrame
df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']
})

# Convert date strings to datetime
df['date'] = pd.to_datetime(df['date'])

# ==============================
# NEW ANALYSIS PART
# ==============================

# Calculate daily average temperature
df['avg_temp'] = (df['max_temp'] + df['min_temp']) / 2

# Calculate daily temperature difference (max - min)
df['temp_diff'] = df['max_temp'] - df['min_temp']

# Basic statistics
overall_avg_temp = df['avg_temp'].mean()
max_temp_day = df.loc[df['max_temp'].idxmax()]
min_temp_day = df.loc[df['min_temp'].idxmin()]
max_diff_day = df.loc[df['temp_diff'].idxmax()]

print("\nBasic Analysis:")
print(f"Overall average temperature: {overall_avg_temp:.2f} °C")
print(f"Hottest day: {max_temp_day['date'].date()} ({max_temp_day['max_temp']} °C)")
print(f"Coldest day: {min_temp_day['date'].date()} ({min_temp_day['min_temp']} °C)")
print(f"Largest daily temperature difference: {max_diff_day['date'].date()} ({max_diff_day['temp_diff']} °C)")

# PLOT



plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')
plt.plot(df['date'], df['avg_temp'], marker='o', label='Average Temp')

plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Prague Weather - Past 7 Days')
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('weather_chart.png')
plt.show()


# SAVE DATA

if not os.path.exists('data'):
    os.makedirs('data')

df.to_csv('data/prague_weather.csv', index=False)

print("Data saved to data/prague_weather.csv")