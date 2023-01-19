import os
import telebot

API_KEY = os.getenv('5608601651:AAHY_d3XgJ14UeEvbT44CWYnexE1UWpIhRQ')
bot = telebot.TeleBot(API_KEY)
data = staging.list(header="100M")
#start command
@bot.message_handler(command=['start'])
def start(message):
    bot.reply_to(message, "Enter the text you want to show to the user whenever they start the bot")

#sending a message and not replying to a message
@bot.message_handler(command=['hello'])
def help(message):
    bot.send_message(message.chat.id, "what is Guicci")

#@bot.message_handler(func=Staging_list)
#def stage(message):
#request = message.text.split()[1]
#data = 
bot.polling()

