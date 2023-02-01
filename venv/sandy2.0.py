import telebot
from telebot import types

bot = telebot.TeleBot("5608601651:AAHY_d3XgJ14UeEvbT44CWYnexE1UWpIhRQ")

@bot.message_handler(commands=['checkin'])
def checkin(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton("100M")
    item2 = types.KeyboardButton("40/70")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Which type of sand are you checking in?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "100M")
def type1(message):
    bot.send_message(message.chat.id, "You have checked in with 100M.")

@bot.message_handler(func=lambda message: message.text == "40/70")
def type2(message):
    bot.send_message(message.chat.id, "You have checked in with 40/70.")

@bot.message_handler(commands=['sand_list'])
def sand_list(message):
   sand_list = []

while True:
    print("Please choose a type of sand:")
    print("1. White Sand")
    print("2. Black Sand")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        sand_list.append("White Sand")
    elif choice == "2":
        sand_list.append("Black Sand")
    else:
        print("Invalid choice. Please try again.")
        continue

    print("Current list of sand: ", sand_list)

bot.polling()
