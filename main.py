from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привіт! Я PolandBot — твій помічник із переїзду до Польщі 🇵🇱.\n\n"
        "Спробуй команди:\n"
        "/instruction — покрокова інструкція\n"
        "/documents — список документів\n"
        "/help — допомога"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Пиши /instruction або /documents, щоб почати 🙂")

if __name__ == '__main__':
    import os
    from dotenv import load_dotenv
    load_dotenv()

    TOKEN = os.getenv("BOT_TOKEN")

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.run_polling()
