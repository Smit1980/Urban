import threading
import random
from time import sleep

class Bank:
    def __init__(self):
        self.balance = 0  # Изначальный баланс банка
        self.lock = threading.Lock()  # Блокировка для потоков

    def deposit(self):
        """Метод пополнения баланса банка"""
        for _ in range(100):  # 100 транзакций пополнения
            amount = random.randint(50, 500)  # Случайное число для пополнения
            with self.lock:  # Используем контекстный менеджер для блокировки
                self.balance += amount
                print(f"Пополнение: {amount}. Баланс: {self.balance}")
                if self.balance >= 500 and self.lock.locked():
                    self.lock.release()  # Разблокируем замок, если баланс >= 500
            sleep(0.001)  # Имитация времени выполнения транзакции

    def take(self):
        """Метод снятия баланса банка"""
        for _ in range(100):  # 100 транзакций снятия
            amount = random.randint(50, 500)  # Случайное число для снятия
            print(f"Запрос на {amount}")
            with self.lock:  # Используем контекстный менеджер для блокировки
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
                    self.lock.acquire()  # Заблокируем поток, если недостаточно средств
            sleep(0.001)  # Имитация времени выполнения транзакции


if __name__ == "__main__":
    # Создаём объект банка
    bk = Bank()

    # Создаём потоки для методов deposit и take
    th1 = threading.Thread(target=Bank.deposit, args=(bk,))
    th2 = threading.Thread(target=Bank.take, args=(bk,))

    # Запускаем потоки
    th1.start()
    th2.start()

    # Ожидаем завершения потоков
    th1.join()
    th2.join()

    # Выводим итоговый баланс
    print(f"Итоговый баланс: {bk.balance}")
