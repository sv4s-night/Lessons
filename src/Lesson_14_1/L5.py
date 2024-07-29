""" 5. Концепция ООП"""

"""Наследование"""


class Employee:
    """Класс сотрудника, который обладает общими свойствами и методаными"""
    name: str
    surname: str

    def work(self):
        print("Do some work")

    def go_to_vacantion(self):
        print("Go to vacantion")


class Develop(Employee):
    """Дочерний класс от Employee, который принимает и переопределяет некоторые свойства"""
    language: str
    level: str

    def work(self):
        print("Write code")

    def read_documentation(self):
        print("Read documentation")


# ============================================================================================================
"""Полиморфизм"""


class JavaDeveloper:
    """класс для представления Java-разработчика"""

    def __init__(self, name):
        """Метод, который инициализирует экземпляр класса"""
        self.name = name

    def info(self):
        """Метод для печати информации о Java-разработчике"""
        print(f"I am {self.name} - Java developer")

    def code(self):
        """Метод для программирования на Java"""
        print("class Helloworld {public static void main(string[]) args}")


class PythonDeveloper:
    """класс для представления Python-разработчика"""

    def __init__(self, name):
        """Метод, который инициализирует экземпляр класса"""
        self.name = name

    def info(self):
        """Метод для печати информации о Python-разработчике"""
        print(f"I am {self.name} - Python developer")

    def code(self):
        """Метод для программирования на Python"""
        print("print ('Hello World')")


# Создаем экземпляры разных классов
dev1 = JavaDeveloper("Ivan")
dev2 = PythonDeveloper("Petr")

# Но работаем с ними единым образом
for developer in (dev1, dev2):
    developer.info()  # вызов метода info()
    developer.code()  # вызов метода code()
