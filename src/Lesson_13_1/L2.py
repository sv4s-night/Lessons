import csv


# ==============================================================================================================
# Запись данных в CSV-файл      csv.writer

row = [['Name', 'Age', 'Gender'],
         ['Alice', '25', 'Female'],
         ['Bob', '30', 'Male'],
         ['Charlie', '35', 'Male']]

with open("file.csv", "w", encoding="UTF-8", newline="") as file:
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
# Работа с CSV как со словарями

""" 
Функция DictReader — позволяет читать CSV-файл и создавать словари из строк файла. 
Ключами в словаре будут названия столбцов, а значениями — значения в соответствующих ячейках.
"""

with open("file.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row['Name'], row['Age'], row['Gender'])






