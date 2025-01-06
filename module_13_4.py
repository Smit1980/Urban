import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import filters

# Установите токен вашего бота
API_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# Логирование
logging.basicConfig(level=logging.INFO)

# Хранилище состояний в памяти
storage = MemoryStorage()

# Создание экземпляра бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)

# Группа состояний
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

# Обработка команды 'Calories' и начало цепочки
@dp.message_handler(text='Calories')
async def set_age(message: types.Message):
    await message.reply("Введите свой возраст:")
    await UserState.age.set()

# Обработка возраста
@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))  # Сохраняем возраст
    await message.reply("Введите свой рост (в см):")
    await UserState.growth.set()

# Обработка роста
@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=int(message.text))  # Сохраняем рост
    await message.reply("Введите свой вес (в кг):")
    await UserState.weight.set()

# Обработка веса и вычисление нормы калорий
@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=int(message.text))  # Сохраняем вес

    # Получаем все данные из состояния
    data = await state.get_data()
    age = data['age']
    growth = data['growth']
    weight = data['weight']

    # Формула Миффлина - Сан Жеора для мужчин
    bmr = 10 * weight + 6.25 * growth - 5 * age + 5

    # Отправляем результат пользователю
    await message.reply(f"Ваша норма калорий: {bmr:.2f} ккал/день.")
    
    # Завершаем состояние
    await state.finish()

# Запуск бота
if __name__ == '__main__':
    print("Bot is running...")
    executor.start_polling(dp, skip_updates=True)
