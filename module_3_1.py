# Переменная для подсчета вызовов функций
calls = 0


# Функция для подсчета количества вызовов
def count_calls():
    global calls
    calls += 1


# Функция для получения информации о строке
def string_info(string):
    # Увеличиваем счетчик вызовов
    count_calls()

    # Возвращаем кортеж: длина строки, строка в верхнем регистре, строка в нижнем регистре
    return (len(string), string.upper(), string.lower())


# Функция для проверки вхождения строки в список
def is_contains(string, list_to_search):
    # Увеличиваем счетчик вызовов
    count_calls()

    # Приводим строку и все элементы списка к нижнему регистру для проверки без учета регистра
    string_lower = string.lower()
    list_lower = [item.lower() for item in list_to_search]

    return string_lower in list_lower


# Примеры вызовов функций
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches

# Выводим количество вызовов функций
print("Количество вызовов функций:", calls)
