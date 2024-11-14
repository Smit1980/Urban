# module_9_1.py

def apply_all_func(int_list, *functions):
    results = {}  # Создаем пустой словарь для хранения результатов
    
    for func in functions:
        # Записываем результат работы функции под ключом ее названия
        results[func.__name__] = func(int_list)
    
    return results  # Возвращаем словарь с результатами

# Пример использования функции
print(apply_all_func([6, 20, 15, 9], max, min))  # Ожидаемый вывод: {'max': 20, 'min': 6}
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))  # Ожидаемый вывод: {'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}
