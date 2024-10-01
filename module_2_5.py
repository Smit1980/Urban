# Объявляем функцию get_matrix с параметрами n, m и value
def get_matrix(n, m, value):
    # Создаем пустой список для матрицы
    matrix = []

    # Первый цикл - создание строк матрицы
    for _ in range(n):
        # Создаем пустую строку (список)
        row = []

        # Второй цикл - создание элементов в строке
        for _ in range(m):
            row.append(value)  # Добавляем элемент value в текущую строку

        # Добавляем готовую строку в матрицу
        matrix.append(row)

    # Возвращаем готовую матрицу
    return matrix


# Вызов функции для создания матрицы 3x4, заполненной числом 7
result_matrix = get_matrix(3, 4, 7)

# Вывод матрицы на экран
for row in result_matrix:
    print(row)
