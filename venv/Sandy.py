import time
import telebot
from telebot import types

bot_token = '5608601651:AAHY_d3XgJ14UeEvbT44CWYnexE1UWpIhRQ'
bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])
def send_welcome (message):
	bot.reply_to(message, 'Welcome! MUFUCKA! :D!')
	

@bot.inline_handler(lambda query: query.query == 'text')
def query_text(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', 'Result', types.InputTextMessageContent('Result message.'))
        r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('Result message2.'))
        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)

def handle_message(update, context):
	if text == 'boom' in text:
		return bot.reply_to (message, 'You have been added to the Staging list, Please wait to be called to the well! Thank You!')
	if '100' in text:
		return 'You have been added to the Staging list, Please wait to be called to the well! Thank You!'

	return 'Please Check in by saying truck # Sand type "EX: 100 or 4070"'	

forty_seventy_list = []  # Initialize an empty list to store "40/70" phrases
hundred_m_list = []  # Initialize an empty list to store "100M" phrases

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Use a regular expression to search for the "40/70" phrase in the message text
    forty_seventy_match = re.search(r'40/70', message.text)
    
    # If the "40/70" phrase was found, add it to the list
    if forty_seventy_match:
        forty_seventy_list.append(forty_seventy_match.group())
    
    # Use a regular expression to search for the "100M" phrase in the message text
    hundred_m_match = re.search(r'100M', message.text)
    
    # If the "100M" phrase was found, add it to the list
    if hundred_m_match:
        hundred_m_list.append(hundred_m_match.group())
    
    # Send a confirmation message
    bot.send_message(message.chat.id, "Phrases added to lists.")

bot.infinity_polling()
