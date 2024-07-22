""" Задачи
Дан файл access.log, содержащий большой объем текста и email-адресов. Необходимо с помощью регулярных выражений
«вытащить» оттуда все email-адреса, подсчитать количество вхождений каждого домена почтового сервиса и сохранить
результат в JSON-файле result.json

Для решения задачи необходимо использовать библиотеки re, json и collections
Содержание файла access.log
"""

import re
import json
from collections import Counter


def counter_emails(input_file: str, output_file: str):
    """Открываем файл с текстом и считываем его содержимое"""
    with open(input_file, "r", encoding="UTF-8") as file:
        text = file.read()

    """Находим все email адреса в тексте с помощью регулярного выражения"""
    pattern = r"\b[\w\.-]+@[\w\.-]+\.\w+\b"
    email_address = re.findall(pattern, text)

    """Создаем объект counter, хранящий кол-во email адресов каждого почтового сервиса"""
    email_counter = Counter(email.split("@")[1] for email in email_address)

    """Создаем словарь, хранящий метаинформацию и списки email адресов для каждого домена"""
    result = {"total_counter": len(email_address), "domains": {}}

    for domain, count in email_counter.items():
        # Получаем список email адресов для данного домена
        domain_emails = [email for email in email_address if email.split("@")[1] == domain]
        # Добавляем информацию о домене в словарь
        result["domains"][domain] = {"count": count, "emails": domain_emails}

    # Записываем результат в Json файл
    with open(output_file, "w", encoding="UTF-8") as file:
        json.dump(result, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    counter_emails("../../logs/access.log", "../../data/result.json")

"""
Пояснения к решению:

В функции count_emails мы открываем файл с текстом и считываем его содержимое.

Далее мы с помощью регулярного выражения находим все email-адреса в тексте.

Создаем объект Counter, хранящий количество email-адресов каждого почтового сервиса.

Создаем словарь result, в котором будем хранить метаинформацию и списки email-адресов для каждого домена.

Используя цикл for, перебираем все домены, для каждого домена получаем список email-адресов и добавляем 
информацию о домене в словарь result.

Записываем результат в JSON-файл с помощью функции json.dump(). Обратите внимание на параметр ensure_ascii=False, 
который позволяет записывать данные в файл в кодировке UTF-8, и на параметр indent=4, который делает форматирование 
JSON-файла более читабельным.
"""