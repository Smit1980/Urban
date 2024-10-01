def get_multiplied_digits(number):
    # Преобразуем число в строку для работы с отдельными цифрами
    str_number = str(number)

    # Если в числе всего одна цифра, то возвращаем её как результат
    if len(str_number) == 1:
        return int(str_number)

    # Получаем первую цифру числа
    first = int(str_number[0])

    # Рекурсивно умножаем первую цифру на результат работы функции с оставшимися цифрами
    return first * get_multiplied_digits(int(str_number[1:]))


# Пример использования функции
result = get_multiplied_digits(40203)
print(result)
