import telebot

# التوكن الجديد والنهائي
TOKEN = "8606111276:AAGBJtV3HUhGUI2pm0EVR16A8sa8VMEFvsQ"
bot = telebot.TeleBot(TOKEN)

# الكلمات الممنوعة
banned_words = ['ارباح', 'أرباح', 'استثمار', 'منصة', 'تداول', 'فلوس', 't.me/']

@bot.message_handler(func=lambda message: True)
def clean_group(message):
    text = message.text if message.text else ""
    for word in banned_words:
        if word.lower() in text.lower():
            try:
                bot.delete_message(message.chat.id, message.message_id)
                bot.ban_chat_member(message.chat.id, message.from_user.id)
                break
            except:
                pass

print("Bot is ready! 🛡️")
bot.infinity_polling()

