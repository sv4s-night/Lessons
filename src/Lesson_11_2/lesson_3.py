import time

"""============================================== Задача 1 ====================================================
Напишите декоратор, который проверяет, что все числа, возвращаемые декорируемой функцией, являются целыми,
и округляет их до целых, если это не так.
============================================================================================================="""


def check_integers(func):
    """Декоратор проверяющий целые числа"""
    def wrapper(*args, **kwargs):


        result = func(*args, **kwargs)
        """проверка на тип с использованием type()"""

        if type(result) == float:
            return round(result)

        elif type(result) in (list, tuple):
            rounded = [round(x) if type(x) == float else x for x in result]
            """возвращает тот же тип, что и исходный (list или tuple)"""
            return type(result)(rounded)

        else:
            return result

    return wrapper


"""============================================== Задача 2 ==============================================
Напишите декоратор, который повторно вызывает декорируемую функцию три раза, 
каждый раз через три секунды, если произошла ошибка.
=========================================================================================================="""


def retry(func):
    def wrapper(*args, **kwargs):
        for i in range(3):
            try:
                return func(*args, **kwargs)
            except:
                time.sleep(3)
        raise Exception("Function call failed after multiple retries.")

    return wrapper


"""============================================== Задача 3 ==============================================
Напишите декоратор, который позволяет возвращать элементы декорируемой функции по одному через yield,
если эта функция возвращает список или кортеж.
========================================================================================================="""


def yield_items(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # Проверка на тип с использованием type()
        if type(result) in (list, tuple):

            for item in result:
                yield item
        else:
            yield result

    return wrapper


"""============================================== Задача 4 ============================================== 
Напишите декоратор, который берет результат декорируемой функции (текст) и возвращает текст, 
в котором каждое слово сокращено до 8 символов. Если слово было сокращено, в конце слова ставится точка.
============================================== ============================================== ======= """


def shorten_words(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        words = result.split()                          # разбиваем строку на список элементов
        short_words = []                                # создаем список куда будем вносить наш результат

        for word in words:                              # проверяем каждый элемент

            if len(word) > 8:                           # если элемент больше 8 символов
                shortened_word = word[:8] + "."         # в переменную записываем его укороченный вариант с точкой
                short_words.append(shortened_word)      # добавляем слова в новый список

            else:                                       # если слово меньше 8 символов, вносим в список
                short_words.append(word)

        return " ".join(short_words)                  # список с результатами объединяем в строку с разделителем пробел

    return wrapper

# Решение в одну строку через Генератор
# return " ".join(f"{word[:8]}." if len(word) > 8 else word for word in result.split())


"""============================================== Задача 5 ==============================================
Напишите три декоратора, которые можно применять последовательно к результату декорируемой функции.

Первый декоратор должен заменять в тексте, который выдает функция, все восклицательные знаки  ! на !!!.
Второй декоратор должен заменять в тексте, который выдает функция, все знаки вопроса ? на ???.
Третий декоратор должен заменять в тексте, который выдает функция, все точки . на ... .
====================================================================================================="""


def exclamation_marks(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.replace("!", "!!!")
    return wrapper



def question_marks(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.replace('?', '???')
    return wrapper



def dots(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.replace('.', '...')
    return wrapper