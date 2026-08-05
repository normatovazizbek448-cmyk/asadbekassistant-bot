import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
from openai import OpenAI

BOT_TOKEN = os.environ["BOT_TOKEN"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

client = OpenAI(api_key=OPENAI_API_KEY)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Assalomu alaykum!\n\nMen Asadbek Assistant AI.\nSavolingizni yozing."
    )

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_text = update.message.text

        response = client.responses.create(
            model="gpt-5",
            input=user_text,
        )

        await update.message.reply_text(response.output_text)

    except Exception as e:
        await update.message.reply_text(f"Xatolik: {e}")

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, chat)
    )

    print("🤖 Asadbek Assistant ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
