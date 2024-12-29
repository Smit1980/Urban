import unittest
import logging

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename="runner_tests.log",
    filemode="w",  # Запись с заменой
    encoding="utf-8",
    format="%(levelname)s: %(message)s"
)

# Предположительная реализация класса Runner (обновленная с проверкой типов)
class Runner:
    def __init__(self, name, speed):
        if not isinstance(name, str):
            raise TypeError("Имя бегуна должно быть строкой")
        if not isinstance(speed, (int, float)) or speed < 0:
            raise ValueError("Скорость должна быть неотрицательным числом")
        self.name = name
        self.speed = speed
        self.distance = 0

    def walk(self):
        self.distance += 5

    def run(self):
        self.distance += 10


# Класс тестов с логированием
class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            # Создание объекта с неверной скоростью
            runner = Runner(name="Test Runner", speed=-5)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s", str(e))

    def test_run(self):
        try:
            # Создание объекта с неверным типом имени
            runner = Runner(name=123, speed=10)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s", str(e))


if __name__ == "__main__":
    unittest.main(verbosity=2)
