from telegram import Bot


def send_telegram(orders):
    bot = Bot(token='5326387724:AAHfKe8Jw-orUM5ZS6VGTRf2Kk5RprMn-AM')
    # Укажите id своего аккаунта в Telegram
    chat_id = 76411159
    text = 'Нарушение сроков поставки у данных заказов: ' + orders
    # Отправка сообщения
    bot.send_message(chat_id, text)
