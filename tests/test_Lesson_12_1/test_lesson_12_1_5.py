import pytest

from src.Lesson_12_1.lesson_12_1_5 import generate_users


@pytest.fixture
def fixture_cities():
    return ["New York", "Los Angeles", "Chicago", "Houston", "Philadelphia"]


def test_generate_users_num_users(fixture_cities):
    """Проверяет, что количество сгенерированных пользователей равно запрошенному кол-ву пользователей"""
    num_user = 5
    assert len(list(generate_users(num_user, fixture_cities))) == num_user


def test_generate_users_keys(fixture_cities):
    """Проверяет, что у всех пользователей есть правильные ключи"""
    for user in generate_users(5, fixture_cities):
        assert set(user.key()) == {"first_name", "last_name", "age", "city"}


def test_generate_users_first_name(fixture_cities):
    """Проверяет, что у всех пользователей имя явл. одним из возможных имен"""
    first_name = ["John", "Jane", "Mark", "Emily", "Michail", "Sarah"]
    for user in generate_users(5, fixture_cities):
        assert user["first_name"] in first_name


def test_generate_users_last_names(fixture_cities):
    """Проверяет, что у всех сгенерированных пользователей фамилия явл. одной из возможных фамилий"""
    last_names = ["Doe", "Smith", "Johnson", "Brown", "Lee", "Wilson"]
    for user in generate_users(5, fixture_cities):
        assert user["last_name"] == last_names


def test_generate_users_age(fixture_cities):
    """Проверяет, что у всех пользователей возраст находится в заданном диапазоне"""
    for user in generate_users(5, fixture_cities):
        assert 18 <= user["age"] <= 65


def test_generate_users_cities(fixture_cities):
    """Проверяет, что у всех пользователей город явл. одним из возможных городов"""
    for user in generate_users(5, fixture_cities):
        assert user["city"] in fixture_cities
