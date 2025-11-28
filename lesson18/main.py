import requests
from dotenv import load_dotenv
import os
from pprint import pprint


def get_current_weather():
    print('\n **** Get Current Weather Conditions. **** \n')
    
    city = input('\nPlease enter city name: \n')
    
    request_url = f""
    
    print(request_url) # check if url works
    
    weather_data = requests.get(request_url).json()
    
    # pprint(weather_data)
    print(f'\nCurrent weather for {weather_data["name"]}')
    print(f'\nThe temp is {weather_data["main"]["temp"]}')
    print(f'\nFees like {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]["description"].capitalize()}')
    
if __name__ == "__main__":
    get_current_weather()