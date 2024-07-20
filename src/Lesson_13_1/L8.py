"""
Задачи по списку пассажиров titanic.csv
"""

import pandas as pd
import json

dframe = pd.read_csv("../../data/titanic.csv")
# print(df.head())


"""========================================= Задача 1 ================================================
Напишите функцию, которая принимает на вход DataFrame из датасета titanic.csv
Функция должна вычислить средний возраст мужчин и женщин отдельно и вернуть результат в виде словаря в формате JSON.
"""


def avg_age_by_gender(df):
    """Вычисляет средний возраст мужчин и женщин отдельно, возвращает в формате JSON"""
    avg_age_male = df[df["Sex"] == "male"]['Age'].mean()
    avg_age_female = df[df["Sex"] == 'female']["Age"].mean()
    result_dict = {'Мужчины': avg_age_male, 'Женщины': avg_age_female}
    return json.dumps(result_dict)


"""========================================= Задача 2 ================================================
Напишите функцию, которая должна отфильтровать DataFrame, чтобы в нем остались только мужчины старше 50 лет 
или женщины младше 30 лет. Функция должна вернуть отфильтрованный DataFrame в формате JSON.
"""


def filter_passengers(df):
    result_df = df[((df["Sex"] == "male") & (df["Age"] > 50)) | ((df["Sex"] == "female") & (df["Age"] < 30))]
    return result_df.to_json(orient="records")



"""========================================= Задача 3 ================================================
Напишите функцию, которая вычислит среднюю стоимость билета на пассажира для каждого класса. 
Функция принимает датафрейм и должна вернуть результат в виде словаря в формате JSON
"""


def fare_per_by_class(df):
    total_fare_by_class = df.groupby('Pclass')['Fare'].sum()
    total_passengers_by_class = df.groupby('Pclass')['PassengerId'].count()
    avg_fare_per_passenger_by_class = total_fare_by_class / total_passengers_by_class
    result_dict = avg_fare_per_passenger_by_class.to_dict()
    return json.dumps(result_dict)



if __name__ == "__main__":

    print(avg_age_by_gender(dframe))
    print(filter_passengers(dframe))
    print(fare_per_by_class(dframe))
