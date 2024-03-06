import telebot;
from telebot import types

token_file = open("token.txt")
token = token_file.read()

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"Добро пожаловать в бота PC Free Simulator сохранения!\nДля получения информации по боту напишите /help")\

@bot.message_handler(commands=['start'])
def start(message):
    

bot.polling(none_stop=True, interval=0)
