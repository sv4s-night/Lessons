"""============================================== Задача 1=========================================================
Напишите декоратор, который проверяет, что все числа, возвращаемые декорируемой функцией,
являются целыми, и округляет их до целых, если это не так. Декоратор должен принимать параметр precision,
 который указывает, до скольких цифр после запятой округлять числа.
"""

import time
from functools import wraps


def check_floats(precision):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):

            result = func(*args, **kwargs)
            # проверка на тип с использованием Type
            if type(result) == float:
                return round(result, precision)
            elif type(result) in (list, tuple):
                rounded = [
                    round(x, precision) if type(x) == float else x for x in result
                ]
                return type(result)(rounded)
            else:
                return result

        return inner

    return wrapper


"""============================================== Задача 2 =========================================================
Напишите декоратор, который повторно вызывает декорируемую функцию заданное количество раз через заданное время,
если произошла ошибка. Параметры, передаваемые в декоратор, обязательно должны быть именованными.
"""


def retry(*, retries=3, delay=3):  # retries - повторные попытки       delay - задержка
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):

            for i in range(retries):
                try:
                    return func(*args, **kwargs)
                except:
                    time.sleep(delay)
            raise Exception("Function call failed after multiple retries.")

        return inner

    return wrapper


@retry(retries=6, delay=3)
def random_func(x):
    return x * x


print(random_func(2))


"""============================================== Задача 3 =========================================================
Напишите декоратор, который берет результат декорируемой функции (текст) и возвращает текст, в котором 
каждое слово сокращено до определенной длины. Если слово было сокращено, в конце слова ставится переданный символ. 
Количество символов в слове и знак в конце сокращенного слова — параметры декоратора, причем символ обязательно 
должен передаваться как именованный аргумент.
"""


def shorten_words(
    max_len, *, end_symbol="."
):  # задается макс длинна слова      и конечный символ
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            return " ".join(
                f"{word[:max_len]}{end_symbol}" if len(word) > max_len else word
                for word in result.split()
            )

        return inner

    return wrapper


text = (
    "Напишите декоратор, который берет результат декорируемой функции (текст) и возвращает текст, в котором "
    "каждое слово сокращено до 8 символов. Если слово было сокращено, в конце слова ставится точка."
)


@shorten_words(3)
def my_function_4(texts):
    """Задача 3"""
    return texts


print(my_function_4(text))

"""============================================== Задача 4 =========================================================
Напишите тесты с использованием библиотеки pytest для проверки корректности работы декоратора из задачи 3.
"""


# Тесты
def test_shortening():
    assert get_text() == "Lore! ipsu! dolo! sit amet, cons! adip! elit!"


def test_no_shortening():
    @shorten_words(10, end_symbol="!")
    def get_long_text():
        return "Lorem ipsum dolor sit amet"

    assert get_long_text() == "Lorem ipsum dolor sit amet"


def test_end_symbol():
    @shorten_words(3, end_symbol="?")
    def get_questioned_text():
        return "Lorem ipsum dolor"

    assert get_questioned_text() == "Lor? ips? dol?"


def test_different_lengths():
    @shorten_words(5, end_symbol=".")
    def get_different_length_text():
        return "Hello beautiful world"

    assert get_different_length_text() == "Hello beaut. world"


if __name__ == "__main__":
    print("hello world!")
