import asyncio

from telegram.ext import CommandHandler

from niffler.bot import Bot
from niffler.handlers import start

bot = Bot()
bot.add_handler(CommandHandler("start", start.handler))


try:
    bot.run_polling()
except KeyboardInterrupt:
    print("正在中断...")
finally:
    print("清理资源...")
    asyncio.run(bot.shutdown_bot())
