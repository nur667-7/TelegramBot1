from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# -----------------------------
# Конфигурация
# -----------------------------
TOKEN = "8742541281:AAFP3Kn9iHIK7Ju19cv9PTMW1uLhzYqZWVU"  # вставь токен от BotFather

SOCIALS = {
    "Instagram": "https://www.instagram.com/saiduali_nurbek/",
    "Telegram": "https://t.me/nigerusl",
    "LinkedIn": "linkedin.com/in/nurbek-saiduali"
}

# -----------------------------
# Кнопки для соцсетей
# -----------------------------
def get_social_buttons():
    buttons = []
    for name, url in SOCIALS.items():
        buttons.append([InlineKeyboardButton(name, url=url)])
    return InlineKeyboardMarkup(buttons)

# -----------------------------
# Обработчики команд
# -----------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "Привет! Я бот, который расскажет обо мне 😊\nВыбери команду:\n/about - обо мне\n/social - соцсети"
    await update.message.reply_text(text)

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Меня зовут Нурбек.\n"
        "Я студент и начинающий IT-разработчик.\n"
        "Люблю Python, Telegram-ботов и создавать полезные проекты."
    )
    await update.message.reply_text(text)

async def social(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Мои соцсети:", reply_markup=get_social_buttons())

# -----------------------------
# Запуск бота
# -----------------------------
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("social", social))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
