""" Задача Режимы доступа"""

"""
1. Для класса User сделайте список задач приватным атрибутом,
чтобы к нему нельзя было получить доступ вне класса

2. Добавьте геттер для приватного атрибута списка задач.
Геттер должен возвращать данные о каждой задаче в списке в формате:
- Назначение задачи, Статус выполнения: Ожидает старта, Дата создания 01.04.2024

3. Для добавления задач пользователю реализуйте отдельный метод (сеттер) в классе User,
При этом не забудьте увеличить счетчик задач всех пользователей

4. Для класса Task реализуйте класс-метод, который будет принимать на вход параметры
задач и возвращать созданный объект класса Task

5. Для класса Task сделайте атрибут даты создания приватным и опишите геттеры и
сеттеры. В сеттеры реализуйте проверку: в случае если дата создания раньше, чем 
сегодняшняя, выводите сообщение в консоль "Нельзя изменить дату создания на дату из 
прошлого", при этом новую дату устанавливать не нужно.

6. Напишите тесты на новый функционал
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



    @classmethod
    def new_task(cls, name, description, status="Ожидает старта", created_at=None):
        return cls(name, description, status, created_at)





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

        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email   #f"{first_name}.{last_name}@email.com"
        self.__task_list = task_list if task_list else []       # task_list - делаем приватным

        # для вычисления 2х параметров мы обращаемся к классу User и к самой переменной которую надо вычислить (user_count, all_tasks_count)
        User.users_count += 1   # будет увеличиваться на 1 при каждой инициализации экземпляра класса User
        User.all_tasks_count += len(task_list) if task_list else 0      # увеличить переменную на число заявок в списке task_list, если он не пустой



    # создаем геттер для __task_list
    @property
    def task_list(self):
        task_str = ""
        for task in self.__task_list:
            task_str += f"{task.name}, Статус выполнения: {task.status}, Дата создания {task.created_at}\n"
        return task_str


    # создаем сеттер для __task_list
    @task_list.setter
    def task_list(self, task: Task):
        self.__task_list.append(task)
        User.all_tasks_count += 1



if __name__ == "__main__":
    task = Task("купить огурцы", "купить огурцы для салата")
    task2 = Task("купить помидоры", "Купить помидоры для салата")  # создаем дополнительные задачи для task_list
    task3 = Task("купить лук", "Купить лук для салата")
    task4 = Task("купить горошек", "Купить горошек для салата")
    task5 = Task("купить перец", "Купить перец для салата")
    #
    # # создаем User
    user = User("Ivan", "Ivan.Ivanov@email.com", "Ivan", "Ivanov", [task, task2, task3, task4, task5])
    #
    # print(user.username)            # Ivan
    # print(user.email)               # Ivan.Ivanov@email.com
    # print(user.first_name)          # Ivan
    # print(user.last_name)           # Ivanov
    # print(user.task_list)
    #
    # print(user.users_count)         # 1
    # print(user.all_tasks_count)     # 5

    task6 = Task("купить помидоры", "Купить помидоры для салата")  # создаем дополнительные задачи для task_list
    user.task_list = task6

    print(user.task_list)
    print(User.all_tasks_count)


    task2 = Task.new_task("Купить билеты", "Купить билеты на самолет")
    print(task2.name)
    print(task2.description)
    print(task2.status)
    print(task2.created_at)
