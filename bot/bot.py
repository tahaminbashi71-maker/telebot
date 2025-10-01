
import telebot

bot = telebot.TeleBot("8309977542:AAHbGygclFlUZ2tTETuSzmbvQgo7b64TaWw")

@bot.message_handler(commands=["start"])
def welcome(message):
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
def welcome(message):
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
def welcome(ins):
    bot.reply_to(ins , "پیج اینستاگرام ما : javaneh_clothes_children")

    """ -------------------------------------------------------------------- """
@bot.message_handler(commands=["command3"])
def welcome(sit):
    bot.reply_to(sit , "سایت ما : javanehclothes.ir")
    """ -------------------------------------------------------------------- """
@bot.message_handler(commands=["command4"])
def welcome(aboutme):
    bot.reply_to(aboutme , "ما یک سایت پوشاک هستیم")
    """ -------------------------------------------------------------------- """
@bot.message_handler(commands=["command2"])
def welcome(rows):
    bot.reply_to(rows , " محصولات ما  : ")
    """ -------------------------------------------------------------------- """
@bot.message_handler(commands=["command6"])
def welcome(ita):
    bot.reply_to(ita , " کانال ایتا  : ")

bot.polling()