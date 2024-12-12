from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from niffler.config import get_settings


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message and update.effective_user:
        await update.message.reply_text(f"Hello {update.effective_user.first_name}")


app = ApplicationBuilder().token(get_settings().tg_bot_token).build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()
