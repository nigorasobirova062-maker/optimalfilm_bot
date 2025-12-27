import telebot

TOKEN = "8560499931:AAFwT9papuUrzpNX5dOu7KgFg83bO06cV6Q"
bot = telebot.TeleBot(TOKEN)

# Homiy kanallar
CHANNELS = [
    "@cartoon_uzbe",
    "https://www.instagram.com/qrbnv.sh?igsh=MXdjbXIxOHY5NDVjNw=="
    "https://www.instagram.com/akhtamovv.11?igsh=dmhlcGRvcXJxNGJ6
    "https://www.instagram.com/kurbonov_ice?igsh=d3dwZjQxdjdrdHYy
]

def check_sub(user_id):
    for channel in CHANNELS:
        try:
            status = bot.get_chat_member(channel, user_id).status
            if status not in ["member", "administrator", "creator"]:
                return False
        except:
            return False
    return True

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id

    if not check_sub(user_id):
        text = "❌ Avval homiy kanallarga obuna bo‘ling:\n\n"
        for ch in CHANNELS:
            text += f"👉 {ch}\n"
        text += "\nObuna bo‘lgach yana /start bosing"
        bot.send_message(message.chat.id, text)
    else:
        bot.send_message(message.chat.id, "✅ Rahmat! Endi film kodini yuboring 🎬")

bot.polling()
