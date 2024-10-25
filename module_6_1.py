# Родительский класс для животных
class Animal:
    alive = True  # Атрибут класса, указывает что животное живо
    fed = False   # Атрибут класса, указывает что животное не накормлено

    def __init__(self, name):
        self.name = name  # Индивидуальный атрибут экземпляра

    def eat(self, food):
        """Метод для поедания растений"""
        if isinstance(food, Plant):  # Проверяем, является ли еда растением
            if food.edible:  # Если растение съедобно
                print(f"{self.name} съел {food.name}")
                self.__class__.fed = True  # Животное накормлено, изменяем атрибут класса
            else:  # Если растение несъедобно
                print(f"{self.name} не стал есть {food.name}")
                self.__class__.alive = False  # Животное погибает, изменяем атрибут класса
        else:
            print(f"{self.name} не ест {food}")

# Родительский класс для растений
class Plant:
    edible = False  # Атрибут класса, по умолчанию растение несъедобное

    def __init__(self, name):
        self.name = name  # Индивидуальный атрибут экземпляра

# Классы-наследники для животных
class Mammal(Animal):
    pass  # У млекопитающего просто наследуются атрибуты и метод eat

class Predator(Animal):
    pass  # У хищника просто наследуются атрибуты и метод eat

# Классы-наследники для растений
class Flower(Plant):
    pass  # Цветы несъедобные по умолчанию

class Fruit(Plant):
    edible = True  # Фрукты съедобн
