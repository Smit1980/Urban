#requests
import requests

# URL для запроса данных
url = "https://jsonplaceholder.typicode.com/posts"

# Отправка GET-запроса
response = requests.get(url)

# Проверка статуса ответа
if response.status_code == 200:
    print("Данные успешно получены!")
    # Вывод первых 3 записей
    for post in response.json()[:3]:
        print(f"ID: {post['id']}, Title: {post['title']}")
else:
    print(f"Ошибка: {response.status_code}")



#pandas
import pandas as pd

# Загрузка данных из CSV
data = pd.read_csv("example.csv")  # Убедитесь, что файл существует в директории

# Просмотр первых 5 строк
print("Первые 5 строк:")
print(data.head())

# Основная статистика
print("\nСтатистика по числовым данным:")
print(data.describe())

# Группировка данных
print("\nСредние значения по категориям:")
print(data.groupby("Category")["Value"].mean())


#numpy
import numpy as np

# Создание массива
array = np.array([1, 2, 3, 4, 5])

# Выполнение операций
print("Оригинальный массив:", array)
print("Умножение на 2:", array * 2)
print("Квадрат массива:", np.square(array))
print("Среднее значение:", np.mean(array))
print("Сумма всех элементов:", np.sum(array))


#


#
