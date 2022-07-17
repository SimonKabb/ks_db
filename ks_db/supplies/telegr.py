from telegram import Bot
from .varriable import TOKEN, CHAT_ID


def send_telegram(orders):
    bot = Bot(token=TOKEN)
    chat_id = CHAT_ID
    text = 'Нарушение сроков поставки у данных заказов: ' + orders
    bot.send_message(chat_id, text)
