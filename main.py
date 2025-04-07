from dotenv import load_dotenv

from src.bot import bot
from src.handlers import start  # noqa

load_dotenv(override=True)

# print("Message handlers:")
# for handler in bot.message_handlers:
#     print(handler['function'].__name__)
# for handler in bot.callback_query_handlers:
#     print(handler['function'].__name__)

bot.polling(none_stop=True, interval=5)
