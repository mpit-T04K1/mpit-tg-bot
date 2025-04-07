import os
from dotenv import load_dotenv
from telebot import types

from src.bot import bot

load_dotenv(override=True)

@bot.message_handler(func=lambda message: True)
def start(message: types.Message):
    link = os.getenv("REGISTRATION_URL")
    link = link.replace("{username}", str(message.chat.username), 1)
    link = link.replace("{id}", str(message.chat.id), 1)

    markup = types.InlineKeyboardMarkup()
    btn_reg = types.InlineKeyboardButton(text='Тык', url=link)
    markup.add(btn_reg)
    bot.send_message(message.from_user.id, "По кнопке можно продолжить регистрацию", reply_markup = markup)
