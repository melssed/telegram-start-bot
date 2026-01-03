import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.enums import ParseMode
import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Получаем токен из переменных окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    logger.error("BOT_TOKEN не найден в .env файле!")
    exit(1)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    user = message.from_user
    logger.info(f"Новый пользователь: {user.id} | @{user.username} | {user.first_name}")
    
    welcome_text = (
        f"✨ <b>Привет, {user.first_name}!</b> ✨\n\n"
        "🎯 Я — тестовый бот, созданный по туториалу!\n"
        "✅ Вы успешно запустили меня командой /start\n\n"
        "📊 <b>Ваша информация:</b>\n"
        f"• ID: <code>{user.id}</code>\n"
        f"• Имя: {user.first_name}\n"
        f"• Фамилия: {user.last_name or 'не указана'}\n"
        f"• Username: @{user.username or 'не указан'}\n\n"
        "🚀 <b>Что дальше?</b>\n"
        "Попробуйте другие команды:\n"
        "/help - получить справку\n"
        "/info - узнать о боте\n\n"
        "💻 Исходный код: github.com/ваш-username/telegram-start-bot-tutorial"
    )
    
    await message.answer(welcome_text)

# Обработчик команды /help
@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    help_text = (
        "🆘 <b>Доступные команды:</b>\n\n"
        "/start - начать работу с ботом\n"
        "/help - получить эту справку\n"
        "/info - информация о боте\n\n"
        "📚 <b>Как это работает?</b>\n"
        "1. Вы отправляете команду\n"
        "2. Бот её обрабатывает\n"
        "3. Вы получаете ответ!"
    )
    await message.answer(help_text)

# Обработчик команды /info
@dp.message(Command("info"))
async def cmd_info(message: types.Message):
    info_text = (
        "🤖 <b>Информация о боте</b>\n\n"
        "Этот бот создан как пример для туториала на GitHub.\n\n"
        "🔧 <b>Технологии:</b>\n"
        "• Python 3.10+\n"
        "• aiogram 3.x\n"
        "• Асинхронное программирование\n\n"
        "⭐ Если проект полезен, поставьте звезду на GitHub!"
    )
    await message.answer(info_text)

# Основная функция
async def main():
    logger.info("Запускаем бота...")
    
    try:
        # Запускаем поллинг (опрос серверов Telegram)
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        logger.info("Бот остановлен")
    finally:
        await bot.session.close()

# Точка входа
if __name__ == "__main__":
    asyncio.run(main())
