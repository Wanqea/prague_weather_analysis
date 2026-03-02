# Prague Weather Analysis

This project retrieves the past 7 days of weather data for Prague using the Open-Meteo API and performs basic time-series analysis on daily temperature data.

## Project Overview

The script:

- Fetches historical weather data via REST API
- Processes the data using Pandas
- Calculates daily average temperature
- Computes daily temperature difference (max - min)
- Identifies the hottest and coldest days
- Determines the day with the largest temperature variation
- Visualizes temperature trends using Matplotlib
- Exports the dataset to CSV format

This project demonstrates API integration, feature engineering, basic statistical analysis, and time-series visualization in Python.

## Technologies Used

- Python
- Requests
- Pandas
- Matplotlib
1. Install dependencies:

pip install -r requirements.txt

2. Run the script:

python prague_weather.py

## Output

The script generates:

- weather_chart.png (temperature visualization)
- data/prague_weather.csv (processed dataset including engineered features)

The exported dataset includes the following columns:

- date
- max_temp
- min_temp
- avg_temp
- temp_diff