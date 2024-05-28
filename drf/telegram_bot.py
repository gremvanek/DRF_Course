import os

from telegram import Bot

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=TELEGRAM_TOKEN)


def send_message(chat_id, text):
    """
    Отправка сообщения через бота Telegram
    """
    bot.send_message(chat_id=chat_id, text=text)
