# Данные списки
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# 1. Генераторная сборка для разницы длин строк, если длины не равны (с использованием zip)
first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))

# 2. Генераторная сборка для сравнения длин строк без zip (используем range и len)
second_result = (len(first[i]) == len(second[i]) for i in range(min(len(first), len(second))))

# Вывод результатов
print(list(first_result))  # Конвертируем генератор в список для вывода
print(list(second_result))
