from telegram.ext import ApplicationBuilder

from niffler.config import settings


class Bot:
    def __init__(self):
        self.app = ApplicationBuilder().token(settings.tg_bot_token).build()

    def add_handler(self, handler):
        self.app.add_handler(handler)

    def run_polling(self):
        self.app.run_polling()

    def run_webhook(self):
        self.app.run_webhook()
