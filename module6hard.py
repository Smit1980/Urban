import math

class Figure:
    sides_count = 0  # Количество сторон, значение определяется в дочерних классах

    def __init__(self, color, *sides):
        self.__color = list(color)
        self.filled = False

        # Если количество сторон не совпадает с sides_count, устанавливаем единичные стороны
        if len(sides) == self.sides_count:
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count

    def get_color(self):
        """Возвращает цвет в формате RGB"""
        return self.__color

    def __is_valid_color(self, r, g, b):
        """Проверка, является ли цвет корректным"""
        return all(isinstance(val, int) and 0 <= val <= 255 for val in (r, g, b))

    def set_color(self, r, g, b):
        """Устанавливает цвет, если он корректен"""
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print(f"Нельзя сменить цвет на ({r}, {g}, {b})")

    def __is_valid_sides(self, *new_sides):
        """Проверка корректности новых значений для сторон"""
        return (
            len(new_sides) == self.sides_count and
            all(isinstance(side, int) and side > 0 for side in new_sides)
        )

    def get_sides(self):
        """Возвращает список сторон"""
        return self.__sides

    def __len__(self):
        """Возвращает периметр фигуры"""
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        """Устанавливает новые стороны, если их количество корректно"""
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)  # Рассчитываем радиус

    def get_square(self):
        """Возвращает площадь круга"""
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        """Возвращает площадь треугольника по формуле Герона"""
        a, b, c = self.get_sides()
        s = sum(self.get_sides()) / 2  # Полупериметр
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        # Устанавливаем 12 одинаковых сторон или заполняем единичными значениями
        if len(sides) == 1:
            super().__init__(color, *([sides[0]] * self.sides_count))
        else:
            super().__init__(color, *([1] * self.sides_count))

    def get_volume(self):
        """Возвращает объем куба"""
        edge = self.get_sides()[0]  # Берём любое ребро, т.к. они все равны
        return edge ** 3


# Пример использования
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
