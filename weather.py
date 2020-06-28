import os
import requests
import json
import math


def farenheit(temp):
    temp = math.floor(temp * (9/5)+32)
    return f'The current temperature is {temp}°.'


def notify(message):
    os.system(
        f'osascript -e \'display notification \"{message}\" with title \"Current Weather\"\'')


def getWeather():
    url = 'http://api.weatherstack.com/current?access_key=f99ceb7b64a7cc1b208aa07be456a127&query=Philadelphia'
    response = requests.get(url)
    data = json.loads(response.content)
    tempCelcius = data['current']['temperature']
    farenheit(tempCelcius)
    notify(farenheit(tempCelcius))


if __name__ == "__main__":
    getWeather()
