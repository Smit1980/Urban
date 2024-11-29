from threading import Thread
from time import sleep

# Общее количество врагов для всех рыцарей
total_enemies = 100

# Класс Knight, наследуемый от Thread
class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name  # Имя рыцаря
        self.power = power  # Сила рыцаря
        self.days = 0  # Количество дней, которое рыцарь сражается

    def run(self):
        global total_enemies
        print(f"{self.name}, на нас напали!")
        
        while total_enemies > 0:
            self.days += 1
            # Уменьшаем количество врагов на силу рыцаря
            total_enemies -= self.power
            total_enemies = max(0, total_enemies)  # Чтобы врагов не стало меньше 0
            print(f"{self.name}, сражается {self.days} день(дня)..., осталось {total_enemies} воинов.")
            sleep(1)  # Задержка в 1 секунду
        
        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


if __name__ == "__main__":
    # Создание рыцарей
    first_knight = Knight("Sir Lancelot", 10)
    second_knight = Knight("Sir Galahad", 20)
    
    # Запуск потоков
    first_knight.start()
    second_knight.start()
    
    # Ожидание завершения потоков
    first_knight.join()
    second_knight.join()
    
    print("Все битвы закончились!")
