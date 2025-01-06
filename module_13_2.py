import logging
from aiogram import Bot, Dispatcher, executor, types

# Установите токен вашего бота
API_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# Включение логирования
logging.basicConfig(level=logging.INFO)

# Создание экземпляра бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Обработка команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    print('Привет! Я бот помогающий твоему здоровью.')  # Вывод в консоль
    await message.reply("Привет! Я бот помогающий твоему здоровью.")  # Ответ пользователю

# Обработка всех остальных сообщений
@dp.message_handler()
async def all_messages(message: types.Message):
    print('Введите команду /start, чтобы начать общение.')  # Вывод в консоль
    await message.reply("Введите команду /start, чтобы начать общение.")  # Ответ пользователю

# Запуск бота
if __name__ == '__main__':
    print("Bot is running...")
    executor.start_polling(dp, skip_updates=True)
