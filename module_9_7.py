def is_prime(func):
    """
    Декоратор, проверяющий, является ли результат функции простым числом.
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # Вызываем оригинальную функцию
        if result < 2:
            print("Составное")
        else:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        return result  # Возвращаем результат функции
    return wrapper

@is_prime
def sum_three(a, b, c):
    """
    Функция, складывающая три числа.
    """
    return a + b + c

# Пример использования
result = sum_three(2, 3, 6)  # Ожидается вывод: Составное
print(result)  # 11

result = sum_three(2, 3, 5)  # Ожидается вывод: Простое
print(result)  # 10
