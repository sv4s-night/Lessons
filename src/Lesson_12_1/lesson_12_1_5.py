import json
import random

""" Задача 1
Напишите функцию 
generate_users(first_names, last_names, cities), которая будет генерировать случайных пользователей. 
Функция должна возвращать генератор, который будет выдавать каждого пользователя по одному в виде словаря.

Каждый пользователь должен иметь следующие данные:
first_name — имя из списка first_names;
last_name — фамилия из списка last_names;
age — возраст от 18 до 65 лет;
city — город из списка cities.
Сгенерируйте группу пользователей и выведите ее списком в консоль в формате JSON.
"""


def generate_users(first_name: list[str], last_name: list[str], cities: list[str]) -> dict:
    """Функция генерирующая пользователя"""

    while True:
        user = {
            "first_name": random.choice(first_name),
            "second_name": random.choice(last_name),
            "age": random.randint(18, 65),
            "city": random.choice(cities)
        }
        yield user



"""Задача 2
Напишите программу, которая будет принимать на вход JSON-файл с данными о финансовых транзакциях, 
фильтровать транзакции, совершенные в определенной валюте, и сохранять отфильтрованные данные в новый JSON-файл.

Также напишите декоратор, который будет выводить в консоль статистику по количеству отфильтрованных транзакций. 
Статистика должна включать в себя количество отфильтрованных транзакций и их суммарную стоимость.

Пример входных данных (transactions.json):
"""


def stat_decorator(func):
    """Декоратор для вывода статистики по отфильтрованным транзакциям"""
    def wrapper(*args, **kwargs):
        filtered_transactions = func(*args, **kwargs)
        total_amount = sum([transaction['amount'] for transaction in filtered_transactions])
        print(f"Отфильтровано {len(filtered_transactions)} транзакций на сумму {total_amount}")
        return filtered_transactions
    return wrapper


@stat_decorator
def filter_transactions_by_currency(input_file, output_file, currency):
    """Фильтрует транзакции по вылюте и сохраняет результат в новый файл"""

    with open(input_file, "r") as file:
        transactions = json.load(file)

    filtered_transactions = [transaction for transaction in transactions if transaction["currency"] == currency]

    with open(output_file, "w") as file:
        json.dump(filtered_transactions, file, indent=4)

    return filtered_transactions


def main():
    input_file = r"../transactions.json"  # если в другой директории, то надо указать путь
    output_file = "../transactions_filtered.json"
    currency = "USD"

    filtered_transactions = filter_transactions_by_currency(input_file, output_file, currency)
    print(filtered_transactions)



if __name__ == "__main__":

    """1 Задача"""
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Philadelphia"]
    first_name = ["John", "Jane", "Mark", "Emily", "Michail", "Sarah"]
    last_name = ["Doe", "Smith", "Johnson", "Brown", "Lee", "Wilson"]

    users = generate_users(first_name, last_name, cities)

    user_group_1 = [next(users) for i in range(4)]
    user_group_2 = [next(users) for i in range(6)]

    print("Users group #1:")
    print(json.dumps(user_group_1, indent=4))
    print("Users group #2:")
    print(json.dumps(user_group_2, indent=4))



    """2 Задача"""
    main()
