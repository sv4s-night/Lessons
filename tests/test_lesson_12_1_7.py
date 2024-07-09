import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.lesson_12_1_7 import get_weather

# Загрузка переменных из .env-файла
load_dotenv(".env") \
    # Получение значения переменной из .env-файла
API_KEY = os.getenv("API_KEY")


@patch('requests.get')
def test_get_weathe(mock_get):
    mock_get.return_value.json.return_value = {'main': {"temp": 1}}
    assert get_weather(1, 1) == 1
    mock_get.assert_called_once_with(f'https://api.openweathermap.org/data/2.5/weather?lat=1&lon=1&appid={API_KEY}')
