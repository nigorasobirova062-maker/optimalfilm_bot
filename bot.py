from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = 8560499931:AAFwT9papuUrzpNX5dOu7KgFg83bO06cV6Q

SPONSOR_CHANNEL = "@optimalfilm_bot"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    member = await context.bot.get_chat_member(SPONSOR_CHANNEL, user.id)

    if member.status not in ["member", "administrator", "creator"]:
        await update.message.reply_text(
            f"Botdan foydalanish uchun avval {cartoon_uzbe} kanaliga obuna bo‘ling!"
        )
        return

    await update.message.reply_text(
        "Assalomu alaykum!\nFilm yoki multfilm kodini yuboring 🎬"
    )

async def get_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    code = update.message.text
    await update.message.reply_text(
        f"🎥 Siz yuborgan kod: {code}\n\nBu yerda film chiqadi."
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, get_code))

app.run_polling()
