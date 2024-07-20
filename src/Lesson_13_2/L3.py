""" Задача =========== Компилированный шаблон регулярного выражения

Напишите программу, которая будет извлекать даты из списка строк
и преобразовывать их в единый формат YYYY-MM-DD

Даты могут быть представлены в различных форматах,
например DD/MM/YYYY, MM-DD-YYYY, YYYY.MM.DD
"""


import re


# регулярные выражения для различных форматов дат
patterns = [
    re.compile(r"(\d{2})/(\d{2})/(\d{4})"),     # формат DD/MM/YYYY
    re.compile(r"(\d{2})-(\d{2})-(\d{4})"),     # формат MM-DD-YYYY
    re.compile(r"(\d{4})\.(\d{2})\.(\d{2})")    # формат YYYY.MM.DD
]


def normalize_date(date_str):
    """Функция преобразования разных форматов дат к 1 формату YYYY-MM-DD"""
    for pattern in patterns:
        match = pattern.search(date_str)    # ищем наш созданный патер в строке
        if match:                           # если search вывел хоть 1 match, то применяем замены
            #print(match)                    # можем вывести что у нас попадает в match
            print(match.groups())            # так же можем вывести все по группам
            # DD/MM/YYYY в YYYY-MM-DD
            if pattern.pattern == r"(\d{2})/(\d{2})/(\d{4})":
                return f"{match.group(3)}-{match.group(2)}-{match.group(1)}"
                # указываются группы, и они переворачиваются в нужное нам место

            # MM-DD-YYYY в YYYY-MM-DD
            elif pattern.pattern == r"(\d{2})-(\d{2})-(\d{4})":
                return f"{match.group(3)}-{match.group(1)}-{match.group(2)}"

            # YYYY.MM.DD в YYYY-MM-DD
            elif pattern.pattern == r"(\d{4})\.(\d{2})\.(\d{2})":
                return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
        return None


def extract_and_normalize_dates(strings):
    """ приобразовываем даты и записываем в новый список"""
    normalized_dates = []                           # новый список
    for string in strings:                          # запускаем цикл
        normal_date = normalize_date(string)        # применяем функцию для преобразования даты
        if normal_date:
            normalized_dates.append(normal_date)    # преобразованную дату добавляем в новый список
    return normalized_dates


# Пример списка строк с датами
dates = [
    "Сегодня 23/04/2021",
    "встреча назначена на 12-05-2020",
    "событие произошло 2019.06.17",
    "Дата: 15/08/2022, запомните ее!",
    "Запланировано на 07-31-2023"
]


# Извлекаем и нормализуем даты
normal_dates = extract_and_normalize_dates(dates)
print(normal_dates)

