# Пользовательское исключение
class StepValueError(ValueError):
    """Исключение для шага, равного 0"""
    pass

# Класс Iterator
class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError("шаг не может быть равен 0")
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start  # Указатель на текущее значение итерации

    def __iter__(self):
        # Сбрасываем pointer и возвращаем итератор
        self.pointer = self.start
        return self

    def __next__(self):
        # Условие завершения итерации в зависимости от знака step
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration

        # Возвращаем текущее значение pointer и сдвигаем его на step
        current = self.pointer
        self.pointer += self.step
        return current

# Пример использования
try:
    iter1 = Iterator(100, 200, 0)  # Здесь шаг равен 0, должно возникнуть исключение
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print("Шаг указан неверно")

# Примеры с разными итерациями
iter2 = Iterator(-5, 1)  # Шаг по умолчанию = 1
iter3 = Iterator(6, 15, 2)  # Шаг = 2
iter4 = Iterator(5, 1, -1)  # Шаг отрицательный
iter5 = Iterator(10, 1)  # Шаг по умолчанию = 1, итерация невозможна

# Итерация для iter2
for i in iter2:
    print(i, end=' ')
print()

# Итерация для iter3
for i in iter3:
    print(i, end=' ')
print()

# Итерация для iter4
for i in iter4:
    print(i, end=' ')
print()

# Итерация для iter5
for i in iter5:
    print(i, end=' ')
print()
