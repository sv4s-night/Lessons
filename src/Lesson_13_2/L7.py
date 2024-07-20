"""
7. Библиотека collections: Counter и defaultdict
"""

""" ================================================== Задача 1 ================================================
Напишите программу, которая принимает на вход
список слов и выводит топ-3 самых часто встречающихся слов в этом списке

Если слова встречаются одинаково часто, их порядок в выводе не важен
====================================================================================================="""

from collections import Counter, defaultdict

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana', 'grape', 'apple', 'grape', 'apple']


def get_top_words(list_words: list, top_n: int = 3) -> list:
    """вывод топ 3 встречающихся слова"""
    counter_words = Counter(list_words)
    return counter_words.most_common(top_n)


print(get_top_words(words))

""" ================================================== Задача 2 ================================================
Напишите программу, которая принимает на вход
список пар(имя студента, оценка) и группирует студентов по оценкам

Программа должна выводить список студентов и их оценки
====================================================================================================="""

grades = [("Alice", 85), ("Bob", 90), ("Alice", 95), ("Bob", 85), ("Alice", 88)]


def grades_group(grades_list: list) -> dict:
    """ """
    names_dict = defaultdict(list)
    for name, grade in grades_list:
        names_dict[name].append(grade)
    return names_dict


result = grades_group(grades)
print(result)           # defaultdict(<class 'list'>, {'Alice': [85, 95, 88], 'Bob': [90, 85]})

