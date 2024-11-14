# module_9_1.py

def apply_all_func(int_list, *functions):
    results = {}  # Создаем пустой словарь для хранения результатов
    
    for func in functions:
        # Записываем результат работы функции под ключом ее названия
        results[func.__name__] = func(int_list)
    
    return results  # Возвращаем словарь с результатами


