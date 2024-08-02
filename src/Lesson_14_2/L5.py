""" 5. Декоратор @property """


# class Employee:
#     raise_amt = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.__email = first + "." + last + "@email.com"  # делаем почту приватной
#
#         # получатель
#
#     def get_email(self):
#         return self.__email
#         """Так как почта у нас приватна, мы создали функцию для получения значения почты"""
#
#         # установитель
#
#     def set_email(self, email):
#         self.__email = email
#         """Так же у нас есть метод для смены почты (для администратора
#         или если необходимо еще по какой либо причине поменять почту)"""


# ====================================================================================================================
""" Задача  
1. реализовать метод Fullname
- Можно обращаться как к обычному атрибуту
- Возвращает имя и фамилию через пробел
- При присваивании строки с именем и фамилией обновляет соответствующие атрибуты

2. Реализовать метод email
- Возвращает email  сотрудника
- Доступ к методу как к обычному атрибуту, без вызова
"""

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last


    @property   # реализация геттера
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property   # реализация геттера
    def fullname(self):
        return f"{self.first} {self.last}"



    """Setter и Deleter - не могут быть реализованы пока нет Геттера ( @property ) """
    @fullname.setter                            # реализация сеттера (реализация через геттер(имя функции) + сеттер)
    def fullname(self, new_fullname):           # необходимо принимать какое-либо значение
        first, last = new_fullname.split(" ")   # задаем что first и last у нас будут равны значению получаемому от
        self.first = first                      # new_fullname разделенным методом split через пробел
        self.last = last


    @fullname.deleter          # реализация делитера (реализация через геттер(имя функции) + deleter)
    def fullname(self):
        self.first = None
        self.last = None






emp = Employee("Ivan", "Ivanov")

# print(emp.email())        # обычный метод
# print(emp.fullname())     # обычный метод

# ============== реализация getter
""" Для того что бы у нас все выводилось не как метод, а как атрибут нам необходимо задать декоратор @property """

print(emp.email)
print(emp.fullname)


# ============== реализация setter
""" Выдаст ошибку так как первоначально у нас не реализован сеттер - замена 
значения (AttributeError: property 'fullname' of 'Employee' object has no setter)"""

emp.fullname = "Petr Petrov"
print(emp.fullname)




# ============== реализация deleter
del emp.fullname        # Применяем deleter
print(emp.fullname)     # Вывод None None

