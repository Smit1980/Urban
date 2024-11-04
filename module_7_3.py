import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read().lower()  # Перевод текста в нижний регистр
                for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    content = content.replace(punct, '')  # Удаление пунктуации
                words = content.split()  # Разделение текста на слова
                all_words[file_name] = words  # Добавление списка слов в словарь
        return all_words

    def find(self, word):
        word = word.lower()
        word_positions = {}
        for file_name, words in self.get_all_words().items():
            try:
                position = words.index(word) + 1  # Поиск позиции первого вхождения слова
                word_positions[file_name] = position
            except ValueError:
                # Если слово не найдено в файле, пропустить
                continue
        return word_positions

    def count(self, word):
        word = word.lower()
        word_counts = {}
        for file_name, words in self.get_all_words().items():
            count = words.count(word)  # Подсчет количества вхождений слова
            word_counts[file_name] = count
        return word_counts
