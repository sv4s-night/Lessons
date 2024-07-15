import requests
import logging

"""
Напишите функцию, которая получает список пользователей из API, сохраняет его в JSON-файл и добавляет в файл логов дату и время запроса.
Ссылка на API: https://jsonplaceholder.typicode.com/users.

Пример содержимого файла 
log.txt
:

INFO:root:Request time: 2022-10-22 14:30:05
INFO:root:Request time: 2022-10-22 14:45:12
У вас есть API: https://jsonplaceholder.typicode.com/photos.
Напишите приложение, которое скачивает картинки заданного альбома и сохраняет в директории 
photos
. Все шаги должны логироваться: от старта приложения до вывода текущего состояния и информации о завершении приложения и общем количестве скачанных картинок.

Требования:

Все шаги приложения должны выводиться в консоль, для этого нужно использовать 
logging
.
Приложение должно принимать аргументы: 
album_id
 (обязательный) и 
limit
 (необязательный, по умолчанию 100).
Приложение должно скачивать картинки по одной и выводить каждую в консоль с указанием имени файла и номера текущей картинки.
В конце работы приложения должна выводиться информация о завершении работы и общем количестве скачанных картинок.
Пример вывода логов в консоль:

INFO:root:Starting app...
INFO:root:Downloading album 1 images...
INFO:root:Saving image 1 to photos/1-1.jpg
INFO:root:Saving image 2 to photos/1-2.jpg
INFO:root:Saving image 3 to photos/1-3.jpg
INFO:root:Saving image 4 to photos/1-4.jpg
INFO:root:Saving image 5 to photos/1-5.jpg
INFO:root:Finished downloading images. Total images downloaded: 5
"""

# задаем настройки логера
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s:%(name)s:%(message)s'
)
logger = logging.getLogger()




URL = "https://jsonplaceholder.typicode.com/photos"


def get_photos_from_album(album_id: int, limit: int = 100) -> None:
    """Скачать фото по заданному альбому"""

    logger.info('Starting app...')

    response = requests.get(URL)
    counter = 1

    logger.info(f'INFO:root:Downloading album {album_id} images...')

    for item in response.json():
        if item.get('albumId') == album_id:
            image_URL = item.get('url')
            image_data = requests.get(image_URL)

            logger.info(f"Saving image {counter} to photos/{album_id}-{counter}.png")

            with open(f'photos/{album_id}-{counter}.png', "wb") as image_file:
                image_file.write(image_data.content)

            counter += 1
            if counter > limit:

                logger.info(f"Finished downloading images. Total images downloaded: {counter - 1}")

                break

        print(item)
        break





if __name__ == "__main__":
    get_photos_from_album(1, 5)