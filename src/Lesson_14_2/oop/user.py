class User:
    username: str
    email: str
    first_name: str
    last_name: str
    task_list: list

    # атрибуты класса (так как задаются в самом классе)
    users_count = 0  # 2 этих параметра это значения, которые надо будет вычисоять
    all_tasks_count = 0

    def __init__(self, username, email, first_name, last_name,
                 task_list=None):  # task list может быть пустым, по этому ставим None

        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email  # f"{first_name}.{last_name}@email.com"
        self.__task_list = task_list if task_list else []  # task_list - делаем приватным

        """ для вычисления 2х параметров мы обращаемся к классу User и к самой переменной 
        которую надо вычислить (user_count, all_tasks_count)"""
        User.users_count += 1  # будет увеличиваться на 1 при каждой инициализации экземпляра класса User
        User.all_tasks_count += len(task_list) if task_list else 0
        """ увеличить переменную на число заявок в списке task_list, если он не пустой"""


    @property                           # создаем геттер для __task_list
    def task_list(self):
        task_str = ""
        for task in self.__task_list:
            task_str += f"{task.name}, Статус выполнения: {task.status}, Дата создания {task.created_at}\n"
        return task_str


    @task_list.setter                   # создаем сеттер для __task_list
    def task_list(self, task):
        self.__task_list.append(task)   # добавляет новую задачу
        User.all_tasks_count += 1       # увеличивает кол-во задач на 1
