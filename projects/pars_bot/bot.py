from myToken import token
import telebot
from telebot import types
from main import main

data = main()


bot = telebot.TeleBot(token)


number_keyboard = types.ReplyKeyboardMarkup()
buttons = {}
for i in range(1,21):
    buttons['btn' + str(i)] = types.KeyboardButton(str(i))
    number_keyboard.add(buttons['btn'+str(i)])


answer_keyboard = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('Description')
button2 = types.KeyboardButton('Photo')
button3 = types.KeyboardButton('Quit')
answer_keyboard.add(button1, button2, button3)




@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, парсим категорию Все новости')

    if len(data) == 0:
        bot.send_message(message.chat.id, 'На сегодня еще нет новостей')

    count = 0
    for news in data:
        count += 1
        bot.send_message(message.chat.id, str(count) + news[0])
    
    msg = bot.send_message(message.chat.id, 'Какую новость вы хотите посмотреть', reply_markup=number_keyboard)
    bot.register_next_step_handler(msg, check_answer)


def check_answer(message):
    number = int(message.text) - 1
    if number > len(data):
        bot.send_message(message.chat.id, 'Такой новости нет')
        return
    msg = bot.send_message(message.chat.id, 'some title news you can see Description of this news and Photo', reply_markup=answer_keyboard)
    bot.register_next_step_handler(msg, get_info, number)


@bot.callback_query_handler(func=lambda call: True)
def get_info(message, number):
    if message.text == 'Description':
        bot.send_message(message.chat.id, data[number][2])
    elif message.text == 'Photo':
        bot.send_message(message.chat.id, data[number][1])
    elif message.text == 'Quit':
        bot.send_message(message.chat.id, 'Досвидание')
    else:
        bot.send_message(message.chat.id, 'Тфкой кнопки нет')


bot.polling()

















