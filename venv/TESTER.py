import telebot
import re  # For using regular expressions to match phrases

bot = telebot.TeleBot("5608601651:AAHY_d3XgJ14UeEvbT44CWYnexE1UWpIhRQ")

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

bot.polling()
