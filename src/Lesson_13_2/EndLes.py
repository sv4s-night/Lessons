import logging

# Конфигурация логгера
logging.basicConfig(filename='example.log', level=logging.DEBUG)

# Настройка форматирования вывода лога
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# Создание обработчика лога для консоли
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
# Добавление обработчика лога к логгеру
logging.getLogger('').addHandler(console_handler)

# Имитация работы программы
for i in range(5):
    try:
        result = 10 / (i - 3)
        logging.info(f"Success: {result}")
    except Exception as e:
        logging.error(f"Exception occurred: {e}", exc_info=True)

# ==================================================================================
"""
У вас есть код на Python, который использует библиотеку logging: 2_before.py.

Ваша задача — сделать так, чтобы сообщения, уровень которых WARNING и выше, не только выводились в консоль, 
но и записывались в лог-файл. Причем в лог-файл надо писать еще и время записи лога.
"""


import json
import logging

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

logger.addHandler(ch)


def get_data_from_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        logger.error(f"Failed to receive data. Status code: {response.status_code}")
        return None


def save_data_to_file(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)
        logger.info("Data saved to file")


def main():
    url = "https://jsonplaceholder.typicode.com/todos/1"

    data = get_data_from_api(url)

    if data is not None:
        logger.debug(f"Data received: {data}")
        save_data_to_file('data.json', data)


if __name__ == "__main__":
    main()