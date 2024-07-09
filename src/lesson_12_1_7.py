import os

import requests
from dotenv import load_dotenv

# Загрузка переменных из .env-файла
load_dotenv(".env") \
    # Получение значения переменной из .env-файла
API_KEY = os.getenv("API_KEY")


def get_coords(city: str) -> tuple:
    """Получение координат по названию города"""
    # получаем ответ в виде JSON объекта
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}")

    # задаем ширину и долготу по полученному списку
    lat = response.json()[0]['lat']
    lon = response.json()[0]['lon']
    return lat, lon


def get_weather(lat: float, lon: float) -> float:
    """получение погоды по координатам"""
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}")
    return response.json()["main"]["temp"]


if __name__ == "__main__":
    lat, lon = get_coords("Moscow")
    print(get_weather(lat, lon))
