def test_user_init(first_user, second_user):
    assert first_user.username == "User"
    assert first_user.email == "user@mail.ru"
    assert len(first_user.task_list) == 2

    assert first_user.users_count == 2
    assert second_user.users_count == 2

    assert first_user.all_tasks_count == 5
    assert second_user.all_tasks_count == 5

def test_user_task_list_property(first_user):
    print(first_user)