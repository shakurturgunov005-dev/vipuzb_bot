import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# Tokeningizni shu yerga qo'ying
TOKEN = "8415242929:AAFK7rskNNNW2UqaHUcW1SL4Yd-Tl2dt3Z4"

bot = telebot.TeleBot(TOKEN)


# Asosiy menyuni yaratamiz
def create_main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    
    btn1 = KeyboardButton("Salom 👋")
    btn2 = KeyboardButton("Yordam ❓")
    btn3 = KeyboardButton("Men haqimda ℹ️")
    btn4 = KeyboardButton("Rasmlar 🖼️")
    
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    
    return markup


@bot.message_handler(commands=['start', 'menu'])
def send_welcome(message):
    text = "Salom! Men senga yordam berish uchun yaratildim 😊\n\nQuyidagilardan birini tanla:"
    bot.reply_to(message, text, reply_markup=create_main_menu())


@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    text = message.text.lower()
    
    if "salom" in text or "👋" in text:
        bot.reply_to(message, "Salom! Qanday yordam bera olaman? 😄")
    
    elif "yordam" in text or "❓" in text:
        bot.reply_to(message, "Hozircha men quyidagilarni bilaman:\n/start - menyuni chiqarish\n/menu - menyuni chiqarish\n\nYana nimalar qo'shamiz deb o'ylaysan?")
    
    elif "men haqimda" in text or "ℹ️" in text:
        bot.reply_to(message, "Men Pyto’da ishlaydigan oddiy, lekin tez orada aqlli bot bo‘laman 😎\nHozircha sen bilan suhbatlashaman va tugmalarni sinab ko‘raman.")
    
    elif "rasmlar" in text or "🖼️" in text:
        bot.reply_to(message, "Hozircha rasm yubora olmayman, lekin keyingi qadamda mushuk yoki it rasmlarini yuborishni qo‘shamiz! 🐱🐶")
    
    else:
        bot.reply_to(message, f"Sening yozganing: {message.text}\n\nMenyudan biror narsani tanlab ko‘r 😊")


print("Bot ishga tushmoqda...")
bot.infinity_polling(allowed_updates=["message"])
