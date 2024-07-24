""" ================================================ HW lesson 13.2 ===

Вам поручено реализовать часть логики, предполагающую работу с регулярными выражениями. Используйте для этого библиотеку
re
"""

""" 1 Задача
Напишите функцию, которая будет принимать список словарей с данными о банковских операциях и строку поиска, 
а возвращать список словарей, у которых в описании есть данная строка. При реализации этой функции можно 
использовать библиотеку re для работы с регулярными выражениями.
Расположение новой функции в структуре проекта определите самостоятельно.
"""

""" 2 Задача
Напишите функцию, которая будет принимать список словарей с данными о банковских операциях и список категорий операций, 
а возвращать словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.
Категории операций хранятся в поле description.

Расположение новой функции в структуре проекта определите самостоятельно.
"""

""" 3 Задача
Напишите функцию main в модуле main, которая отвечает за основную 
логику проекта и связывает функциональности между собой.
Ожидаемое поведение программы должно быть следующим:

===========
Программа приветствует пользователя:
Программа: Привет! Добро пожаловать в программу работы 
с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла

Пользователь: 1
Программа: Для обработки выбран JSON-файл.
===========

После пользователь выбирает статус интересующих его операций.
Не забудьте, что для пользователя executed, Executed и EXECUTED — это одно и то же, 
а для программы — разное. Используйте приведение к единому регистру.

Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING

Пользователь: EXECUTED
Программа: Операции отфильтрованы по статусу "EXECUTED"

=============
В случае, если пользователь ввел неверный статус, программа не должна падать в ошибку, 
а должна возвращать пользователя к вводу корректного статуса:

Пользователь: test

Программа: Статус операции "test" недоступен.

Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING

"""

"""
После фильтрации программа выводит следующие вопросы для уточнения выборки операций, 
необходимых пользователю, и выводит в консоль операции, соответствующие выборке пользователя:

Программа: Отсортировать операции по дате? Да/Нет

Пользователь: да

Программа: Отсортировать по возрастанию или по убыванию? 

Пользователь: по возрастанию/по убыванию

Программа: Выводить только рублевые транзакции? Да/Нет

Пользователь: да

Программа: Отфильтровать список транзакций по определенному слову 
в описании? Да/Нет

Пользователь: да/нет

Программа: Распечатываю итоговый список транзакций...

Программа: 
Всего банковских операций в выборке: 4

08.12.2019 Открытие вклада 
Счет **4321
Сумма: 40542 руб. 

12.11.2019 Перевод с карты на карту
MasterCard 7771 27** **** 3727 -> Visa Platinum 1293 38** **** 9203
Сумма: 130 USD

18.07.2018 Перевод организации 
Visa Platinum 7492 65** **** 7202 -> Счет **0034
Сумма: 8390 руб.

03.06.2018 Перевод со счета на счет
Счет **2935 -> Счет **4321
Сумма: 8200 EUR

Если выборка оказалась пустой, программа выводит сообщение:

Программа: Не найдено ни одной транзакции, подходящей под ваши
условия фильтрации
"""






# Шаг 1
words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}








# Шаг 2
def choose_difficulty():
    # функция выбора сложности.

    user_input = input("Выберите уровень сложности:\n1. Легкий\n2. Нормальный\n3. Сложный\n").lower()
    words = {"1. легкий": words_easy, "2. нормальный": words_medium, "3. сложный": words_hard}

    for key, values in words.items():
        if user_input in key:
            return words[key]

    if user_input not in words:
        return words["2. нормальный"]


# Шаг 3
def play_game(words):
    # Функция основной логики вопросов пользователю.

    # answers — словарь с записями о верных и неверных ответах.
    answers = {}

    for key, values in words.items():
        word_length = len(words[key])
        first_letter = values[0]

        user_response = input(f"Переведите слово: {key.title()}. Слово состоит из {word_length} букв."
                              f" Начинается на {first_letter.upper()}...\n").lower()

        if user_response == words[key]:
            print(f"Верно. {key.title()} — это {values.title()}.")
            answers[key] = True
        else:
            print(f"Неверно. {key.title()} — это {values.title()}")
            answers[key] = False
    return answers


# Шаг 4
def display_results(answers):
    # функция вывода результатов пользователю.

    correct_answers = []
    incorrect_answers = []

    for key, values in answers.items():
        correct_answers.append(str(key)) if values else incorrect_answers.append(str(key))

    result_correct = ' '.join(correct_answers)
    result_incorrect = ' '.join(incorrect_answers)

    print(f"Правильно отвечены слова: {result_correct}\nНеправильно отвечены слова: {result_incorrect}")


# Шаг 5
def calculate_rank(answers):
    #  функция вывода пользователю ранга на основе его верных ответов.

    counter = 0
    for key in answers:
        if answers[key]:
            counter += 1

    for key, values in levels.items():
        if counter == key:
            return print(f"Ваш ранг: {values}")


function = play_game(choose_difficulty())
display_results(function)
calculate_rank(function)