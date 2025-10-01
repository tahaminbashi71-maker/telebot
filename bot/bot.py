import os
import time
import threading
import telebot
from flask import Flask

bot = telebot.TeleBot("8309977542:AAHbGygclFlUZ2tTETuSzmbvQgo7b64TaWw")
app = Flask(__name__)

@app.route("/")
def home():
    return "ربات تلگرام فعال است ✅", 200

@bot.message_handler(commands=["start"])
def welcome1(message):
    text = "سلام به ربات تلگرامی جوانه خوش آمدید 🌱\n"
    text +=  " \n"
    text += "/command1 = شروع دوباره 🔄 \n"
    text +=  " \n"
    text += "/command2 = محصولات ما \n"
    text +=  " \n"
    text += "/command3 = سایت ما \n"
    text +=  " \n"
    text += "/command4 = درباره ما \n"
    text +=  " \n"
    text += "/command5 = پیج ایسنتاگرام \n"
    text +=  " \n"
    text += "/command6 = کانال ایتا \n"
    bot.reply_to(message , text)
    """ -------------------------------------------------------------------- """
@bot.message_handler(commands=["command1"])
def welcome2(message):
    text = "سلام به ربات تلگرامی جوانه خوش آمدید 🌱\n"
    text +=  " \n"
    text += "/command1 = شروع دوباره 🔄 \n"
    text +=  " \n"
    text += "/command2 = محصولات ما \n"
    text +=  " \n"
    text += "/command3 = سایت ما \n"
    text +=  " \n"
    text += "/command4 = درباره ما \n"
    text +=  " \n"
    text += "/command5 = پیج ایسنتاگرام \n"
    text +=  " \n"
    text += "/command6 = کانال ایتا \n"
    bot.reply_to(message , text)
    """ -------------------------------------------------------------------- """
@bot.message_handler(commands=["command5"])
def welcome3(ins):
    bot.reply_to(ins , "پیج اینستاگرام ما : javaneh_clothes_children")

    """ -------------------------------------------------------------------- """
@bot.message_handler(commands=["command3"])
def welcome4(sit):
    bot.reply_to(sit , "سایت ما : javanehclothes.ir")
    """ -------------------------------------------------------------------- """
@bot.message_handler(commands=["command4"])
def welcome5(aboutme):
    bot.reply_to(aboutme , "ما یک سایت پوشاک هستیم")
    """ -------------------------------------------------------------------- """
@bot.message_handler(commands=["command2"])
def welcome6(rows):
    text = "محصولات ما \n"
    text +=  " \n"
    text += "سایت \n"
    text += "javanehclothes.ir \n"
    text += "کانال تلگرام \n"
    text += "https://t.me/javaneh_childrens_clothing \n"
    bot.reply_to(rows , text)
    """ -------------------------------------------------------------------- """
@bot.message_handler(commands=["command6"])
def welcome7(ita):
    bot.reply_to(ita , " کانال ایتا  : ")

def start_polling():
    while True:
        try:
            bot.infinity_polling(timeout=60, long_polling_timeout=90, skip_pending=True)
        except Exception as e:
            print("خطای polling:", e)
            time.sleep(5)

if __name__ == "__main__":
    # اجرای polling در یک Thread جدا
    t = threading.Thread(target=start_polling, daemon=True)
    t.start()

    # اجرای Flask (پورت باید از Render گرفته بشه)
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)



