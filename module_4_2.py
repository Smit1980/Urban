def test_function():
    # Определение внутренней функции
    def inner_function():
        print("Я в области видимости функции test_function")

    # Вызов внутренней функции
    inner_function()

# Вызов test_function
test_function()
