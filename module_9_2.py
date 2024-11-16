def apply_all_func(int_list, *functions):
    # Создаем пустой словарь для хранения результатов
    results = {}

    # Перебираем все переданные функции
    for func in functions:
        # Сохраняем результат выполнения функции в словарь
        results[func.__name__] = func(int_list)

    # Возвращаем словарь с результатами
    return results

# Пример использования функции
if __name__ == "__main__":
    # Передаем список чисел и функции
    print(apply_all_func([6, 20, 15, 9], max, min))
    # Ожидаемый результат: {'max': 20, 'min': 6}

    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
    # Ожидаемый результат: {'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}
