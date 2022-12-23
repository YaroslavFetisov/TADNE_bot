from aiogram import Bot, Dispatcher, executor, types
from api import get_pic

tg_token = '5260788214:AAEUJaOBP38SgxqAjO_u54FF0nLoNuPvIhA'

bot = Bot(token=tg_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Зіґ хайль!")


@dp.message_handler(commands=["go"])
async def pic(req: types.Message):
    try:
        await req.reply_photo(get_pic(req.text))
        await req.reply("Ви тільки що витратили 35 коп з рахунку його величності Ярослава. Ваша душа тепер належить йому")
    except:
        await req.reply("Ідеш нахуй по причині: \"Кончений долбойоб\"")


if __name__ == '__main__':
    executor.start_polling(dp)