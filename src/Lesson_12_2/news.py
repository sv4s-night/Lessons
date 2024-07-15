import datetime
import requests
from src.config import API_KEY, BASE_URL


def get_news(query: str, exclude_words: list, api_key: str = API_KEY) -> list:
    # query - запрос пользователя    exclude_words - слова исключения

    # https://newsapi.org/v2/everything?q=tesla&from=2024-06-14&sortBy=publishedAt&apiKey=a022965c02b44fb9a8f4dd5adfbbc000
    # первоначальная строчка с сайта которую мы разбиваем на параметры

    to_day = datetime.datetime.today()  # переменная сегодняшнего дня
    params = {"q": query,
              "from": to_day.strftime("%Y-%m-%d"),  # передаем сегодняшний день
              "sortBy": "publishedAt",
              "apiKey": api_key
              }

    response = requests.get(
        url=BASE_URL,
        params=params)

    news_data = response.json()
    if news_data.get("status") != "ok":
        return []

    # мы должны сформировать список статей
    arcticals_list = news_data.get("articles", [])  # если нет ключа "articles" то, возвращаем пустой список

    articals_result = []    # формируется список статей с важной информацией
    

    return news_data.get("articles")

    # Итог: функция возвращает список статей которые у нас задается по исходному вопросу
