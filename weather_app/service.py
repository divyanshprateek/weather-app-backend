import requests 
from config import API_KEY

def fetch_weather_data(zip_code):
    response = requests.get(f"http://api.weatherstack.com/current?access_key={API_KEY}&query={zip_code}")
    return response.json()