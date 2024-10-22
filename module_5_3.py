class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __len__(self):
        return self.number_of_floors

    # Сравнение по количеству этажей
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return False

    # Арифметические операторы
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

# Пример выполнения программы
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# Вывод объектов
print(h1)
print(h2)

# Сравнение
print(h1 == h2)  # __eq__

# Увеличение этажей
h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

# Другие операторы сравнения
print(h1 > h2)   # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)   # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
