import unittest
from unittest.mock import patch

from drf.telegram_bot import send_telegram_message, TELEGRAM_BOT_TOKEN


class TestTelegramBot(unittest.TestCase):
    @patch('drf.telegram_bot.requests.post')
    def test_send_telegram_message(self, mock_post):
        # Подготовка мокового ответа
        mock_post.return_value.json.return_value = {'ok': True}

        # Вызов функции send_telegram_message
        chat_id = '1002245786508'
        message_text = 'Тестовое сообщение'
        response = send_telegram_message(chat_id, message_text)

        # Проверка, что функция отправила запрос на корректный URL
        mock_post.assert_called_once_with(
            'https://api.telegram.org/bot{}/sendMessage'.format(TELEGRAM_BOT_TOKEN),
            json={'chat_id': chat_id, 'text': message_text}
        )

        # Проверка, что функция вернула корректный ответ
        self.assertEqual(response, {'ok': True})


if __name__ == '__main__':
    unittest.main()