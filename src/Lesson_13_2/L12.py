""" Задачи"""
import random
import string
from collections import deque, defaultdict, Counter
import re

"""======================================= Задача 1 =======================================================
Напишите программу, которая находит все даты в формате "dd-mm-yyyy" в заданном тексте.

import re
========================================================================================================="""

text_1 = "Сегодня 23-09-2021, а завтра будет 24-09-2021. Вчера была дата 22-09-2021."
pattern = r'\b\d{2}[-]\d{2}[-]\d{4}\b'

# \b \b - границы слова (все что в этой границе указывает каким будет искомое слово)
# \d - любая цифра от 0 до 9
# {3} - указывает сколько нужных символов идут подряд
# [-] - любой из символов указанных в скобках [-+=/* и тд]

date_time = re.findall(pattern, text_1)
print(f'Задача 1. {date_time}')

# ['23-09-2021', '24-09-2021', '22-09-2021']


"""======================================= Задача 2 =======================================================
Напишите программу, которая извлекает все хештеги из заданного текста.

import re
========================================================================================================="""
text_2 = "Сегодня я сделал #Python, а вчера #MachineLearning. Завтра буду изучать #DataScience"

pattern = r"#\w+"
hash_tags = re.findall(pattern, text_2)
print(f"Задача 2. {hash_tags}\n")

# Вывод ['#Python', '#MachineLearning', '#DataScience']


"""======================================= Задача 3 =======================================================
Напишите программу, которая проверяет строки на соответствие требованиям пароля: 
длина не менее 8 символов, наличие хотя бы одной большой буквы, одной маленькой буквы и одной цифры.

import re
========================================================================================================="""

passwords = ["Password123", "password", "PASSWORD123", "Passw0rd", "Passw"]

pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"

# ^$ - ^ от начала строки и до $ конца строки
# {8,} - как минимум 8 символов
# [a-zA-Z\d] - указывает все буквы Верхн и нижн регистра, и цифры
# (?=.*[a-z]) - означает, хотя бы 1 символ из указанных границ [a-z]

valid_password = [pwd for pwd in passwords if re.match(pattern, pwd)]
print(f"Задача 3. Подходящие пароли: {valid_password}\n")



"""======================================= Задача 4 =======================================================
Напишите программу, которая подсчитывает, сколько раз каждое слово встречается в тексте. Используйте 
collections.Counter

from collections import Counter
========================================================================================================="""

text_3 = "Это пример текста в котором встречаются слова и слова могут повторяться слова"
words_list = text_3.split()  # разбиваем строку на элементы списка
words_counter = Counter(words_list)  # применяем метод Counter
print(f"Задача 4. Подсчет слов в строке:\n{words_counter}\n")

# Counter({'слова': 3, 'Это': 1, 'пример': 1, 'текста': 1, 'в': 1, 'котором': 1,
# 'встречаются': 1, 'и': 1, 'могут': 1, 'повторяться': 1})



"""======================================= Задача 5 =======================================================
Используйте defaultdict, чтобы создать словарь, где значения по умолчанию будут равны пустым спискам. 
Затем добавьте несколько ключей и значений в этот словарь.

(Импортируем   from collections import defaultdict)
========================================================================================================="""

data = [("группа_1", "элемент_1"), ("группа_1", "элемент_2"), ("группа_2", "элемент_1")]

def_dict = defaultdict(list)

for key, values in data:  # с помощью цикла создаем словарь в котором значения(value) будут списки
    def_dict[key].append(values)

print(f"Задача 5. Созданный словарь \n{def_dict}\n")
# Вывод:
# defaultdict(<class 'list'>, {'группа_1': ['элемент_1', 'элемент_2'], 'группа_2': ['элемент_1']})






"""======================================= Задача 6 =======================================================
Используйте collections.deque для реализации очереди задач. 
Добавьте несколько задач в начало и конец очереди, затем извлеките их.
(Импортируем   from collections import deque)
========================================================================================================="""
# deque (double-ended queue) — это структура данных, представляющая собой двустороннюю очередь.
task_deque = deque()  # Создаем очередь

task_deque.append("Task1")  # Создаем задачи
task_deque.appendleft("Task2")
task_deque.append("Task3")
task_deque.appendleft("Task4")
task_deque.append("Task5")

while task_deque:
    print(f" Задача 6. {task_deque.popleft()}")
    # Выводим задачи, пока они не закончатся





"""======================================= Задача 7 =======================================================
Напишите программу, которая создает случайный пароль длиной 12 символов, в котором используются буквы верхнего и 
нижнего регистра, цифры и специальные символы.
(Необходим модуль import string для импорта букв)
========================================================================================================="""

# все буквы верхнего и нижнего регистра + все цифры + все спецсимволы
all_symbols = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(all_symbols) for _ in range(12))
print(f"\nЗадача 7. Рандомный пароль: {password}")




"""======================================= Задача 8 =======================================================
Создайте список чисел от 1 до 10 и перемешайте его элементы случайным образом.
========================================================================================================="""

number_list = list(range(1, 11))
random.shuffle(number_list)
print(f"Задача 8. {number_list}")




"""======================================= Задача 9 =======================================================
Дан список студентов. Напишите программу, которая случайным образом выбирает одного студента для ответа на вопрос.
students = ["Алексей", "Иван", "Мария", "Ольга", "Екатерина"]
========================================================================================================="""

students = ["Алексей", "Иван", "Мария", "Ольга", "Екатерина"]
result = random.choice(students)
print(f"Задача 9. На вопрос отвечает: {result}")
