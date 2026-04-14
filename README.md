# 🌤️ Weather Data Analyzer

A Python web application that fetches real-time weather data,
displays it in a clean web interface and shows temperature
trend graphs over time.

---

## Project Information

For this assignment, I created a connection to the
OpenWeatherMap API and developed a solution to work with
real-world weather datasets. The application allows users
to search for any city and view current weather conditions.
All weather data fetched is automatically saved to a CSV
file which allows the user to track and compare temperature
trends over time through an interactive graph.

---

## Project Files

- `app.py` - Main streamlit web application
- `weather_data.csv` - Historical weather data
  (automatically created when program runs)

---

## Technologies Used

- Python Programming Language
- Streamlit - For web interface
- Pandas - For data handling and CSV management
- Matplotlib - For temperature trend graph
- OpenWeatherMap API - For real-time weather data
- Requests Library - For API calls
- Datetime Module - For timestamps

---

## Libraries Used

- `streamlit` - Used to create the web interface
- `pandas` - Used to manage and store weather data in CSV
- `matplotlib` - Used to produce the temperature trend graph
- `requests` - Used to fetch data from OpenWeatherMap API
- `datetime` - Used to create timestamps for weather records

---

## How to Run

1. Install required libraries:
   pip install streamlit pandas matplotlib requests

2. Get free API key from:
   https://openweathermap.org

3. Replace API key in app.py:
   key = "your_api_key_here"

4. Run the application:
   streamlit run app.py

5. Browser will open automatically at:
   http://localhost:8501

---

## Features

- Real-time weather data using OpenWeatherMap API
- Clean web interface built with Streamlit
- Displays temperature, humidity, wind speed and condition
- Shows feels like temperature and weather condition
- Automatically saves weather history to CSV using Pandas
- Interactive temperature trend graph using Matplotlib

---

## Concepts Used

- Functions
- API integration using requests library
- Dictionary data structure
- File handling using Pandas
- Data visualization using Matplotlib
- Web interface using Streamlit
