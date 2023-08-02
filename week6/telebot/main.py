import telebot


TOKEN = '6013509821:AAFK8qSplatDsxs4nRH9EAw363GtS3SJzQ8'

bot = telebot.TeleBot(TOKEN)


# @bot.message_handler(content_types=['sticker','text'], func=lambda message: True)
# def start_message(message):
#     print(message)
#     bot.send_message(message.chat.id,'привет')
#     # if message.sticker:
#     bot.send_sticker(message.chat.id, message.sticker.file_id)




keyboard = telebot.types.InlineKeyboardMarkup()

button1 = telebot.types.InlineKeyboardButton('да', callback_data='yes')
button2 = telebot.types.InlineKeyboardButton('нет',callback_data='no')

keyboard.row(button1,button2)

# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id,'choose button', reply_markup=keyboard)
#     bot.register_next_step_handler(message, reply_to_button)

# def reply_to_button(message):
#     if message.text == 'да':
#         bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEJmIVkpQI0xMP14-qevTYDLT9O1WKNjAACDgQAAoRRIANbKPfZeJFgiy8E')
#     elif message.text == 'нет':
#         pass
#     else:
#         bot.send_message(message.chat.id, 'нажмите на кнопку')
#         bot.register_next_step_handler(message, reply_to_button)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'choose button', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def handler_callback(call):
    if call.data == 'yes':
        bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAEJmIVkpQI0xMP14-qevTYDLT9O1WKNjAACDgQAAoRRIANbKPfZeJFgiy8E')
    elif call.data == 'no':
        pass



bot.polling()