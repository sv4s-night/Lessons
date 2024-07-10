"""Задача 1
Напишите программу, которая получает информацию о репозиториях пользователей GitHub.

Программа должна иметь следующую функциональность:

Принимает на вход список пользователей GitHub.
Для каждого пользователя получает его информацию и список его репозиториев.
Составляет список результатов в формате JSON, в котором для каждого пользователя указаны его логин, количество публичных
репозиториев и список его репозиториев.
Для получения информации о пользователе и его репозиториях должны использоваться открытые API GitHub.

Пример использования программы:

users = ['user1', 'user2', 'user3']
result = get_github_users(users)
print(result)
"""

import json
import requests


def get_github_users(users):
    """ """
    results = []
    for user in users:
        status, user_data = get_user_info(user)
        if not status:
            continue

        status, repositories = get_user_repos(user)
        if not status:
            continue

        result = {
            "login": user_data["login"],
            "public_repos": user_data["public_repos"],
            "repositories": repositories,
        }
        results.append(result)
    return json.dumps(results)


def get_user_info(user: str) -> tuple[bool, dict]:
    """ """
    url = f"https://api.github.com/users/{user}"
    response = requests.get(url)
    if response.status_code != 200:
        return False, {}
    return True, response.json()


def get_user_repos(user: str) -> tuple[bool, list]:
    repo_url = f"https://api.github.com/users/{user}/repos"
    repo_response = requests.get(repo_url)
    if repo_response.status_code != 200:
        return False, []
    return True, [repo["name"] for repo in repo_response.json()]


"""Задача 2
Напишите функцию, которая будет получать курс валюты на заданную дату из API ЦБ РФ и возвращать его в формате JSON.

Используйте сайт https://www.cbr-xml-daily.ru/daily_json.js.

Пример вызова функции:

rate = get_currency_rate("USD")
print(rate)
Результат:

{
    "currency_code": "USD",
    "rate": 72.7384
}
"""


def get_currency_rate(date, currency_code):
    url = f"https://www.cbr-xml-daily.ru/archive/{date}/daily_json.js"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Failed to get currency rate for date {date}")
    data = response.json()
    currency_code = data["Valute"].get(currency_code)
    if not currency_code:
        raise ValueError(f"No data for currency {currency_code}")
    return {
        "date": date,
        "currency_code": currency_code,
        "rate": currency_code["Value"],
    }


if __name__ == "__main__":
    users = ["user1", "user2", "user3"]
    result = get_github_users(users)
    print(result)

    print(get_currency_rate("2021-10-29", "AUD"))
