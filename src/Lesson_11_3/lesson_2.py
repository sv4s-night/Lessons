from time import time


def timer(func):
    """Декоратор вычисляющий время работы функции"""

    def wrapper(*args, **kwargs):
        print(f" Start TIMER decorator")
        time_1 = time()
        result = func(*args, **kwargs)
        time_2 = time()
        print(f"Time for work: {time_2 - time_1}")
        return result

    return wrapper


# Декоратор болванка
# def timer(func):
#   def wrapper(*args, **kwargs):
#       result = func(*args, **kwargs)
#       return result
#   return wrapper


def printing(func):
    """Декоратор вывода сообщения"""

    def wrapper(*args, **kwargs):
        print(f"Start  {func}")
        result = func(*args, **kwargs)
        print(f"Stopped {func}")
        return result

    return wrapper
