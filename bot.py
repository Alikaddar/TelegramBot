import telebot

TOKEN = "8606111276:AAHjh2KgAtjt8dfDn-vcxUJM9JslmynaWwE"
bot = telebot.TeleBot(TOKEN)

# الكلمات الممنوعة
banned_words = ['W9', 'قود', 'استثمار', 'ارباح', 'فلوس', 'اربح', 'منصة', 'تداول', 'كلمني خاص', 't.me/']

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
