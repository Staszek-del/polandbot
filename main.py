import os
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("8009352726:AAEU6T6d_1kQffVEXWjQQsbf0G0uhECGerA")  # ключ из Render

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [KeyboardButton("📄 Документы для визы")],
        [KeyboardButton("🛂 Пересечение границы")],
        [KeyboardButton("🇵🇱 Полезные фразы")],
        [KeyboardButton("📚 Энциклопедия")],
        [KeyboardButton("🆘 Поддержка")]
    ]
    markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    await update.message.reply_text("Привет! Я PolandGPTbot. С чего начнём?", reply_markup=markup)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
