import csv
"""2. Библиотека csv"""

# ==============================================================================================================
# Запись данных в CSV-файл      csv.writer

row = [['Name', 'Age', 'Gender'],                   # тут данные в виде списка LIST []
         ['Alice', '25', 'Female'],
         ['Bob', '30', 'Male'],
         ['Charlie', '35', 'Male']]

with open("file.csv", "w", encoding="UTF-8", newline="") as file:          # открываем файл на запись W
    writer = csv.writer(file)
    # writer = csv.writer(file, delimiter=":")      # если в файле в качестве разделителя исп не ,  а ; или :
    writer.writerow(row)


# ==============================================================================================================
# Чтение из CSV-файла       csv.reader(file)

with open('file.csv') as file:
    reader = csv.reader(file)
    # reader = csv.reader(file, delimiter=";")      # если в файле в качестве разделителя исп не ,  а ; или :

    for row in reader:
        print(f"Чтение из CSV-файла:\n{row}")  # код последовательно выводит каждую строку file.csv


# ==============================================================================================================
# Работа с CSV как со словарями    чтение     csv.DictReader(file)

""" 
Функция DictReader — позволяет читать CSV-файл и создавать словари из строк файла. 
Ключами в словаре будут названия столбцов, а значениями — значения в соответствующих ячейках.
"""

with open("file.csv") as file:                  # тут данные в виде словаря DICT  {ключ: значение}
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Name"], row["Age"], row["Gender"])

# ==============================================================================================================
# Работа с CSV как со словарями     запись          writer = csv.DictWriter(file, fieldnames=fieldnames)

rows = [{'Name': 'Alice', 'Age': '25', 'Gender': 'Female'},
        {'Name': 'Bob', 'Age': '30', 'Gender': 'Male'},
        {'Name': 'Charlie', 'Age': '35', 'Gender': 'Male'}]

with open('file.csv', 'w', newline='') as file:
    fieldnames = ['Name', 'Age', 'Gender']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)

# ==============================================================================================================
"""
Необходимо прочитать CSV-файл и вывести на экран информацию о студентах, у которых средний балл больше 4.5.
Файл с данными для задачи: students.csv
Решение:
"""

with open("students.csv") as st_file:
    reader = csv.reader(st_file, delimiter=',')
    next(reader)    # пропускаем первую строке с заголовками Name, age, avg_grade
    for row in reader:
        name, age, avg_grade = row      # извлекает значение из текущей строки и присваивает их
        if float(avg_grade) > 4.5:      # переменным name, age, avg_grade
            print(f"{name}, {age} лет - средний бал {avg_grade}")

