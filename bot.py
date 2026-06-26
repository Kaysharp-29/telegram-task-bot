)from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DISCORD_URL = os.getenv("DISCORD_URL")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🚀 Join Discord", url=DISCORD_URL)],
        [InlineKeyboardButton("✅ I've Joined & Verified", callback_data="verified")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🎉 *Welcome to Taskz Rewards!*\n\n"
        "Complete the Discord verification task.\n\n"
        "1️⃣ Join our Discord\n"
        "2️⃣ Get verified\n"
        "3️⃣ Tap *I've Joined & Verified*",
        parse_mode="Markdown",
        reply_markup=reply_markup,
    )


async def verified(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    await query.message.reply_text(
        "📸 Great!\n\nPlease upload a screenshot showing you're verified in the Discord server."
    )


app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(verified, pattern="verified"))

print("✅ Bot is running...")

app.run_polling()
