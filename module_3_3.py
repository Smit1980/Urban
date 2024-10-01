# Часть 1: Функция с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Вызовы функции с разным количеством аргументов
print_params()  # Все значения по умолчанию
print_params(10)  # Только a меняется, остальные по умолчанию
print_params(b=25)  # Меняем только b
print_params(c=[1, 2, 3])  # Меняем только c

# Часть 2: Распаковка параметров
# Создаем список с тремя элементами разных типов
values_list = [42, 'Hello', False]

# Создаем словарь с тремя ключами, соответствующими параметрам функции
values_dict = {'a': 99, 'b': 'World', 'c': None}

# Вызов функции с распаковкой параметров из списка
print_params(*values_list)

# Вызов функции с распаковкой параметров из словаря
print_params(**values_dict)

# Часть 3: Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']

# Вызов функции с распаковкой списка и дополнительным аргументом
print_params(*values_list_2, 42)