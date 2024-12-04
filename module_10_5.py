import time
from multiprocessing import Pool

# Функция для считывания информации из файла
def read_info(name):
    all_data = []  # Локальный список для хранения данных
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:  # Прекращаем чтение, если строка пустая
                break
            all_data.append(line.strip())  # Добавляем строку в список
    return all_data  # Возврат данных (опционально)

if __name__ == '__main__':
    # Список файлов
    filenames = [f'./file_{number}.txt' for number in range(1, 5)]  # Пример: file_1.txt, file_2.txt...

    # Линейный вызов
    print("Запуск линейного подхода...")
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    end_time = time.time()
    print(f"Время выполнения линейного подхода: {end_time - start_time:.6f} секунд")

    # Многопроцессный вызов
    print("Запуск многопроцессного подхода...")
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    print(f"Время выполнения многопроцессного подхода: {end_time - start_time:.6f} секунд")
