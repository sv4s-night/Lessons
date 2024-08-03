""" Сначала тестируем задачу Task()"""


def test_task_init(task):
    assert task.name == "купить салат"
    assert task.description == "Купить салат для салата"
    assert task.created_at == "20.04.2024"
    assert task.status == "Ожидает старта"

# ======================================================================================================
"""
Нужно протестировать инициализацию и корректность работы атрибутов класса
"""

def test_user_init(first_user, second_user):
    assert first_user.username == "Ivan"
    assert first_user.email == "user@email.com"
    assert len(first_user.task_list) == 2

    assert first_user.users_count == 2
    assert second_user.users_count == 2

    assert first_user.all_tasks_count == 5
    assert second_user.all_tasks_count == 5
