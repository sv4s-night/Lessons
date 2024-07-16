import pandas as pd

"""5. Дополнительные операции для выборки"""

# ================================================================================================================
# Метод ISIN - проверяет, содержится ли значение в определенном столбце в заданном списке значений

# italy_france_reviews = reviews.loc[reviews.country.isin(['Italy', 'France'])]
# print(italy_france_reviews)

# Вывод новый Дфрейм в котоом будут лежать вина из италии и франции


# ================================================================================================================
# ================================================================================================================
# метод NOTNULL - выбираются стороки, где значения не равны NaN (нулю)

# not_null_price = wine_reviews.loc[wine_reviews.price.nornull()]
# вывод вина у которых заполнена цена


# ================================================================================================================
# ================================================================================================================
# Объединение условий   & или |
#
# complex_cond = wine_reviews.loc[
#     ((wine_reviews.country == "Italy") | (wine_reviews.points >= 90))
#     &
#     ((wine_reviews.price.notnull()))
#     ]
# комбинация: (Вина из италии или больше 90 очков) и графа с ценой заполнена


# ================================================================================================================
# ================================================================================================================
# Присваивание данных   (исп обращение через квадратные скобки и имя столбца в виде строки)

# # Присвоить значение "everyone" всем значениям в столбце "critic"
# wine_reviews['critic'] = 'everyone'
#
# # создание нового столбца с обратным порядком индексов
# wine_reviews['index_backwards'] = range(len(wine_reviews), 0, -1)


# ================================================================================================================
# ================================================================================================================
"""Задача
Выбрать из Дфрейма только те строки, где значение в столбце country равно Italy"""

df = pd.read_excel("../../data/winemag-data-130k-v2.xlsx")

italy_wine = df.loc[df.country == "Italy"]      # задаем новый Дфрейм переменной
print(italy_wine.head())    # проверяем что выбрана италия

