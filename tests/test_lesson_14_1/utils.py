"""
Модуль для чтения файла

"""

import json
import os

from src.Lesson_14_1.L9 import Task, User


def read_json(path: str) -> dict:
    """Функция для считывания данных из файла"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)

    return data


def create_objects_from_json(data):
    """Функция, которая создает объекты из предоставленного файла"""
    # для заполнения наших данных создаем отдельную переменную
    users = []
    for user in data:
        tasks = []
        for task in user["task_list"]:
            tasks.append(Task(**task))
        user["task_list"] = tasks
        users.append(User(**user))
    return users

"""
# список, который будет заполняться экземплярами класса USER
# для того чтобы создать экземпляры класса USER, нам надо перебрать data(список получаемый на вход)
# user - это у нас словарь, и нам надо его преобразовать в экземпляр класса USER. Но у нас есть Вложенный словарь с задачами TASK, который нам так же нужно преобразовать в экземпляры класса TASK
# для этого мы создаем новый список task = [], и перебором обращаемся к текущему пользователю user["task_list"] по ключу "task_list"
# получая очередную задачу, мы добавляем непосредственно экземпляр класса Task() |  **task - идет распаковка значений, которые будут подставляться
"""



if __name__ == "__main__":
    raw_data = read_json("../../data/L9_oop_data.json")
    # print(row_data)
    users_data = create_objects_from_json(raw_data)
    print(users_data)
    print(users_data[0].username)   # проверяем имя первого пользователя
    print(users_data[0].task_list)  # и его задачи
