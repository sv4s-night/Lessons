import pytest


def check_that_arg_this(predicate, error_message):
    def wrapper(func):
        def inner(args):
            if not predicate(args):
                raise ValueError(error_message)  # тест проходит на вывод исключения
            return func(args)

        return inner

    return wrapper


def predicate_is_positive(x):
    """С помощью предиката будем тестировать работу Декоратора"""
    return x > 0


@check_that_arg_this(predicate_is_positive, "Число должно быть положительным")
def square(
    x,
):  # созданная функция к которой мы применяем наш декоратор check_that_arg_this
    """Возведение числа в квадрат"""
    return x * x


"""====================================================================================================="""

if __name__ == "__main__":
    with pytest.raises(
        ValueError, match="Число должно быть положительным"
    ):  # через raises проверяем работу предикатов
        square(
            -3
        )  # проверка Декоратора с параметрами (если подставим 3 - выдаст ошибку)

        assert square(2) == 4  # проверка самого теста
        assert (
            predicate_is_positive(3) == True
        )  # проверка предиката (можно без == True)
