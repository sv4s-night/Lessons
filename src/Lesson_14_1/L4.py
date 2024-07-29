""" 4. Инициализация"""


class Employee:
    """Класс для представления сотрудников"""
    name: str
    surname: str
    email: str
    pay: int

    # Переменная на уровне класса для подсчета количества сотрудников
    number_of_employees = 0

    def __init__(self, name, surname, pay):  # сам инициализатор или конструктор\ передаем аргументы в конструктор self
        """Метод для инициализации экземпляра класса. Задаем значения атрибутов экземпляра"""
        self.name = name
        self.surname = surname
        self.pay = pay
        self.email = f"{self.name}.{self.surname}@imail.com"

        # прописываем в объекте, что бы на уровне класса происходил подсчет созданных объектов
        Employee.number_of_employees += 1


    def fullname(self):
        """Метод, который возвращает полное имя сотрудника"""
        return f"{self.name} {self.surname}"






emp_1 = Employee("Ivan", "Ivanov", 50000)

print(emp_1.name)
print(emp_1.surname)
print(emp_1.pay)
print(emp_1.email)

print(emp_1.fullname())


print(Employee.number_of_employees)