import os
import requests

# Получите токен бота из переменной окружения
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


def send_telegram_message(chat_id, text):
    """Отправляет сообщение через Telegram бота."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    response = requests.post(url, json=payload)
    return response.json()
