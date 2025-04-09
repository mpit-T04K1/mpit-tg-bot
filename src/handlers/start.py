from telebot import types
from src.settings import settings
from src.bot import bot

from src.database.session import Session
from src.service import UserService
from src.schemas import UserSchema, UserModifySchema


@bot.message_handler(func=lambda message: True)
def start(message: types.Message):
    user = message.from_user

    markup = types.InlineKeyboardMarkup()
    btn_reg = types.InlineKeyboardButton(text='Тык', url=settings.REGISTRATION_URL)
    markup.add(btn_reg)
    bot.send_message(user.id, "По кнопке можно продолжить регистрацию", reply_markup = markup)

    try:
        with Session() as session:
            user_service = UserService(session=session)
            if user_service.exist(user.id):
                user_service.edit(UserModifySchema(
                    id=user.id,
                    username=user.username,
                    first_name=user.first_name,
                    last_name=user.last_name
                ))
            else:
                user_service.add(UserSchema(
                    id=user.id,
                    username=user.username,
                    first_name=user.first_name,
                    last_name=user.last_name
                ))
    except Exception as e:
        print(type(e), str(e))
        print(dict(
            id=user.id,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name
        ))

    
