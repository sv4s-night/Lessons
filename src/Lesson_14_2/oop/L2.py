"""
Декоратор
"""


def printing(func):                      # Декоратор - всегда на вход принимает функция (Пример 1)
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return inner                         # inner - ссылка на функцию, inner() - функция


@printing       # вызываем декоратор
def add_one(x):
    return x + 1


# Пример 1
y = add_one(10)
print(y)



# Пример 2
# new_f = printing(add_one)   # В декоратор записали саму функцию add_one без аргументов
# y = new_f(10)
# print(y)


# params = {"x": 10}        - 3 записи полностью идентичны
# y = add_one(**params)
# y = add_one(x=10)


# =======================================================================================================
import random



def my_decorator(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return int(result)
    return inner




@my_decorator
def get_rand_numbers():
    """ Результат выполнения функции всегда будет дробное число. Надо декоратором сделать вывод целым числом"""
    return random.randint(1, 100) / random.randint(1, 100)




print(get_rand_numbers())

