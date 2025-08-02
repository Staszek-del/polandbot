from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)
import os

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📄 Документы для визы", callback_data="visa_docs")],
        [InlineKeyboardButton("🛂 Пересечение границы", callback_data="border_docs")],
        [InlineKeyboardButton("🇵🇱 Полезные фразы", callback_data="phrases")],
        [InlineKeyboardButton("📚 Энциклопедия", callback_data="guide")],
        [InlineKeyboardButton("💬 Поддержка", callback_data="support")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выберите нужный раздел:", reply_markup=reply_markup)

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = {
        "visa_docs": "📄 Вот список документов для визы...",
        "border_docs": "🛂 Вот документы для пересечения границы...",
        "phrases": "🇵🇱 Полезные фразы на польском:\n- Dzień dobry — Добрый день\n- Dziękuję — Спасибо",
        "guide": "📚 Энциклопедия доступна в гайде: Poland Guide 📎",
        "support": "💬 Напишите нам: @support_helper_bot",
    }
    await query.edit_message_text(data.get(query.data, "Неизвестная команда"))

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_button))
    app.run_polling()

