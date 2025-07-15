import requests
import json
from quixstreams import Application

def fetch_weather():
    """Fetch weather data from Open-Meteo API for London"""
    try:
        response = requests.get(
            "https://api.open-meteo.com/v1/forecast", 
            params={
                "latitude": 51.52,
                "longitude": -0.11,
                "current_weather": True,
                "current": "temperature_2m",
                "timezone": "Europe/London",
            }
        )
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def send_to_kafka(weather_data):
    """Send weather data to Kafka topic"""
    if not weather_data:
        print("No weather data to send")
        return
    
    app = Application(
        broker_address="localhost:9092",
        loglevel="DEBUG",
    )

    try:
        with app.get_producer() as producer:
            producer.produce(
                topic="weather_data_demo",
                key="London",
                value=json.dumps(weather_data),
            )
        print("Weather data sent to Kafka successfully!")
    except Exception as e:
        print(f"Error sending data to Kafka: {e}")

if __name__ == "__main__":
    # Fetch weather data
    weather = fetch_weather()
    
    # Send to Kafka
    send_to_kafka(weather)