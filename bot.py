from config import BOT_TOKEN, Data
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text


class Advisor:
    def __init__(self):
        # change it to your own
        bot = Bot(token=BOT_TOKEN)
        dp = Dispatcher(bot)
        data = Data()
        buttons = ["День", "Месяц", "Полная дата", "Какая пара ?", "Расчитать дни"]

        @dp.message_handler(commands=["start", "hello", "help"])
        async def start(message: types.Message):
            msg = str(open("message.txt", "r", encoding="utf-8").read())
            kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
            kb.add(*buttons)
            await message.answer(msg, reply_markup=kb)

        @dp.message_handler(Text(equals=f"{buttons[0]}"))
        async def show_data(message: types.Message):
            text = f"⏸День: {data.this_day_location}\n💬Название: {data.this_day}\n\n" \
                   f"▶Следующий день: {data.next_day_location}\n 💬Название: {data.next_day}"
            await bot.send_message(chat_id=message.chat.id, text=text)

        @dp.message_handler(Text(equals=f"{buttons[1]}"))
        async def show_data(message: types.Message):
            text = f"⏸Месяц: {data.this_month_location}\n💬Название: {data.this_month}\n\n" \
                   f"▶Следующий месяц: {data.next_month_location}\n💬Название: {data.next_month}"
            await bot.send_message(chat_id=message.chat.id, text=text)

        @dp.message_handler(Text(equals=f"{buttons[3]}"))
        async def show_data(message: types.Message):
            text = Data().getLesson()
            await message.answer(text=text)
        self.bot = bot
        self.dp = dp

    def start_bot(self):
        executor.start_polling(self.dp)


if __name__ == '__main__':
    advisor = Advisor()
    advisor.start_bot()
