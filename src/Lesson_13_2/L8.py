""" 8. Библиотека collections: deque и namedtuple
"""

# Создаем deque
from collections import deque, namedtuple

my_deque = deque([1, 2, 3])

# добавляем элемент     deque([1, 2, 3, 4])
my_deque.append(4)

# добавляем элемент     deque([0, 1, 2, 3, 4])
my_deque.appendleft(0)

# удаляем элементы из конца и начала
my_deque.pop()  # deque([0, 1, 2, 3])
my_deque.popleft()  # deque([1, 2, 3])

# добавляем несколько элементов в конец списка  deque([1, 2, 3, 4, 5, 6, 7])
my_deque.extend([4, 5, 6, 7])

# добавляем несколько элементов в начало списка deque([-2, -1, 1, 2, 3, 4, 5, 6, 7])
my_deque.extendleft([-1, -2])
my_deque.extendleft([-4, -3])  # deque([-3, -4, -2, -1, 1, 2, 3, 4, 5, 6, 7])

# поворачиваем элементы на 2 позиции вправо     deque([6, 7, -3, -4, -2, -1, 1, 2, 3, 4, 5])
my_deque.rotate(2)
print(my_deque)

"""======================================= Задача ================================================
Напишите программу которая моделирует работу очереди в магазине.
Программа должна добавлять новых клиентов в очередь, обслуживать клиентов по принципу 
"первый пришел - первый ушел (FIFO)"
А так же поддерживать возможность добавления VIP-клиентов, которые обслуживаются без очереди.
================================================================================================="""


def add_customer(my_queue, customer):
    """передаем нашу очередь и клиентов"""
    my_queue.append(customer)  # добавляем в очередь клиента
    print(f"Текущее положение очереди: {my_queue}")


def surv_customer(my_queue):
    """"""
    if my_queue:  # надо проверить что очередь не пустая
        print(f"Обслуживаем клиента: {my_queue.popleft()}")  # выводим имя клиента и удаляем его из списка
    else:
        print("Очередь пуста")
    print(f"Текущее положение очереди: {my_queue}")


def add_vip_customer(my_queue, customer):
    """добавляем вип в начало очереди"""
    my_queue.appendleft(customer)
    print(f"Текущее положение очереди: {my_queue}")


queue = deque()  # queue - очередь
add_customer(queue, "Alice")  # функции в который мы передаем нашу очередь и клиента
add_customer(queue, "Max")
surv_customer(queue)
add_vip_customer(queue, "Charly")
surv_customer(queue)

# ============================================================================================================

# Создаем класс Point   импортируя из collections
Point = namedtuple("Point", ["x", "y"])  # передаем класс и задаем его атрибуты

# Создание объекта Point
p = Point(1, 2)
print(p.x, p.y)  # Выводим атрибуты нашего класса 1 2

# заменяем значение в поле (создастся новый объект)
p2 = p._replace(x=10)
print(p2)  # Point(x=10, y=2)

# Преобразование в словарь      {'x': 1, 'y': 2}
print(p._asdict())

# Получение списка полей нашего объекта     ('x', 'y')
print(p._fields)

# Создание из итерируемого объекта       Point(x=3, y=4)
p3 = Point._make([3, 4])
print(p3)


"""======================================= Задача ================================================
Напишите программу, которая будет хранить информацию о студентах и их оценках
по различным предметам, используя namedtuple

Программа должна позволять добавлять студентов, добавлять оценки по предметам и
выводить средний бал каждого студента 
================================================================================================="""


def add_student(students_dict, name, subject, grade):
    """Передаем наш словарь students, имя студента, предмет и оценку"""
    if name in students_dict:   # если студент уже есть, но добавляется новый предмет с оценками
        students_dict[name].grades[subject] = grade
        # берем уже заготовленный словарь, по ключу получаем Алис и записываем новую оценку

    else:   # случай если в списке нет студентов
        students_dict[name] = Student(name, {subject: grade})



def add_grade(students_dict, name, subject, grade):
    """в student_dict по ключу name для предмета добавить оценку"""
    if name in students_dict:
        students_dict[name].grades[subject] = grade
    else:
        print(f"Студент с именем {name} не существует")




def print_average_grades(students_dict):
    """"""
    for student in students_dict.values():  # пробегаемся по объекту, а точнее по его параметрам
        avg = sum(student.grades.values()) / len(student.grades.values() )
        print(f"Средняя оценка студента {student.name}: {avg}")


students = dict()

#создаем класс
Student = namedtuple("Student", ["name", "grades"])

add_student(students, "Alice", "математика", 85)
add_student(students, "Alice", "физика", 90)
add_student(students, "Alice", "химия", 88)

add_student(students, "Bob", "математика", 91)
add_student(students, "Bob", "физика", 92)
add_student(students, "Bob", "химия", 78)

add_grade(students, "Alice", "физ-ра", 51)  # оценка добавится
add_grade(students, "John", "физ-ра", 51)   # Студент с именем John не существует
#
# print_average_grades(students)

print(students)

print_average_grades(students)