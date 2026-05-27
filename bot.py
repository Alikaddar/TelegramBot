import os
import telebot
from flask import Flask
from threading import Thread

TOKEN = "8606111276:AAGBJtV3HUhGUI2pm0EVR16A8sa8VMEFvsQ"
bot = telebot.TeleBot(TOKEN)

banned_words = [
    'شباب', 'بنات', 'يكلمني', 'خاص', 'يراسلني خاص', 'مجال مرة حلو',
    'ارباح', 'أرباح', 'الارباح', 'الأرباح', 'استثمار', 'إستثمار', 'تداول', 'فلوس', 't.me/', 'منصة', 'واتساب',
    'مسابقة', 'اربح معنا', 'سجل هنا', 'usdt', 'USDT', 'سحب', 'إيداع', 'حوالات', 
    'داخلية', 'خارجية', 'مالية', 'بنكية', 'لي يبي يكلمني', 'عملات', 'مجال',
    'نيك مك', 'قحبة', 'قود', 'كلب', 'حمار', 'رخيس', 'w9', 'الله ينعلك'
]

@bot.message_handler(func=lambda message: True)
def clean_group(message):
    text = message.text.lower()
    for word in banned_words:
        if word in text:
            try:
                bot.delete_message(message.chat.id, message.message_id)
            except:
                pass
            break

app = Flask(__name__)

@app.route('/')
def home():
    return "CleanGroupDZ_bot is running!"

def run_server():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    server_thread = Thread(target=run_server)
    server_thread.start()
    bot.polling(non_stop=True)
    
