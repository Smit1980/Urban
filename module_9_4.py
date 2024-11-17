from random import choice

# Задача 1: Lambda-функция
first = 'Мама мыла раму'
second = 'Рамена мало было'

# Используем lambda-функцию в list(map()) для проверки совпадения символов на одинаковых позициях
result = list(map(lambda x, y: x == y, first, second))
print(result)
# Вывод: [False, True, True, False, False, False, False, False, True, False, False, False, False, False]

# Задача 2: Замыкание
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for data in data_set:
                file.write(str(data) + '\n')
    return write_everything

# Пример использования замыкания
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Задача 3: Метод __call__
class MysticBall:
    def __init__(self, *words):
        self.words = list(words)  # Сохраняем слова в атрибуте words

    def __call__(self):
        return choice(self.words)  # Возвращаем случайное слово из коллекции

# Пример использования класса MysticBall
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
