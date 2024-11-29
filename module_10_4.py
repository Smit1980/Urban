from threading import Thread
from queue import Queue
from random import randint
from time import sleep

# Класс Table
class Table:
    def __init__(self, number):
        self.number = number  # Номер стола
        self.guest = None  # Гость за столом (изначально None)

# Класс Guest
class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name  # Имя гостя

    def run(self):
        # Имитируем процесс приёма пищи задержкой от 3 до 10 секунд
        sleep(randint(3, 10))

# Класс Cafe
class Cafe:
    def __init__(self, *tables):
        self.tables = tables  # Список столов в кафе
        self.queue = Queue()  # Очередь гостей

    def guest_arrival(self, *guests):
        """
        Обрабатывает прибытие гостей.
        Если есть свободный стол, сажает гостя.
        Если столов нет, отправляет гостя в очередь.
        """
        for guest in guests:
            # Ищем первый свободный стол
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()  # Запускаем поток гостя
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    break
            else:
                # Если свободных столов нет, отправляем гостя в очередь
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        """
        Имитирует обслуживание гостей, освобождает столы,
        обслуживает очередь.
        """
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None:
                    # Проверяем, завершил ли гость приём пищи
                    if not table.guest.is_alive():
                        print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                        print(f"Стол номер {table.number} свободен")
                        table.guest = None  # Освобождаем стол

                        # Если очередь не пуста, пересаживаем следующего гостя
                        if not self.queue.empty():
                            next_guest = self.queue.get()
                            table.guest = next_guest
                            next_guest.start()  # Запускаем поток нового гостя
                            print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
            sleep(1)  # Задержка для проверки состояний

# Основной блок программы
if __name__ == "__main__":
    # Создаём столы
    tables = [Table(number) for number in range(1, 6)]

    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]

    # Создаём гостей
    guests = [Guest(name) for name in guests_names]

    # Создаём кафе с указанными столами
    cafe = Cafe(*tables)

    # Приём гостей
    cafe.guest_arrival(*guests)

    # Обслуживание гостей
    cafe.discuss_guests()
