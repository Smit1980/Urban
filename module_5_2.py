class House:
    def __init__(self, name, number_of_floors):
        """Инициализация объекта с именем и количеством этажей."""
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        """Метод для перемещения на указанный этаж."""
        if 1 <= new_floor <= self.number_of_floors:
            # Выводим поочередно все этажи от 1 до new_floor включительно
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            # Если этаж некорректен, выводим сообщение об ошибке
            print("Такого этажа не существует")

    def __len__(self):
        """Возвращает количество этажей здания."""
        return self.number_of_floors

    def __str__(self):
        """Возвращает строку с названием и количеством этажей."""
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

# Пример использования
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
