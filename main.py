import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# --- Команды ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("📄 Документы для визы"), KeyboardButton("🛂 Документы для пересечения границы")],
        [KeyboardButton("🗣 Полезные фразы на польском")],
        [KeyboardButton("📘 Всё, что нужно знать"), KeyboardButton("📩 Связаться с поддержкой")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "👋 Привет! Я PolandGPTbot.\nВыбери, что тебя интересует:",
        reply_markup=reply_markup
    )

# Ответы на кнопки

async def visa_documents(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📄 *Документы для визы:*\n- Паспорт\n- Фото 3.5x4.5 см\n- Страховка\n- Приглашение или умова\n- Заполненная анкета\n- Квитанция об оплате\n- Доп. документы по требованию консульства"
    )

async def border_documents(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛂 *Документы для пересечения границы:*\n- Паспорт\n- Виза или биометрия\n- Страховка\n- Приглашение или умова\n- Адрес проживания\n- Фото 3.5x4.5 см (на всякий случай)"
    )

async def polish_phrases(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🗣 Полезные фразы на польском языке на каждый день:\n👉 [Открыть список](https://zgoda-studio.pl/blogs/poleznyie-frazyi-na-polskom-na-kazhdyij-den/)",
        parse_mode='Markdown',
        disable_web_page_preview=True
    )

async def guide(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📘 Всё, что нужно знать:\nЗдесь описываю твой каждый шаг:\n- Выбор вакансии и работодателя\n- Выбор города\n- Общение на границе\n- Как не попасть к мошенникам\n\n👉 [Скачать гайд](https://stanzborowski.gumroad.com/l/polandguide)",
        parse_mode='Markdown',
        disable_web_page_preview=True
    )

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📩 Поддержка: @st_zborowski")

# Роутинг по тексту кнопок
async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "📄 Документы для визы":
        await visa_documents(update, context)
    elif text == "🛂 Документы для пересечения границы":
        await border_documents(update, context)
    elif text == "🗣 Полезные фразы на польском":
        await polish_phrases(update, context)
    elif text == "📘 Всё, что нужно знать":
        await guide(update, context)
    elif text == "📩 Связаться с поддержкой":
        await contact(update, context)
    else:
        await update.message.reply_text("❓ Не понял запрос. Пожалуйста, выбери вариант из меню.")

# --- Запуск бота ---
app = ApplicationBuilder().token("8009352726:AAEU6T6d_1kQffVEXWjQQsbf0G0uhECGerA").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", start))  # Можно убрать при желании
app.add_handler(CommandHandler("go", start))    # Альтернатива /help
app.add_handler(CommandHandler("contact", contact))
app.add_handler(CommandHandler("guide", guide))

from telegram.ext import MessageHandler, filters
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))

if __name__ == '__main__':
    app.run_polling()
