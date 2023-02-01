import time
import telebot
from telebot import types
bot = telebot.TeleBot("5608601651:AAHY_d3XgJ14UeEvbT44CWYnexE1UWpIhRQ")
commands = {"checkin": "Check in a truck",
            "list": "Show the current list of orders",
            "unload": "unload a truck"}

@bot.message_handler(commands=['help'])
def show_help(message):
    help_message = "Available commands:\n"
    for command, description in commands.items():
        help_message += f"/{command}: {description}\n"
    bot.send_message(message.chat.id, help_message)

# Create a list to store the sand orders
sand_orders = {"100m": [], "40/70": []}

# Create a markup keyboard with the sand options
markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
markup.add("100m", "40/70")

# Keep track of the user that just checked in

last_checkin_user = None

# Handle the message when the user sends /checkin
@bot.message_handler(commands=['checkin', 'Checkin', 'CHECKIN'])
def start(message):
    global last_checkin_user
    last_checkin_user = message.from_user.id
    bot.send_message(message.chat.id, "Please enter your truck number:")
    bot.register_next_step_handler(message, get_sand_type)

@bot.message_handler(commands=['checkin'])
def start(message):
    if message.text.lower() == '/checkin':
        global last_checkin_user
        last_checkin_user = message.from_user.id
        bot.send_message(message.chat.id, "Please enter your truck number:")
        bot.register_next_step_handler(message, get_sand_type)

# Handle the message when the user sends their truck number
def get_sand_type(message):
    global last_checkin_user
    if message.from_user.id != last_checkin_user:
        bot.send_message(message.chat.id, "You have not checked in yet.")
        return
    truck_number = message.text
    bot.send_message(message.chat.id, "Please choose a sand option:", reply_markup=markup)
    bot.register_next_step_handler(message, add_to_list, truck_number=truck_number)

# Handle the message when the user selects a sand option
def add_to_list(message, truck_number):
    global last_checkin_user
    if message.from_user.id != last_checkin_user:
        bot.send_message(message.chat.id, "You have not checked in yet.")
        return
    sand_type = message.text

    # Add the user's sand choice to the list
    sand_orders[sand_type].append(truck_number)

    # Send the updated list to the user
    bot.send_message(message.chat.id, f"Current orders:\n100m: {sand_orders['100m']}\n40/70: {sand_orders['40/70']}")
    last_checkin_user = None

@bot.message_handler(commands=['list'])
def show_list(message):
    list_message = "Current orders:\n"
    for key in sand_orders:
        list_message += f"{key}: {sand_orders[key]}\n"
    bot.send_message(message.chat.id, list_message)

@bot.message_handler(commands=['unload'])
def unload_truck_number(message):
    bot.send_message(message.chat.id, "Please enter your truck number:")
    bot.register_next_step_handler(message, remove_from_list)

def remove_from_list(message):
    truck_number = message.text
    truck = f"{truck_number}"
    for key in sand_orders:
        if truck in sand_orders[key]:
            sand_orders[key].remove(truck)
            bot.send_message(message.chat.id, f"{truck} has been removed from {key} list")
            break
    else:
        bot.send_message(message.chat.id, f"{truck} not found in any list")

bot.polling()