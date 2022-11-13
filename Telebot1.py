import telebot
import sqlite3
from SmallTalk import smalltalk
from useDataBase import connect
# from useDataBase import DBmanager
# import useDataBase

bot = telebot.TeleBot('5336984475:AAFD5hwCndn7WgDS0NkqOq1-Ws2Kx--Tu50');

#Обработка старта
@bot.message_handler(commands=['start']) 
def start(message):
    hellotext = f'Привет, <b>{message.from_user.first_name}!</b>'
    bot.send_message(message.chat.id, hellotext, parse_mode='html')

# @bot.message_handler(commands=['connect']) 
# def connect_module(message):
#     DBmanager = useDataBase.DBmanager("PyDB2.db")
#     DBmanager.add_user("Виктор")
#     bot.send_message(message.chat.id, "Виктор записан.")
    

@bot.message_handler(commands=['connect']) 
def connect_module(message):
    bot.send_message(message.chat.id, connect())



#Обработка смоллтока
@bot.message_handler()
def sm(message):
    bot.send_message(message.chat.id, smalltalk(message.text))

bot.polling(non_stop=True)
