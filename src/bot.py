import os
import telebot
from dotenv import load_dotenv

load_dotenv(override=True)

bot = telebot.TeleBot(os.getenv("TOKEN"))
