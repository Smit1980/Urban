def add_everything_up(a, b):
    try:
        # Попытка сложить a и b как числа или строки
        result = a + b
        return result
    except TypeError:
        # Обработка ситуации, когда типы a и b разные (например, int и str)
        return str(a) + str(b)

# Пример использования
print(add_everything_up(123.456, 'строка'))  # Ожидаемый вывод: '123.456строка'
print(add_everything_up('яблоко', 4215))     # Ожидаемый вывод: 'яблоко4215'
print(add_everything_up(123.456, 7))         # Ожидаемый вывод: 130.456
