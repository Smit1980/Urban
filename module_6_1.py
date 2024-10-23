# Родительский класс для животных
class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True  # Живой по умолчанию
        self.fed = False   # Накормлен ли по умолчанию

    def eat(self, food):
        """Метод для поедания растений"""
        if isinstance(food, Plant):  # Проверяем, является ли еда растением
            if food.edible:  # Если съедобно
                print(f"{self.name} съел {food.name}")
                self.fed = True  # Животное накормлено
            else:  # Если не съедобно
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False  # Животное погибает
        else:
            print(f"{self.name} не ест {food}")

# Родительский класс для растений
class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False  # По умолчанию растение несъедобное

# Классы-наследники для животных
class Mammal(Animal):
    pass  # У млекопитающего просто наследуются атрибуты и метод eat

class Predator(Animal):
    pass  # У хищника просто наследуются атрибуты и метод eat

# Классы-наследники для растений
class Flower(Plant):
    pass  # Цветы несъедобные по умолчанию

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Фрукты съедобные

# Пример использования
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)  # Волк с Уолл-Стрит
print(p1.name)  # Цветик семицветик

print(a1.alive)  # True, Волк жив
print(a2.fed)    # False, Хатико не накормлен

a1.eat(p1)       # Волк пытается съесть цветок
a2.eat(p2)       # Хатико ест апельсин

print(a1.alive)  # False, Волк погиб
print(a2.fed)    # True, Хатико накормлен
