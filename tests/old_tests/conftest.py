import pytest
from src.Lesson_14_1.L9 import User, Task


#
#
# @pytest.fixture
# def cities():
#     return ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']


@pytest.fixture
def task():
    return Task("купить салат", "Купить салат для салата", created_at="20.04.2024")

        # создаем фикстуру для задачи

# ===============================================================================================================




# создаем пользователей для подсчета задач
@pytest.fixture
def first_user():
    return User(
        username="Ivan",
        email="user@email.com",
        first_name="Ivan",
        last_name="Ivanov",
        task_list=[
            Task("купить лук", "Купить лук для салата"),
            Task("купить помидоры", "Купить помидоры для салата")
        ]
    )


# создаем второго пользователя что бы проверить атрибуты классов user_count и all_task_count
@pytest.fixture
def second_user():
    return User(
        username="Petr",
        email="petr@email.com",
        first_name="Petr",
        last_name="Petrov",
        task_list=[
            Task("купить лук", "Купить лук для салата"),
            Task("купить помидоры", "Купить помидоры для салата"),
            Task("купить салат", "Купить салат для салата")
        ]
    )



