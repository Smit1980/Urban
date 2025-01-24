import sqlite3

# Создаем подключение к базе данных
connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

# Создаем таблицу Users, если она еще не существует
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
""")

# Заполняем таблицу 10 записями
users_data = [
    (f"User{i}", f"example{i}@gmail.com", i * 10, 1000) for i in range(1, 11)
]
cursor.executemany("""
INSERT INTO Users (username, email, age, balance) 
VALUES (?, ?, ?, ?)
""", users_data)

# Обновляем balance у каждой 2-й записи начиная с 1-й на 500
cursor.execute("""
UPDATE Users 
SET balance = 500 
WHERE id % 2 = 1
""")

# Удаляем каждую 3-ю запись начиная с 1-й
cursor.execute("""
DELETE FROM Users 
WHERE id % 3 = 0
""")

# Выбираем записи, где возраст не равен 60
cursor.execute("""
SELECT username, email, age, balance 
FROM Users 
WHERE age != 60
""")
records = cursor.fetchall()

# Выводим записи в нужном формате
for username, email, age, balance in records:
    print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()
