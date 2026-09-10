from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "PASTE_YOUR_BOT_TOKEN_HERE"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎬 Welcome to Video Magnet!\n\n"
        "Send me a video URL and I'll analyze it."
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Video Magnet Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
