# создаем заглушку


from unittest.mock import patch

import requests


def get_github_user_info(username):  # username Пользователя github
    """Пример Ф которая берет инфо о пользователе github"""
    response = requests.get(f"https://api.github.com/users/{username}")
    return response.json()  # возвращаем Json файл и превращаем в Python объект


@patch(
    "requests.get"
)  # мокаем request.get - означает что в реквест полностью заменяется на объект Моск
def test_get_github_user_info(mock_get):
    # настраиваем объект Моск, что бы он возвращал заранее заданный словарь
    mock_get.return_value.json.return_value = {"login": "testuser", "name": "Test User"}

    # сравниваем Объект Моск с проверочным словарем (заданным параметром)
    assert get_github_user_info("testuser") == {
        "login": "testuser",
        "name": "Test User",
    }

    # проверяем что наш метод был вызван хоть 1 раз с правильным параметром
    mock_get.assert_called_once_with("https://api.github.com/users/username")
