# Данные списки
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# 1. Список длин строк из first_strings, если длина >= 5
first_result = [len(string) for string in first_strings if len(string) >= 5]

# 2. Список кортежей из пар слов одинаковой длины из first_strings и second_strings
second_result = [
    (word1, word2) 
    for word1 in first_strings 
    for word2 in second_strings 
    if len(word1) == len(word2)
]

# 3. Словарь из объединённых списков, где ключ - строка, значение - длина строки (только для строк с чётной длиной)
third_result = {
    string: len(string) 
    for string in first_strings + second_strings 
    if len(string) % 2 == 0
}

# Вывод результатов
print(first_result)
print(second_result)
print(third_result)
