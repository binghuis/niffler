from telegram import Update
from telegram.ext import ContextTypes


async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message and update.effective_user:
        await update.message.reply_text(f"Hello {update.effective_user.first_name}")
