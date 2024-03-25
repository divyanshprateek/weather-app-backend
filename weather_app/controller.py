from concurrent.futures import ThreadPoolExecutor
executor = ThreadPoolExecutor(max_workers=3)
from weather_app.service import fetch_weather_data

class WeatherController:
    
    def __init__(self, zip_codes) -> None:
        self.zip_codes = zip_codes

    def  get_weather_response(self):
        weather_data = list(executor.map(fetch_weather_data, self.zip_codes))
        
        return weather_data
