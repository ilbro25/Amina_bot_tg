import telebot
from config import *
from class_guitar import *

API_TOKEN = TOKEN

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler('info')
def send_info(message):
    bot.send_message(message.chat.id, "Ну короче бот, инфы нет. Good luck.")

@bot.message_handler(func=lambda message: True, content_types = ['photo'])
def user_photo(message):
    bot.send_message(message.chat.id, 'Классная фотка.')

@bot.message_handler(func=lambda message: True, content_types = ['voice'])
def user_voice(message):
    bot.send_message(message.chat.id, 'Не могу сейчас прослушать голосовое.')

@bot.message_handler('guitar')
def class_guitar(message):
    args1 = (telebot.util.extract_arguments(message.text)).split()
    guitar1 = Guitar(brand = args1[0], form = args1[1])
    bot.send_message(message.chat.id, guitar1.info())


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)



bot.infinity_polling()