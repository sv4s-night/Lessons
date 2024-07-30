""" 6. Тестирование Классов"""

""" проверяем создание нашего объекта через pytest"""


class Employee:
    name: str
    surname: str
    email: str
    pay: int

    def __init__(self, name, surname, pay):
        self.name = name
        self.surname = surname
        self.pay = pay
        self.email = f"{name}.{surname}@email.com"

        self.is_work = False   # по умолчанию пользователь у нас не работает                    1 действие
        self.is_vacation = False    # для отпуска (по умолчанию сотрудник у нас на работе)      1 действие


# ==========================================================================================================================================
    def work(self):                     # 2 действие
        """Метод работа"""
        self.is_work = True         # обращаемся к текущем объекту через self меняем его значение
        self.is_vacation = False
        print("Go to work")

    # ==========================================================================================================================================
    def go_to_vacation(self):           # применяя данный метод мы меняем False(по умолчанию ) на True          # 2 действие
        """Метод отправки в отпуск"""
        self.is_vacation = True
        self.is_work = False
        print("Go to vacation")

    # ==========================================================================================================================================

    # Необходимо написать логику(если сотрудник на работе, то он не в отпуске и наоборот)

    # def is_work_not_vacation(self):
    #     """Метод если работа выполняется, то vacation == False"""
    #     self.is_work = True
    #     print("Go to work")




if __name__ == "__main__":

    emp1 = Employee("Ivan", "Ivanov", 50000)
    # emp2 = Employee("Egor", "Egorov", 60000)

    # print(emp1)
    # print(emp1.name)
    # print(emp1.surname)
    # print(emp1.email)
    # print(emp1.pay)


