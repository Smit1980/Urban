import asyncio

# Асинхронная функция для соревнований одного силача
async def start_strongman(name: str, power: int):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):  # Поднять 5 шаров
        await asyncio.sleep(1 / power)  # Задержка обратно пропорциональна силе
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования.')

# Асинхронная функция для запуска турнира
async def start_tournament():
    # Создаём 3 задачи для разных силачей
    tasks = [
        start_strongman('Pasha', 3),
        start_strongman('Denis', 4),
        start_strongman('Apollon', 5)
    ]
    # Запуск задач параллельно
    await asyncio.gather(*tasks)

# Запуск турнира
if __name__ == '__main__':
    asyncio.run(start_tournament())
