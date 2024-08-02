""" Задачи Введение в ООП"""

"""
1. Создайте класс Task который будет определять задачу. Для класса Task определите
след свойства:

* Название
* Описание
* Статус
* Дата создания в формате DD.MM.YYYY
    
    Для класса добавьте инициализацию так, чтобы каждый параметр был передан при
    создании объекта и сохранен. При этом если не передан Статус значение автоматически
    выставляется в "Ожидает старта", а если не указана дата - автоматически проставляется "текущая дата"
    
2. Создайте класс User который будет определять каждого пользователя системы. Для класса User определите 
следующие свойства:

* Имя пользователя
* Email
* Имя
* Фамилия
* Список уникальных задач
    
    Для класса добавьте инициализацию так. чтобы каждый параметр был передан при создании объекта и сохранен
    
3. Для класса User добавьте два атрибута класса. Эти атрибуты хранят в себе количество
пользователей в системе и количество задач всех пользователей

4. Напишите тесты для классов, которые проверят:

* Корректность инициализации объектов класса User
* Корректность инициализации объектов класса Task
* подсчет количества пользователей
* подсчет количества задач всех пользователей

5. Реализуйте функцию для загрузки данных о пользователях и задачах из json файла

"""


import datetime

# ========================================================= 1 Задача ==================================================
class Task:
    name: str
    description: str
    status: str
    created_at: str

    def __init__(self, name, description, status="Ожидает старта", created_at=None):
                                                                    # self - ссылка на экземпляр класса
        self.name = name
        self.description = description                            # descriptions - описание
        self.status = status
        self.created_at = created_at if created_at else datetime.date.today().strftime("%d.%m.%Y")
        # created_at - дата создания (применяем библиотеку datetime) .strtime() - переводит из даты в строку
                                                                    # .date.today() - подставляет сегодняшную дату


# ========================================================= 2 Задача ==================================================

class User:
    username: str
    email: str
    first_name: str
    last_name: str
    task_list: list

    # атрибуты класса (так как задаются в самом классе)
    users_count = 0     # 2 этих параметра это значения, которые надо будет вычисоять
    all_tasks_count = 0


    def __init__(self, username, email, first_name, last_name, task_list=None): # task list может быть пустым, по этому ставим None
        # if task_list is None:
        #     task_list = []
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email   #f"{first_name}.{last_name}@email.com"
        self.task_list = task_list if task_list else []

        # для вычисления 2х параметров мы обращаемся к классу User и к самой переменной которую надо вычислить (user_count, all_tasks_count)
        User.users_count += 1   # будет увеличиваться на 1 при каждой инициализации экземпляра класса User
        User.all_tasks_count += len(task_list) if task_list else 0      # увеличить переменную на число заявок в списке task_list, если он не пустой






if __name__ == "__main__":

    # ========================================================= 1 Задача ==================================================
    task = Task("купить огурцы", "купить огурцы для салата")

    print(task.name)                # купить огурцы
    print(task.description)        # купить огурцы для салата
    print(task.status)              # Ожидает старта
    print(task.created_at)          # 30.07.2024



    # ========================================================= 2 Задача ==================================================
    task2 = Task("купить помидоры", "Купить помидоры для салата")   # создаем дополнительные задачи для task_list
    task3 = Task("купить лук", "Купить лук для салата")
    task4 = Task("купить горошек", "Купить горошек для салата")
    task5 = Task("купить перец", "Купить перец для салата")


    # создаем User
    user = User("Ivan", "Ivan.Ivanov@email.com", "Ivan", "Ivanov", [task, task2, task3, task4, task5])

    print(user.username)        # Ivan
    print(user.email)           # Ivan.Ivanov@email.com
    print(user.first_name)      # Ivan
    print(user.last_name)       # Ivanov
    print(user.task_list)       # [<__main__.Task object at 0x000001CF7BCE1850>, <__main__.Task object at 0x000001CF7BCE18E0>, <__main__.Task object at 0x000001CF7BCE1760>, <__main__.Task object at 0x000001CF7BCE19D0>, <__main__.Task object at 0x000001CF7BD198E0>]

    print(user.users_count)     # 1
    print(user.all_tasks_count) # 5
