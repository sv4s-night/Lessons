import json
import datetime
import requests

""" Задача 1
Написать функцию, которая будет принимать путь до файла и название города и выполнять следующие действия:
Прочитать JSON-файл с данными о погоде в формате JSON.
Выбрать из этого файла данные для города, который введет пользователь.
Рассчитать среднюю температуру за неделю для выбранного города.
Записать результат расчета в новый JSON-файл.

Пример выходного файла для города
"Moscow"
:
{
  "Moscow": {
    "Average temperature": -0.29
  }
"""


def get_avg_from_city(path: str, city: str) -> bool:
    """ Получение средней температуры за неделю для города"""
    try:  # если пользователь неправильно указал файл
        with open(path) as city_file:

            try:
                city_data = json.load(city_file)
            except json.JSONDecodeError:
                print("Ошибка декодирования файла")
                return False

    except FileNotFoundError:
        print("Файл не найден")
        return False
    """ Все что выше - обработка файла"""

    avg_temp = round(sum(city_data[city].values()) / len(city_data[city].values()), 2)

    out_data = {
        city: {
            "Average temperature": avg_temp
        }
    }
    with open("../out.json", "w") as out_file:
        json.dump(out_data, out_file)

    return True


""" Задача 2
Напишите функцию 
get_days_between_dates(date1, date2), которая принимает на вход две даты в формате "dd.mm.yyyy"
и возвращает количество дней между ними.
Пример использования функции:

>>> get_days_between_dates("01.01.2022", "31.01.2022")
30
"""


def get_days_between_dates(date_1: str, date_2: str) -> int:
    """Получить кол-во дней между датами"""
    date1_obj = datetime.datetime.strptime(date_1, "%d.%m.%Y")
    date2_obj = datetime.datetime.strptime(date_2, "%d.%m.%Y")

    date_diff = (date2_obj - date1_obj).days
    return date_diff


""" Задача 3
Напишите функцию с названием get_github_repos(username: str) -> list[str]
, которая принимает на вход имя пользователя GitHub и возвращает список названий репозиториев этого пользователя.
Для выполнения задания необходимо использовать следующие этапы:

Сделать GET-запрос к API GitHub, используя следующий URL: 
https://api.github.com/users/{username}/repos
Обработать ответ и извлечь из него названия репозиториев.
Вернуть список названий репозиториев.
Если пользователь с указанным именем не найден, функция должна вернуть пустой список.

Пример использования:

repos = get_github_repos('octocat')
print(repos)"""


def get_github_repos(username: str) -> list[str]:
    """Возвращает список названий репозиториев выбранного пользователя"""
    response = requests.get(f"https://api.github.com/users/{username}/repos")

    if response.status_code == 200:
        repos = [repo["full_name"] for repo in response.json()]
    else:
        repos = []

    return repos


if __name__ == "__main__":
    # Задача 1
    get_avg_from_city('data_lesson_12_1_15.json', "Moscow")

    # Задача 2
    print(get_days_between_dates("01.01.2022", "29.01.2022"))

    # Задача 3
    repos = get_github_repos('octocat')
    print(repos)
