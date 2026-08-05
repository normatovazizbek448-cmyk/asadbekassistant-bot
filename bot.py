from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "BOT_TOKENINGIZ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Salom! Men Asadbek Assistantman 🤖\n"
        "Sizga yordam berishga tayyorman."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Buyruqlar:\n"
        "/start - Botni ishga tushirish\n"
        "/help - Yordam"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))

app.run_polling()
