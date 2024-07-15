"""
Напишите функцию, которая получает список пользователей из API, сохраняет его в JSON-файл и добавляет в файл логов дату и время запроса.
Ссылка на API: https://jsonplaceholder.typicode.com/users.

Пример содержимого файла
log.txt

INFO:root:Request time: 2022-10-22 14:30:05
INFO:root:Request time: 2022-10-22 14:45:12
"""

import json
import requests
import logging

URL = "https://jsonplaceholder.typicode.com/users"

# ===================================================================
# создаем формат лога
logging.basicConfig(
    filename='application.log',                                 # путь к файлу и его название (куда будет сохраняться лог)
    filemode="a+",                                              # дозапись
    format="%(levelname)s:%(name)s:Request time: %(asctime)s",  # формат лога (как он будет сформирован)
    level=logging.INFO                                          # уровень лога
)
# ===================================================================
# создаем логер
logger = logging.getLogger()  # имя не указываем (по умолч root)


def get_users_and_save() -> None:
    """ Получение пользователей и сохранение в файл """
    response = requests.get(URL)

    logger.info("Hello World!")                                     # сообщение при логировании

    with open('users.json', "w") as users_file:
        json.dump(response.json(), users_file)


if __name__ == "__main__":
    get_users_and_save()
