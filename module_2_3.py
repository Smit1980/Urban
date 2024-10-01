# Исходные данные
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

# Начальный индекс
index = 0

# Цикл while, который продолжает выполнение, пока индекс меньше длины списка
while index < len(my_list):
    # Получаем текущий элемент списка
    current_number = my_list[index]

    # Если число отрицательное, прерываем цикл
    if current_number < 0:
        break

    # Если число равно нулю, пропускаем этот шаг и продолжаем цикл
    if current_number == 0:
        index += 1
        continue

    # Печатаем положительное число
    print(current_number)

    # Увеличиваем индекс для перехода к следующему элементу
    index += 1
