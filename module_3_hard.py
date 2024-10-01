def calculate_structure_sum(data):
    total_sum = 0

    # Определяем тип элемента и обрабатываем его
    if isinstance(data, (list, tuple, set)):
        # Если это список, кортеж или множество, проходимся по его элементам
        for item in data:
            total_sum += calculate_structure_sum(item)

    elif isinstance(data, dict):
        # Если это словарь, проходимся по его ключам и значениям
        for key, value in data.items():
            total_sum += calculate_structure_sum(key)
            total_sum += calculate_structure_sum(value)

    elif isinstance(data, int):
        # Если это число, добавляем его к общей сумме
        total_sum += data

    elif isinstance(data, str):
        # Если это строка, добавляем её длину к общей сумме
        total_sum += len(data)

    return total_sum

# Входные данные
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

# Вызов функции и вывод результата
result = calculate_structure_sum(data_structure)
print(result)
