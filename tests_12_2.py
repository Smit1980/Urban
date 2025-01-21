import unittest

# Пример реализации класса Runner для тестов
class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def walk(self):
        self.distance += 5

    def run(self):
        self.distance += 10


class RunnerTest(unittest.TestCase):
    # Тестирование метода walk
    def test_walk(self):
        runner = Runner("TestRunner")
        for _ in range(10):  # Исправлено на корректный синтаксис Python
            runner.walk()
        self.assertEqual(runner.distance, 50, "Distance should be 50 after walking 10 times.")

    # Тестирование метода run
    def test_run(self):
        runner = Runner("TestRunner")
        for _ in range(10):  # Исправлено на корректный синтаксис Python
            runner.run()
        self.assertEqual(runner.distance, 100, "Distance should be 100 after running 10 times.")

    # Тестирование сравнения двух бегунов
    def test_challenge(self):
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")
        for _ in range(10):  # Исправлено на корректный синтаксис Python
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance, "Distances should not be equal.")

# Запуск тестов
if __name__ == "__main__":
    unittest.main()
