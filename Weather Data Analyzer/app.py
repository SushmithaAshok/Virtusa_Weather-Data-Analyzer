# import the required libraries
import streamlit as st           
import pandas as pd             
import matplotlib.pyplot as plt  
import requests                  
import datetime                  
key = "ENTER YOUR API"
url = "https://api.openweathermap.org/data/2.5/weather"
def fetch_weather(city):
    params = {
        "q":city,         
        "appid":key,      
        "units":"metric"  
    }
    response = requests.get(url, params=params)
    return response.json()
# this function saves the weather data to the CSV using pandas
def save_to_csv(city, temp, humidity, wind):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    new_row = {
        "City": city,
        "Temperature": temp,
        "Humidity": humidity,
        "Wind": wind,
        "Date": date
    }
    try:
        df = pd.read_csv("weather_data.csv")
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    except:
        # if CSV doesnt exist it create new csv
        df = pd.DataFrame([new_row])
    # save dataframe back to CSV
    df.to_csv("weather_data.csv", index=False)
# this function reads the CSV and displays the temperature trend graph
def show_graph():
    try:
        df = pd.read_csv("weather_data.csv")
        fig, ax = plt.subplots()
        # plot date vs temperature
        ax.plot(df["Date"], df["Temperature"], marker="o", color="red")
        ax.set_xlabel("Date & Time")
        ax.set_ylabel("Temperature °C")
        ax.set_title("Temperature Trend")
        plt.xticks(rotation=45)
        plt.tight_layout()
        # display graph in streamlit
        st.pyplot(fig)
    except:
        st.warning("No data yet!")
st.title(" Weather Data Analyzer")
st.write("Get the real time weather data for any of the  city!")
# text input box for the city name
city = st.text_input("Enter City Name", "Chennai")
# when user clicks the Get Weather button
if st.button("Get Weather"):
    data = fetch_weather(city)
    if data["cod"] == 200:
        temp=data["main"]["temp"]
        feels=data["main"]["feels_like"]
        humidity=data["main"]["humidity"]
        wind=data["wind"]["speed"]
        desc=data["weather"][0]["description"]
        country = data["sys"]["country"]
        st.success(f"Weather in the {city}, {country}")
        col1, col2, col3 = st.columns(3)
        col1.metric("🌡️ Temperature", f"{temp}°C")
        col2.metric("💧 Humidity", f"{humidity}%")
        col3.metric("💨 Wind Speed", f"{wind} m/s")
        st.info(f"Feels Like: {feels}°C  |  Condition: {desc}")
        save_to_csv(city, temp, humidity, wind)
        st.success("Data saved to CSV!")
        st.subheader("📈 Temperature Trend")
        show_graph()
    else:
        st.error("City not found!")