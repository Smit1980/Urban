class House:
    # Атрибут класса для хранения истории домов
    houses_history = []

    def __new__(cls, *args, **kwargs):
        # Создание нового объекта
        instance = super(House, cls).__new__(cls)

        # Добавление названия здания в историю
        if args:
            cls.houses_history.append(args[0])  # Название здания в args[0]
        
        return instance

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __del__(self):
        # Сообщение при удалении объекта
        print(f"{self.name} снесён, но он останется в истории")

# Пример выполнения программы
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

h2 = House('ЖК Акация', 20)
print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

# После завершения программы, если не удалить объект явно, Python сам вызовет __del__ для h1
