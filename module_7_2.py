def custom_write(file_name, strings):
    # Словарь для хранения позиций строк
    strings_positions = {}

    # Открываем файл для записи в кодировке utf-8
    with open(file_name, 'w', encoding='utf-8') as file:
        # Итерируемся по списку строк с отслеживанием индекса (начиная с 1)
        for line_number, string in enumerate(strings, start=1):
            # Сохраняем текущую позицию в байтах перед записью строки
            start_byte = file.tell()
            # Записываем строку в файл с новой строкой в конце
            file.write(string + '\n')
            # Записываем информацию в словарь
            strings_positions[(line_number, start_byte)] = string

    # Возвращаем словарь позиций строк
    return strings_positions

# Пример использования
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
