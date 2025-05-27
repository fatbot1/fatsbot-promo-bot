import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

BOT_TOKEN = os.environ.get("BOT_TOKEN")

WELCOME_TEXT = (
    "🎲 *Welcome to FatsBot Promo Bot!*\n\n"
    "Use /promo to get promo tools for the FatsBot dice game."
)

PROMO_TEXT = (
    "🚀 *FatsBot Dice Game Promo Pack*\n\n"
    "Copy and share this text or image in your groups to invite friends!\n\n"
    "🎲 Play FatsBot Dice: [t.me/FatsBot](https://t.me/FatsBot)\n"
    "#FatsBot #DiceGame"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_TEXT, parse_mode="Markdown")

async def promo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(PROMO_TEXT, parse_mode="Markdown")

def main():
    if not BOT_TOKEN:
        logging.error("BOT_TOKEN environment variable not set.")
        return
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("promo", promo))
    app.run_polling()

if __name__ == '__main__':
    main()
