from telegram.ext import CommandHandler

from niffler.bot import Bot
from niffler.handlers import start

bot = Bot()
bot.add_handler(CommandHandler("start", start.handler))
bot.run_polling()