import requests
import os

with open("file.txt", "r", encoding="utf-8") as f:   # Чтение строк из файла file.txt
    lines = f.read().splitlines()


API_KEY = os.environ["GRAVITEE_API_KEY"]

session = requests.Session()  # Создание сессии с передачей заголовков
session.headers.update({'accept': 'application/json','Content-Type': 'application/json'})


def process(i):   #  Основная функция выполнения запроса
    r = session.post(
        "https://petstore.swagger.io/v2/pet",
        json = {"id": i},
        timeout = (3, 10)
    )
    r.raise_for_status()

def searchbyid(i):  # Функция поиска только что созданной записи
    r = session.get(
        f"https://petstore.swagger.io/v2/pet/{i}",
        timeout = (3, 10)
    )
    r.raise_for_status()
    return print(r.text)

if __name__ == "__main__":
    print(API_KEY)
    for i in lines:
        process(i)
        searchbyid(i)
