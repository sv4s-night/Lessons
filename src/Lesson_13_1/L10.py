import pandas as pd
import json

# dframe = pd.read_csv("../../data/titanic.csv")

"""========================================= Задача 1 ================================================
Напишите функцию, которая принимает на вход DataFrame из датасета titanic.csv. 
Функция должна отфильтровать пассажиров, у которых цена билета больше 50 и возраст меньше 30 лет. 
Затем функция должна отсортировать отфильтрованный DataFrame по имени пассажира в алфавитном порядке и вернуть результат
Ожидаемый результат — отфильтрованный и отсортированный DataFrame
======================================================================================================"""


def get_passengers(age: int, fare: float) -> pd.DataFrame:
    """Фильтрация пассажиров"""
    df = pd.read_csv("../../data/titanic.csv")
    price_and_age_df = df.loc[(df.Age < age) & (df.Fare > fare)]  # сортировка по возрасту и цене билета
    price_and_age_df.sort_values('Name', inplace=True)  # фильтрация по имени
    return price_and_age_df


"""========================================= Задача 2 ================================================
Напишите функцию, которая принимает на вход DataFrame из датасета titanic.csv
Функция должна сгруппировать пассажиров по классу и посчитать среднюю стоимость билета и количество 
пассажиров в каждом классе. Функция должна вернуть результат в виде словаря в формате JSON.
======================================================================================================"""


def pass_agg(df: pd.DataFrame):
    """Агрегация по классу и выборка цены и кол-ва пассажиров"""
    grouped_df = df.groupby("Pclass").agg({
        "Fare": "mean",
        "PassengerId": "count"
    })

    dict_data = grouped_df.to_dict(orient="records")

    result = dict()
    for index, item in enumerate(dict_data):
        result[f"{index + 1}"] = {
            "average_ticket_price": round(item["Fare"], 2),
            "passenger_count": item["PassengerId"]
        }

    return json.dumps(result, indent=4)


"""========================================= Задача 3 ================================================
Напишите функцию, которая принимает на вход DataFrame из датасета titanic.csv
Функция должна отфильтровать пассажиров, которые выжили в катастрофе, и записать данные об этих пассажирах в 
файл в формате JSON. Функция должна вернуть количество выживших пассажиров.
======================================================================================================"""


def get_survived(df: pd.DataFrame) -> int:
    """Запись в файл выживших и вернуть кол-во"""
    survived_df = df[df["Survived"] == 1]  # фильтрация по выжившим
    survived_df.to_json("survived.json", orient="records", indent=4, lines=True)  # создается файл json
    return survived_df.count()


if __name__ == "__main__":
    # Задача 1
    filtered_df = get_passengers(age=30, fare=50)
    print(filtered_df.shape)
    print(filtered_df.head())

    # Задача 2
    dframe = pd.read_csv("../../data/titanic.csv")
    result = pass_agg(dframe)
    print(result)

    # Задача 3
    dframe = pd.read_csv("../../data/titanic.csv")
    get_survived(dframe)
