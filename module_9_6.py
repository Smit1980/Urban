def all_variants(text):
    """
    Генератор, который возвращает все возможные подпоследовательности строки text.
    """
    length = len(text)
    for start in range(length):
        for end in range(start + 1, length + 1):
            yield text[start:end]  # Возвращаем подпоследовательность строки


# Пример использования функции-генератора
a = all_variants("abc")
for i in a:
    print(i)
