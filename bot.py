import telebot

TOKEN = "8606111276:AAGBJtV3HUhGUI2pm0EVR16A8sa8VMEFvsQ"
bot = telebot.TeleBot(TOKEN)

# القائمة الموسعة والنهائية حسب طلبك
banned_words = [
    'ارباح', 'أرباح', 'الارباح', 'الأرباح', 
    'إستثمار', 'استثمار', 'تداول', 'مجال مرة حلو',
    'شباب', 'بنات', 'يكلمني خاص', 'يراسلني خاص',
    'قود', 'الله ينعلك', 'كلب', 'حمار', 'w9',
    'منصة', 'فلوس', 't.me/', 'واتساب', 'واتس'
]

@bot.message_handler(func=lambda message: True)
def clean_group(message):
    # تحويل النص للحروف الصغيرة وتجاهل المسافات الزائدة
    text = message.text.lower() if message.text else ""
    
    for word in banned_words:
        if word in text:
            try:
                bot.delete_message(message.chat.id, message.message_id)
                bot.ban_chat_member(message.chat.id, message.from_user.id)
                print(f"تم حظر كلمة ممنوعة: {word}")
                break
            except Exception as e:
                print(f"Error: {e}")

print("The sniper bot is active! 🛡️")
bot.infinity_polling()

