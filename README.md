# Weather Streaming with Kafka

Simple app that grabs weather data from London and streams it to Kafka using QuixStreams.

## What it does

- Fetches current weather from Open-Meteo API
- Sends the data to a Kafka topic called `weather_data_demo`
- That's it

## Running it

1. Start Kafka:
```bash
docker-compose up -d
```

2. Run the script:
```bash
pip install -r requirements.txt
python main.py
```

The weather data gets pushed to Kafka and you'll see "Weather data sent to Kafka successfully!" if it works.

## What you get

Temperature, wind speed, and other weather info for London in JSON format streaming through Kafka. 