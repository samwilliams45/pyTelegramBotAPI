import telebot
import datetime

bot = telebot.TeleBot("5608601651:AAHY_d3XgJ14UeEvbT44CWYnexE1UWpIhRQ")

# Create an empty list to store the truck numbers and check-in information
truck_list = []

# Initialize check-in order for each type of sand
type_1_order = 0
type_2_order = 0

# Handle message event and extract truck number and check-in information
@bot.message_handler(content_types=["text"])
def handle_message(message):
    # Extract truck number and check-in information from message
    truck_number = message.text.split()[0]
    check_in_info = message.text.split()[1]
    
    # Create a dictionary to store truck number and check-in information
    truck_data = {"info": check_in_info, "time": datetime.datetime.now()}
    
    # Append the truck data to the list
    truck_list.append(truck_data)
    
    # Sort the list by time of check-in
    truck_list.sort(key=lambda x: x["time"])
    
    # Use list comprehension to separate the truck_list into two lists
    type_1_list = [x['number'] for x in truck_list if x["info"] == "40/70"]
    type_2_list = [x['number'] for x in truck_list if x["info"] == "100M"]
    

def get_sand_type(message, company):
    truck_number = message.text
    bot.send_message(message.chat.id, "Please choose a sand option:", reply_markup=markup)
    bot.register_next_step_handler(message, add_to_list, company=company, truck_number=truck_number)

# Handle the message when the user chooses a sand option
@bot.message_handler(func=lambda message: message.text in sand_orders)
def add_to_list(message, company, truck_number):
    sand_type = message.text
    # Add the user's sand choice to the list
    sand_orders[sand_type].append(f"{company} {truck_number}")
    # Send the updated list to the user
    bot.send_message(message.chat.id, f"Current orders:\n100m: {sand_orders['100m']}\n40/70: {sand_orders['40/70']}")

 # Send the updated list to the user
@bot.message_handler(commands=['list'])
def show_list(message):
    list_message = "Current orders:\n"
    for key in sand_orders:
        list_message += f"{key}: {sand_orders[key]}\n"
    bot.send_message(message.chat.id, list_message)
    
  # Respond to the user with the truck number, check-in information, check-in time, and the truck numbers checked in with each type of sand in separate columns on the same list
    bot.reply_to(message, f"Check-in information: {check_in_info}\nCheck-in time: {truck_data['time'].strftime('%Y-%m-%d %H:%M')}\n\nTruck Numbers for Type 1 Sand: {type_1_list}\nTruck Numbers for Type 2 Sand: {type_2_list}")

if __name__ == "__main__":
    bot.polling()