import telebot
from telebot import types

bot = telebot.TeleBot('5858774048:AAEdJkmNAN27WuOTYNOn6tw7-Ae3MgYvzkE')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b> <u>{message.from_user.last_name}</u>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


#@bot.message_handler()
#def get_user_text(message):
    #if message.text == "Hello":
        #bot.send_message(message.chat.id,'И тебя привет ', parse_mode='html')
    #elif message.text == 'id':
       #bot.send_message(message.chat.id, f'Твой ID:{message.form_user.id}', parse_mode='html')
    #elif message.text == 'photo':
        #photo = open('photo_2023-01-19_15-46-05.jpg', 'rb')
        #bot.send_photo(message.chat.id, photo)
    #elif message.text == 'audio':
        #audio1 = open('01 место -  Tones & I, Dj Noiz - Dance Monkey.mp3', 'rb')
        #bot.send_audio(message.chat.id, audio1)
    #else:
        #bot.send_message(message.chat.id, 'я тебя не понимаю ')



@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'вау какре крутое фото')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Посетить веб сайт', url="https://kinogo.biz/?ysclid=ld3plrfjbf356248814"))
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)




@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('Веб сайт')
    start = types.KeyboardButton('Start')
    markup.add(website, start)
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)

bot.polling(none_stop=True)