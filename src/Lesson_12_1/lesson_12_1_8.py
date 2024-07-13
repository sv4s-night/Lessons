import requests

"""ConnectionError - Ошибка возникает при отсутствии интернета"""
try:
    response = requests.get("http://example.com")
except requests.exceptions.ConnectionError:
    print("Connection Error. Please check your network connection.")



"""HTTPError - ответ от сервера не явл. корректным HTTP-ответом"""
try:
    response = requests.get("http://example.com")
    response.raise_for_status()
except requests.exceptions.HTTPError:               #отлавливаем из пакета реквест -> exceptions -> ошибку HTTPError
    print("HTTP Error. Please check the URL.")



"""Timeout - ошибка если запрос не получил ответа в течении заданного времени"""
try:
    response = requests.get("http://example.com", timeout=5)
except requests.exceptions.Timeout:
    print("Request time out. Please check your internet connection.")



"""ToManyredirects - возникает если кол-во перенаправлений запроса превышает макс. допустимое значение"""
try:
    response = requests.get("http://example.com", allow_redirects=False)
except requests.exceptions.TooManyRedirects:
    print("Too many redirects. Please check the URL.")



"""RequestException - это базовый класс для всех исключений, которые может  выбросить библиотека requests"""
try:
    response = requests.get("http://example.com")
    response.raise_for_status()
except requests.exceptions.RequestException:
    print("An error occurred. Please try again later.")
