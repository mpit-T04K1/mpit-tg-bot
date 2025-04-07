from src.bot import bot
from src.handlers import start  # noqa


bot.polling(none_stop=True, interval=5)
