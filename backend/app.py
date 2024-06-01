# import datetime as dt
# import requests

# def f2c(fahrenheit):
#     celsius = (fahrenheit - 32) * 5 / 9
#     return celsius

# api_key = 'api'

# city = input("Enter city: ")

# weather_data = requests.get(
#     f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}"
# )
# response = weather_data.json()

# temp_f = response['main']['temp']
# temp_c = f2c(temp_f)
# feels_f = response['main']['feels_like']
# feels_c = f2c(feels_f)

# wind_spd = response['wind']['speed']
# humidity = response['main']['humidity']
# description = response['weather'][0]['description']
# sunrise = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
# sunset = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

# print(f"Temperature in {city}: {temp_c:.2f}˚C or {temp_f:.2f}˚F")
# print(f"Temprtature in {city} feels like: {feels_c:.2f}˚C or {feels_f:.2f}˚F")
# print(f"Humidity in {city}: {humidity}%")
# print(f"Wind Speed in {city}: {wind_spd}m/s")
# print(f"General Weather in {city}: {description}")
# print(f"Sun rises in {city} at {sunrise} local time.")
# print(f"Sun sets in {city} at {sunset} local time.")

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import datetime as dt
import requests
from config import API_KEY

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

def f2c(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={API_KEY}"
    )

    if weather_data.status_code != 200:
        return jsonify({'error': 'Failed to fetch weather data'}), weather_data.status_code

    response = weather_data.json()
    
    if 'main' not in response or 'weather' not in response:
        return jsonify({'error': 'Invalid response from weather service'}), 500

    temp_f = response['main']['temp']
    temp_c = f2c(temp_f)
    feels_f = response['main']['feels_like']
    feels_c = f2c(feels_f)
    wind_spd = response['wind']['speed']
    humidity = response['main']['humidity']
    description = response['weather'][0]['description']
    sunrise = dt.datetime.utcfromtimestamp(response['sys']['sunrise'])
    sunset = dt.datetime.utcfromtimestamp(response['sys']['sunset'])

    return jsonify({
        'temp_f': temp_f,
        'temp_c': temp_c,
        'feels_f': feels_f,
        'feels_c': feels_c,
        'wind_spd': wind_spd,
        'humidity': humidity,
        'description': description,
        'sunrise': sunrise.strftime('%Y-%m-%d %H:%M:%S'),
        'sunset': sunset.strftime('%Y-%m-%d %H:%M:%S')
    })

@app.route('/')
def serve_index():
    return send_from_directory('frontend', 'index.html')

@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory('frontend', path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
