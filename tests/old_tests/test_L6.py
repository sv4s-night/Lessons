import pytest

from src.Lesson_14_1.L6 import Employee

@pytest.fixture()
def employee_ivan():
    return Employee("Ivan", "Ivanov", 50000)    # создаем объект (главное его импортировать)


def test_init(employee_ivan):           # создаем тест init и в него передаем наш объект employee_ivan
    assert employee_ivan.name == "Ivan"      # и проверяем что у нас employee == имени
    assert employee_ivan.surname == "Ivanov"    # проверка фамилии
    assert employee_ivan.pay == 50000       # проверка оплаты
    assert employee_ivan.email == "Ivan.Ivanov@email.com" # проверка email


def test_is_work(employee_ivan):
    """Тест на работу"""
    assert not employee_ivan.is_work       # проверяем первоначальное значение (по умолчанию False)
    employee_ivan.work()                        # Метод который, отправляет сотрудника работать (меняет False на True)
    assert employee_ivan.is_work       # и проверяем что сотрудник на работе


def test_is_work_not_vacation(employee_ivan):
    """Метод если работа выполняется, то vacation == False"""
    employee_ivan.go_to_vacation()
    employee_ivan.work()
    assert not employee_ivan.is_vacation




def test_is_vacation(employee_ivan):
    """Тест на отпуск"""
    assert not employee_ivan.is_vacation   # проверяем первоначальное значение (по умолчанию False)
    employee_ivan.go_to_vacation()              # Метод который, отправляет сотрудника в отпуск
    assert employee_ivan.is_vacation    # и проверяем что сотрудник ушел в отпуск


def test_vacation_is_not_work(employee_ivan):
    """Метод если работа выполняется, то vacation == False"""
    employee_ivan.work()
    employee_ivan.go_to_vacation()
    assert not employee_ivan.is_work
